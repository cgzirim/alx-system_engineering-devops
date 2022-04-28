#!/usr/bin/python3
"""Defines a function that queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list containing the titles of all hot articles for a given
    subreddit.
    - Returns None if no results are found for the given subreddit.
    """
    api_url = "https://reddit.com/r/" + subreddit + "/hot.json"
    headers = {'User-Agent': 'MyAPI/0.01'}

    response = requests.get(api_url, headers=headers)
    if after is not None:
        response = requests.get(api_url, headers=headers, params={
            'after': after,
            'limit': 100},
            allow_redirects=False)

    if response.status_code >= 300:
        return None

    for post in response.json()['data']['children']:
        hot_list.append(post['data']['title'])

    after = response.json().get("data").get("after")

    if after is not None:
        recurse(subreddit, hot_list, after=after)
    return hot_list
