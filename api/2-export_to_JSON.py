#!/usr/bin/python3
"""Using what you did in the task #0
 extend your Python script
 to export data in the JSON format."""

import json
import requests # type: ignore
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user_data = requests.get(url + "users/" + user_id).json()
    todo_data = requests.get(url + "todos?userId=" + user_id).json()

    tasks = []
    for task in todo_data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_data["username"]
        }
        tasks.append(task_dict)

    data = {user_id: tasks}

    with open(user_id + '.json', 'w') as f:
        json.dump(data, f)