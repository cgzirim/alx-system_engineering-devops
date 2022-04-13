#!/usr/bin/python3
"""Export data in the JSON format."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    username = requests.get(url + "users/{}".format(
        argv[1])).json()['username']
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    dicts = []
    for t in tasks:
        dicts.append({"task": t['title'], "completed": t['completed'],
                      "username": username})
    data = {user_id: dicts}

    jsonString = json.dumps(data)
    with open("{}.json".format(user_id), 'w') as f:
        f.write(jsonString)
