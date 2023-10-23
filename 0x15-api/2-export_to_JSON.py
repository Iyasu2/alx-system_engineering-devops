#!/usr/bin/python3
'''
gather data from an API
'''
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    response = requests.get(employee_url)

    employee_data = response.json()
    employee_user_name = employee_data.get('username')

    response = requests.get(todos_url)

    todos = response.json()

    export_data = {
            f"{employee_id}": []
            }
    for todo in todos:
        task_completed_status = todo.get('completed')
        task_title = todo.get('title')
        user_data = {
                "task": task_title,
                "completed": task_completed_status,
                "username": employee_user_name
                }
        export_data[f"{employee_id}"].append(user_data)

    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(export_data, jsonfile)
