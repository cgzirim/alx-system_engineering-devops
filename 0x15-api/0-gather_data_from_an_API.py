#!/usr/bin/python3
"""Returns information on TODO list progress for a given employee Id
using REST API."""
import requests
from sys import argv


if __name__ == "__main__":
	api_url = "https://jsonplaceholder.typicode.com/"
	response = requests.get(api_url)
	print(response.json())

"Employee {} is done with tasks({}/{}):".format()
