#!/usr/bin/python3
"""Defines a function that queries the Reddit API."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given
    subreddit.
    """
    api_url = "https://reddit.com/r/" + subreddit + "/hot.json"
    headers = {'User-Agent': 'MyAPI/0.01'}

    response = requests.get(api_url, headers=headers, params={'limit': '10'})
    if response.status_code >= 300:
        print("None")
        return

    for post in response.json()['data']['children']:
        print(post['data']['title'])
