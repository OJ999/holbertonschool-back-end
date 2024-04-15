#!/usr/bin/python3
"""
Script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user info
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    user_data = user_response.json()

    # Fetch TODO list
    todo_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id))
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    done_tasks = sum(1 for task in todo_data if task['completed'])

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data['name'], done_tasks, total_tasks))
    for task in todo_data:
        if task['completed']:
            print("\t {}".format(task['title']))
