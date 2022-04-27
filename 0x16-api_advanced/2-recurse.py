#!/usr/bin/python3
"""Defines a function that queries the Reddit API."""
import requests


def recurse(subreddit, hot_list=[], fullname=None):
    """Returns a list containing the titles of all hot articles for a given
    subreddit.
    - Returns None if no results are found for the given subreddit.
    """
    api_url = "https://reddit.com/r/" + subreddit + "/hot.json"
    headers = {'User-Agent': 'MyAPI/0.01'}

    response = requests.get(api_url, headers=headers)
    if fullname is not None:
         response = requests.get(api_url, headers=headers, params={
                                'after': fullname})

    if response.status_code >= 300:
        return None

    post = response.json()['data']['children'][0]
    hot_list.append(post['data']['title'])
    fullname = post['kind'] + '_' + post['data']['id']

    if response.get(after) is None:
        return hot_list

    recurse(subreddit, hot_list, fullname=fullname)
