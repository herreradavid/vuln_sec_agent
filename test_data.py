
# 28 story points, 10 dev1 and 11 dev2
test_developers = {
    "dev1": {
        "velocity": 10,
        "email": "dev1@dev.com"
    },
    "dev2": {
        "velocity": 18,
        "email": "dev2@dev.com"
    },
}

expected_sprint = [
    {
        "task_name": "Add php tool for application sec testing",
        "decription": "add new ingration with php sonarQuebe",
        "story_points": 2,
        "id":"mews","type":"security fix",
        "priority": 9,
        "repo_id": "sec/go-unsafepointer-poc",
        "unassigned":"dev1"
    },
    {
        "task_name": "Audit unsafe calls in struct-cast",
        "description": "Buffer overflow possibly leading to arbitrary code execution from user inputs.",
        "story_points": 3,
        "id": "struct-cast-main-go",
        "type": "security finding",
        "priority": 9,
        "repo_id": "go-unsafepointer-poc/struct-cast/main.go",
        "assignee": "dev2"
    },
    {
        "task_name": "Fix race condition in slice types",
        "description": "Use-after-free vulnerability due to a garbage collector race condition causing a use-after-free vulnerability.",
        "story_points": 3,
        "id": "race-slice-main-go",
        "type": "security finding",
        "priority": 9,
        "repo_id": "go-unsafepointer-poc/race-slice/main.go",
        "assignee": "dev2"
    }, 
]

finding_tasks = [
    {
        "task_name": "Audit unsafe calls in struct-cast",
        "description": "Buffer overflow possibly leading to arbitrary code execution from user inputs.",
        "story_points": 3,
        "id": "struct-cast-main-go",
        "type": "security finding",
        "priority": 9,
        "repo_id": "go-unsafepointer-poc/struct-cast/main.go",
        "assignee": "unassigned"
    },
    {
        "task_name": "Fix race condition in slice types",
        "description": "Use-after-free vulnerability due to a garbage collector race condition causing a use-after-free vulnerability.",
        "story_points": 3,
        "id": "race-slice-main-go",
        "type": "security finding",
        "priority": 9,
        "repo_id": "go-unsafepointer-poc/race-slice/main.go",
        "assignee": "unassigned"
    },
    {
        "task_name": "Address information leak",
        "description": "Buffer overflow leading to information leak in memory.",
        "story_points": 3,
        "id": "information-leak",
        "type": "security finding",
        "priority": 9,
        "repo_id": "go-unsafepointer-poc/information-leak/main.go",
        "assignee": "unassigned"
    },
    {
        "task_name": "Fix HTTP request vulnerability",
        "description": "The adversary can send HTTP requests to any server on the internet and determine the response status code, useful for IP spoofing during host enumeration and DoS attacks.",
        "story_points": 2,
        "id": "main-go-1",
        "type": "security fix",
        "priority": 6,
        "repo_id": "main.go",
        "assignee": "unassigned"
    },
    {
        "task_name": "Correct file closure in test",
        "description": "Deferring unsafe method \"Close\" on type \"*os.File\", leaving a file open is not high risk in a test environment.",
        "story_points": 1,
        "id": "test-main-go",
        "type": "security finding",
        "priority": 2,
        "repo_id": "test/main.go",
        "assignee": "unassigned"
    },
    {
        "task_name": "Review use of unsafe calls in go-fuse",
        "description": "Potential issue with use of unsafe calls needs auditing.",
        "story_points": 2,
        "id": "go-fuse-opcode",
        "type": "security finding",
        "priority": 3,
        "repo_id": "go-unsafepointer-poc/go-fuse/opcode.go",
        "assignee": "unassigned"
    }
]

task_backlog = [
    {"task_name":"integrate Bitbucket", "decription":"add new ingration with bitbucket", "story_points":3, "id":"cqocvn", "type":"dev", "priority": 7, "repo_id": "bank1/trasact", "assignee":"unassigned"},
    {"task_name":"Add php tool for application sec testing", "decription":"add new ingration with php sonarQuebe", "story_points":2,"id":"mews","type":"security fix",  "priority": 9, "repo_id": "sec/go-unsafepointer-poc","assignee":"unassigned"},
    {"task_name":"Add installation workflow", "decription":"add automation to installation workflow", "story_points":4,"id":"rs0wke", "type":"dev", "priority": 5, "repo_id": "bank1/trasact","assignee":"unassigned"},
    {"task_name":"add package scanning with yarn audit", "decription":"add automation to installation workflow", "story_points":2,"id":"msgfow", "type":"dev", "priority": 5, "repo_id": "bank1/trasact","assignee":"unassigned"},
    {"task_name":"Add installation workflow", "decription":"add automation to installation workflow", "story_points":4,"id":"kefiw", "type":"dev", "priority": 4, "repo_id": "sec/go-unsafepointer-poc","assignee":"unassigned"}
]


parsed_report = {
    "task_name": "Finding: SQL string formatting",
    "description": "Database arbitrary query execution",
    "story_points": 3,
    "id": "handlers-89-sql",
    "type": "security-finding",
    "priority": 8,
    "location": "server/internal/handlers/handlers.go",
    "assignee": "unassigned"
}

json_open_ai_output = '''{
    "file": "go-unsafepointer-poc/go-fuse/exploit.go",
    "line": 16,
    "Subjective Priority": {
        "Value": 4,
        "Description": "Use of unsafe operations for memory manipulation"
    },
    "Fix": {
        "story_points": 2,
        "lines_affected": 1
    },
    "Score": {
        "Severity": "LOW",
        "Confidence": "HIGH",
        "Value": 3
    },
    "Code Analysis": {
        "Real_impact": "MEDIUM",
        "Details": "Use of unsafe calls should be audited"
    },
    "Exploitability": "Difficult",
    "Is Test?": "No",
    "CWE Scope Impact": "Integrity and Confidentiality"
}'''