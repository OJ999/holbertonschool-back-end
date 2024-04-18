#!/usr/bin/python3
"""
Write a Python script that, using this REST API.
"""
import csv
import requests # type: ignore
import sys


if __name__ == '__main__':
    id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + id
    res = requests.get(url_user).json()
    u = res.get("username")
    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id) + '/todos')
    with open("{}.csv".format(id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in req.json():
            writer.writerow([id, u,
                            t.get("completed"), t.get("title")])