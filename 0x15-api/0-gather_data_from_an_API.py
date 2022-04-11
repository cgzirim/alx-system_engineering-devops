#!/usr/bin/python3
"""Returns information on TODO list progress for a given employee Id
using REST API."""
import requests
from sys import argv


if __name__ == "__main__":
	api_url = "https://jsonplaceholder.typicode.com/"
	user = requests.get(api_url + "users/{}".format(argv[1])).json()
	todos = requests.get(api_url + "todos", params={"userId": argv[1]}).json()

	completed = [t.get("title") for t in todos if t.get("completed") is True]
	print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
	[print("\t {}".format(t)) for t in completed]
