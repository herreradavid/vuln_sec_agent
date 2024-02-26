### "file": "/david-ml/server/internal/handlers/handlers.go"


- Subjective Priority
8
Database arbitrary query execution

- Fix estimation: 3h
1 line affected
5 additional places for user input validation


- Score
severity = score["MEDIUM"]
confidence = score["HIGH"]
score = severity * confidence = 6

- Code analysis
Real confidence = HIGH
"details": "SQL string formatting"

- Exploitability
Medium, automated


- Is test?
No


- CWE Scope Impact
CIA





### "file": "/david-ml/server/internal/repository/product/product.go",


- Subjective Priority
7
Web server file disclosure and execution

- Fix estimation: 2h
1 line affected with  extra dependencies
3 additional places for user input validation


- Score
severity = score["MEDIUM"]
confidence = score["HIGH"]
score = severity * confidence = 6

- Code analysis
Real confidence = HIGH
"details": "Potential file inclusion via variable",

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
CIA




### "file": "/david-ml/server/internal/app/app.go"


- Subjective Priority
5
HTTP timeouts are necessary to expire inactive connections and failing to do so might make the application vulnerable to attacks like slowloris which work by sending data very slow, which in case of no timeout will keep the connection active eventually leading to a denial-of-service (DoS) attack.


- Fix estimation: 1h
1 lines_affected with 0 extra dependencies
Fix: 
    server := &http.Server{
        Addr:              ":8080",
        ReadHeaderTimeout: 3 * time.Second,
    }


- Score
severity = score["MEDIUM"]
confidence = score["HIGH"]
score = severity * confidence = 6

- Code analysis
Real confidence = HIGH
"details": "Use of net/http serve function that has no support for setting timeouts"


- Exploitability
Medium


- Is test?
No


- CWE Scope Impact
A

