#!/usr/bin/python3
"""Exports records of all tasks from all employees in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    data = {}
    for user in users:
        u_id = user['id']
        username = user['username']
        tasks = requests.get(url + "todos", params={'user_Id': u_id}).json()

        dicts = []
        for t in tasks:
            dicts.append({"task": t['title'],
                         "completed": t['completed'], "username": username})
        data[u_id] = dicts

    jsonString = json.dumps(data)
    with open("todo_all_employees.json", 'w') as f:
        f.write(jsonString)
