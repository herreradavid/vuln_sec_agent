
sample_developers = {
    "andrew": {
        "velocity": 7,
        "email": "andrew@tlltcompany.com"
    },
     "stella": {
        "velocity": 7,
        "email": "stella@tlltcompany.com"
     },
     "peter": {
        "velocity": 7,
        "email": "stella@tlltcompany.com"
     }
}

def sample_backlog():
    task_backlog = [
        {"task_name":"integrate Bitbucket", "decription":"add new ingration with bitbucket", "story_points":3, "id":"cqocvn", "type":"dev", "priority": 7, "repo_id": "bank1/trasact", "assignee":"unassigned"},
        {"task_name":"Add php tool for application sec testing", "decription":"add new ingration with php sonarQuebe", "story_points":2,"id":"mews","type":"security fix",  "priority": 9, "repo_id": "sec/go-unsafepointer-poc","assignee":"unassigned"},
        {"task_name":"Add installation workflow", "decription":"add automation to installation workflow", "story_points":4,"id":"rs0wke", "type":"dev", "priority": 5, "repo_id": "bank1/trasact","assignee":"unassigned"},
        {"task_name":"add package scanning with yarn audit", "decription":"add automation to installation workflow", "story_points":2,"id":"msgfow", "type":"dev", "priority": 5, "repo_id": "bank1/trasact","assignee":"unassigned"},
        {"task_name":"Add installation workflow", "decription":"add automation to installation workflow", "story_points":4,"id":"kefiw", "type":"dev", "priority": 4, "repo_id": "sec/go-unsafepointer-poc","assignee":"unassigned"}
    ]
    return task_backlog

def add_task_backlog(task_backlog, tasks):
    task_backlog.extend(tasks)
    return task_backlog

def by_priority_then_points(task):
    return (-task["priority"], task["story_points"])

def assign_sprint(sprint, developers=None):
    if developers == None:
        developers = sample_developers
    sprint_devs = { dev_name: dev["velocity"] for dev_name, dev in developers.items() }
    remaining_capacity = sprint_devs.copy()
    for task in sprint:
        for dev_name, capacity in sprint_devs.items():
            if remaining_capacity[dev_name] >= task["story_points"]:
                task["assignee"] = dev_name
                remaining_capacity[dev_name] -= task["story_points"]
                break  # Assigning task to first dev who can take it and then stopping

def compute_next_sprint(task_backlog=None, sprint_capacity=21, developers=None):
    if task_backlog == None:
       task_backlog = sample_backlog()
    if developers == None:
       developers = sample_developers
    task_backlog.sort(key=by_priority_then_points)
    estimation = 0
    sprint = []
    for task in task_backlog:
        if estimation + task["story_points"] > sprint_capacity:
            break
        sprint.append(task)
        estimation += task["story_points"]
    assign_sprint(sprint, developers) 
    return sprint

def parse_report(report):
    task_name = report['Code Analysis']['Details']
    description = report['Subjective Priority']['Description']
    priority = report['Subjective Priority']['Value']
    story_points = report['Fix']['story_points']
    path = report['file']
    print(path.rsplit('/'))
    id_name = path.split('/')[-1].split('.')[0]
    line = report['line']
    type = task_name.split()[0].lower()
    return {
        "task_name": f"Finding: {task_name}",
        "description": description,
        "story_points": story_points ,
        "id": f"{id_name}-{line}-{type}",
        "type": "security-finding",
        "priority": priority,
        "location": path,
        "assignee": "unassigned"
    }
    