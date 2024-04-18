#!/usr/bin/python3
"""
Script that, using a given REST API, retrieves information about an employee's TODO list progress.
"""

import sys
import requests # type: ignore


def fetch_employee_todo_progress(employee_id):
    """
    Fetches and displays information about an employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee whose progress is to be retrieved.

    Returns:
        None
    """
    # API URL for employee's TODO list
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    # Fetch data from the API
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No TODO list found for employee with ID:", employee_id)
        return

    # Count completed and total tasks
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Employee name
    employee_name = todos[0]['username']

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for todo in todos:
        if todo['completed']:
            print("\t", todo['title'])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)
