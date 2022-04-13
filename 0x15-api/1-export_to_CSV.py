#!/usr/bin/python3
"""Export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()['username']
    tasks = requests.get(url + "todos", params={"userId": argv[1]}).json()

    data = []
    for t in tasks:
        row = []
        row.append("{}".format(argv[1]))
        row.append("{}".format(user))
        row.append("{}".format(t['completed']))
        row.append("{}".format(t['title']))
        data.append(row)

    with open("{}.csv".format(argv[1]), 'w', newline="") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(data)
