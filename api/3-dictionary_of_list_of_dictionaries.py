#!/usr/bin/python3
"""Using what you did in the task#0
 extend your Python script
 to export data in the JSON format."""

import json
import requests # type: ignore
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    user_u = requests.get(f"{url}/users")
    todo_u = requests.get(f"{url}/todos")
    if user_u.ok is False or todo_u.ok is False:
        print("Error: API request failed.")
        sys.exit(1)

    user_data = user_u.json()
    todo_data = todo_u.json()

    user_dict = {}
    for user in user_data:
        user_id = user["id"]
        username = user["username"]
        user_dict[user_id] = []
        for todo in todo_data:
            if user_id == todo["userId"]:
                user_dict[user_id].append({
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"]
                })

    with open("todo_all_employees.json", "w") as f:
        json.dump(user_dict, f)