#!/usr/bin/python3
'''
gather data from an API
'''
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    response = requests.get(users_url)

    employees = response.json()

    response = requests.get(todos_url)

    todos = response.json()

    export_data = {}
    for employee in employees:
        employee_id = employee.get('id')
        employee_user_name = employee.get('username')

        export_data[employee_id] = []

        for todo in todos:
            if todo.get('userId') == employee_id:
                task_title = todo.get('title')
                completed_task_status = todo.get('completed')
                user_data = {
                        "username": employee_user_name,
                        "task": task_title,
                        "completed": completed_task_status
                        }

                export_data[employee_id].append(user_data)

    filename = f"todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        json.dump(export_data, jsonfile)
