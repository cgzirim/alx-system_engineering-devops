#!/usr/bin/python3
"""Defines a function that queries Reddit API."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.

    - If an invalid subreddit is given, the function should returns 0.
    - Uses a custom User-Agent.
    """
    api_url = "https://reddit.com/r/" + subreddit + "/about.json"
    headers = {'User-Agent': 'MyAPI/0.01'}

    response = requests.get(api_url, headers=headers)
    if response.status_code >= 300:
        return 0

    return (response.json()['data']['subscribers'])
