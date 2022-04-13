#!/usr/bin/python3
"""Export data in the CSV format."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    username = requests.get(url + "users/{}".format(
        argv[1])).json()['username']
    tasks = requests.get(url + "todos", params={"userId": user_id}).json()

    data = []
    for t in tasks:
        row = []
        row.append(user_id)
        row.append(username)
        row.append(t['completed'])
        row.append(t['title'])
        data.append(row)

    with open("{}.csv".format(argv[1]), 'w', newline="") as f:
        csvwriter = csv.writer(f, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(data)
