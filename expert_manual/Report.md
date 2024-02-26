### Rule #1
if confidence >= medium
    priority = confidence * severity

score = {
    "HIGH": 3,
    "MEDIUM": 2,
    "LOW": 1,
}


### Rule 2
if nosec == true, exclude


Based on the severity and confidence the first arrangement of priorities is:



## 0 "file": "/main.go"


- Subjective Priority
6 because is easy to fix and it can reach other systems over the network.


- Fix estimation: 1h
Only 1 line affected with 0 dependencies

- Score
severity = score["MEDIUM"]
confidence = score["MEDIUM"]
score = severity * confidence = 4

- Code analysis
The adversary can send HTTP requests to any server on the internet and determine
the response status code. Useful for IP spoffing during host enumeration and DoS attacks.
Real confidence = HIGH
details": "Potential HTTP request made with variable url",

- Exploitability
Easy

- Is test?
No

- CWE Scope Impact
Confidentiality
Integrity
Availability
Other

- CWE Technical Impact
Technical Impact: Execute Unauthorized Code or Commands; Alter Execution Logic; Read Application Data; Modify Application Data
An attacker could include arguments that allow unintended commands or code to be executed, allow sensitive data to be read or modified or could cause other unintended behavior.




## 1"file": "/test/main.go"

- Subjective Priority
2 because is a test an leaving a file open is not high risk.
In this case the program finishes after the defer call, therefore
the resources are immediatelly returned to the OS.

- Fix estimation: <1h
Only 1 line affected with 0 dependencies
Correct code: file.Close()


- Score
severity = score["MEDIUM"]
confidence = score["HIGH"]
score = severity * confidence = 6

- Code analysis
Real confidence = HIGH
Real technical impact = System resource usage
details": "Deferring unsafe method \"Close\" on type \"*os.File\""

- Exploitability
Easy


- Is test?
Yes


- CWE Scope Impact
Confidentiality
Availability
Integrity


- CWE Technical Impact
Read Application Data; DoS: Crash, Exit, or Restart; Unexpected State



### 2 "file": "/go-unsafepointer-poc/struct-cast/main.go",

- Subjective Priority
9 because the vulnerability is a buffer overflow.
Assuming arbitrary code execution is possible from user inputs
(not possible in the sample code, in that case the impact is only to leak arbitrary memory)


- Fix estimation: 1h
4 lines_affected with 0 extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
Real technical impact = System resource usage
"details": "Use of unsafe calls should be audited"


- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other



### 3 "file": "/go-unsafepointer-poc/race-slice/main.go"


- Subjective Priority
9 assuming the inputs could be controlled by the adversay
insecure casting pattern for slice types leads to a garbage collector
race condition that causes a use-after-free vulnerability
(not possible in the sample code, in that case the impact is only to overwirite a buffer with random data)


- Fix estimation: 1h
3 lines_affected with at least 1 extra dependency


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other




### "/go-unsafepointer-poc/information-leak/main.go" 14


- Subjective Priority
9 buffer overflow, leak of information in memory

- Fix estimation: 1h
3 lines_affected with 0 extra dependencies

- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy

- Is test?
No

- CWE Scope Impact
Other




### "/go-unsafepointer-poc/go-fuse/opcode.go" L25


- Subjective Priority


- Fix estimation: 1h
2 lines_affected with 0 extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other





### 


- Subjective Priority


- Fix estimation: 1h
 lines_affected with  extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other





### 


- Subjective Priority


- Fix estimation: 1h
 lines_affected with  extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
Real technical impact = 
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other






### 


- Subjective Priority


- Fix estimation: 1h
 lines_affected with  extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
Real technical impact = 
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other





### 


- Subjective Priority


- Fix estimation: 1h
 lines_affected with  extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
Real technical impact = 
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other






### 


- Subjective Priority


- Fix estimation: 1h
 lines_affected with  extra dependencies


- Score
severity = score["LOW"]
confidence = score["HIGH"]
score = severity * confidence = 3

- Code analysis
Real confidence = HIGH
Real technical impact = 
"details": "Use of unsafe calls should be audited"

- Exploitability
Easy


- Is test?
No


- CWE Scope Impact
Other


