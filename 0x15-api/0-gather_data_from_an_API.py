#!/usr/bin/python3
'''
gather data from an API
'''
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(employee_url)

    employee_data = response.json()
    employee_name = employee_data.get('name')

    response = requests.get(todos_url)

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = []
    for todo in todos:
        if todo.get('completed'):
            completed_tasks.append(todo)
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
