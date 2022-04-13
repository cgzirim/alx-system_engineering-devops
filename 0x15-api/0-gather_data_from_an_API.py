#!/usr/bin/python3
"""Returns information about a given employee todo list progress."""
import requests
from sys import argv


url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(argv[1])).json()['name']
tasks = [d for d in requests.get(url + "todos").json() \
        if d["userId"] == int(argv[1])]

tsks_done = 0
tsks_num = 0
for t in tasks:
        tsks_num += 1
        if t['completed']:
                tsks_done += 1
print("Employee {} is done with tasks({}/{}):".format(user, tsks_done,
tsks_num))
[print("\t " + t['title']) for t in tasks if t['completed']]
