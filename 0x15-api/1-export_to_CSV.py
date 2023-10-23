#!/usr/bin/python3
'''
gather data from an API
'''
import csv
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

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            task_completed_status = "True" \
                    if todo.get('completed') \
                    else "False"
            task_title = todo.get('title')
            writer.writerow([employee_id,
                             employee_user_name,
                             task_completed_status,
                             task_title])
