#!/usr/bin/python3
"""Defines a function that queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], fullname=None, count=0):
    """Returns a list containing the titles of all hot articles for a given
    subreddit.
    - Returns None if no results are found for the given subreddit.
    """
    api_url = "https://reddit.com/r/" + subreddit + "/hot.json"
    headers = {'User-Agent': 'MyAPI/0.01'}

    response = requests.get(api_url, headers=headers)

    if response.status_code >= 300:
        return None

    try:
        post = response.json()['data']['children'][count]
        hot_list.append(post['data']['title'])
    except IndexError:
        return hot_list

    count += 1
    recurse(subreddit, hot_list, count=count)
