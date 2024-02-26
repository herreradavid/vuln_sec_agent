import pytest
from sprint import add_task_backlog, compute_next_sprint, sample_backlog, assign_sprint, by_priority_then_points
from test_data import finding_tasks, expected_sprint, task_backlog, test_developers
from copy import copy

def test_sample_backlog():
    assert sample_backlog() == task_backlog

def test_add_task_backlog():
    backlog_copy = copy(task_backlog)
    add_task_backlog(backlog_copy, [{"priority": 1, "story_points": 3}, {"priority": 2, "story_points": 2}])
    assert len(backlog_copy) == len(task_backlog) + 2

# Test sorting with by_priority_then_points
def test_by_priority_then_points():
    tasks = [{"priority": 1, "story_points": 3}, {"priority": 2, "story_points": 2}]
    tasks.sort(key=by_priority_then_points)
    assert tasks == [{"priority": 2, "story_points": 2}, {"priority": 1, "story_points": 3}]

# Test compute_next_sprint with mocked task_backlog
def test_compute_next_sprint():
    task_backlog = [{"priority": 3, "story_points": 5, "assignee": "unassigned"},
                    {"priority": 2, "story_points": 7, "assignee": "unassigned"},
                    {"priority": 1, "story_points": 9, "assignee": "unassigned"}]
    sprint = compute_next_sprint(task_backlog, sprint_capacity=12)
    assert len(sprint) == 2  # Only two tasks can fit within the capacity

# Test compute_next_sprint with expected_sprint
def test_compute_next_sprint():
    task_backlog = [{"priority": 3, "story_points": 5, "assignee": "unassigned"},
                    {"priority": 2, "story_points": 7, "assignee": "unassigned"},
                    {"priority": 1, "story_points": 9, "assignee": "unassigned"}]
    sprint = compute_next_sprint(task_backlog, sprint_capacity=12)
    assert len(sprint) == 2  # Only two tasks can fit within the capacity

# Test assign_sprint
def test_assign_sprint():
    sprint = [{"priority": 3, "story_points": 5, "assignee": "unassigned"},
              {"priority": 2, "story_points": 7, "assignee": "unassigned"}]
    assign_sprint(sprint)
    assert all(task["assignee"] != "unassigned" for task in sprint)  # Ensuring all tasks are assigned

# Test to check if compute_next_sprint correctly selects tasks based on capacity and priority
def test_compute_next_sprint_with_finding_tasks():
    backlog = finding_tasks
    sprint = compute_next_sprint(backlog, sprint_capacity=10)
    # Expecting tasks to be selected based on priority, then points, without exceeding capacity
    expected_tasks = ["Audit unsafe calls in struct-cast", "Fix race condition in slice types", "Address information leak"]
    assert [task["task_name"] for task in sprint] == expected_tasks

# def test_compute_next_sprint_with_expeced_sprint():
#     backlog = task_backlog + finding_tasks
#     sprint = compute_next_sprint(backlog, 28, test_developers)
#     assert sprint == expected_sprint

# Run the tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()


