#!/usr/bin/python3
"""Returns information about a given employee todo list progress."""
import requests
from sys import argv


if __name__ == "__main__":
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url + "users/{}".format(argv[1])).json()['name']
        tasks = requests.get(url + "todos", params={"userId": argv[1]}).json()
        print(requests.get(url + "todos", params={"userId": argv[1]}).url)

        completed = [t["title"] for t in tasks if t["completed"] is True]
        print("Employee {} is done with tasks({}/{}):".format(user,
        len(completed), len(tasks)))
        [print("\t {}".format(t)) for t in completed]
