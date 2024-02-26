package product

import (
	"database/sql"
	"errors"
	"fmt"
	"david/internal/entity"
	"david/internal/repository"
)

type productRepository struct {
	db *sql.DB
}

// checking for compliance of the methods of the model and its interface
var _ repository.ProductRepository = (*productRepository)(nil)

func New(db *sql.DB) (*productRepository, error) {
	const op = "vulnerable.internal.repository.product_repository.NewProductRepository"

	queries := []string{
		`CREATE TABLE Products (
			id INTEGER PRIMARY KEY,
			name VARCHAR(255),
			description TEXT,
			price INT
        );`,
		`CREATE TABLE flags (
		  	id INTEGER PRIMARY KEY ,
		  	flag TEXT
		);`,
		`INSERT INTO Products (name, description, price) VALUES 
			('Product 1', 'This is product 1', 100),
			('Product 2', 'This is product 2', 200),

		`,
		`INSERT INTO flags (flag) VALUES 
			('fake flag'),
			('WB{n1c3_tr9_y0u_w1n}');
		`,
	}

	for _, query := range queries {
		_, err := db.Exec(query)
		if err != nil {
			fmt.Errorf("%s: %w", op, err)
		}
	}

	return &productRepository{db: db}, nil
}

func (r *productRepository) GetByIdVulnerable(id string) (*entity.Product, error) {
	const op = "vulnerable.internal.repository.product_repository.GetByIdVulnerable"

	stmt := `SELECT id, description FROM Products WHERE id = ` + id

	product := &entity.Product{}

	err := r.db.QueryRow(stmt).Scan(&product.ID, &product.Name)
	if err != nil {
		if errors.Is(err, sql.ErrNoRows) {
			return nil, fmt.Errorf("%s: %w", "No rows returned", err)
		}
		return nil, fmt.Errorf("%s: %w", op, err)
	}

	return product, nil
}
