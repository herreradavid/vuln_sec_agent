package repository

import "david/internal/entity"

type ProductRepository interface {
	GetByIdVulnerable(id string) (*entity.Product, error)
}

type NoteRepository interface {
	GetById(id string) (*entity.Note, error)
	GetLimited() ([]entity.Note, error)
}
