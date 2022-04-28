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
            'limit': 100})

    if response.status_code >= 300:
        return None

    for post in response.json()['data']['children']:
        hot_list.append(post['data']['title'])

    after = response.json().get("data").get("after")

    if after is not None:
        recurse(subreddit, hot_list, after=after)
    return hot_list


def count_words(subreddit, word_list):
    """Prints a sorted count of given keywords (case-insensitive, delimited
    by spaces) in the titles of all hot articles in a subreddit.

    Args:
        subreddit (str): Subreddit's name.
        word_list (list): List of keywords to count.

    - If word_list contains the same word, the final count is the same for
      separate keywords.
    - Result is printed in decending order, by count. If count is the same
      for separate keywords, they are sorted alphabetically.
    - Results are based on the number of times a keyword appears in a title.
    - If no posts match or the subreddit is invalid, print nothing.
    """
    hot_list = recurse(subreddit, [])
    if hot_list is None:
        return

    result = {word.lower(): 0 for word in word_list}

    for title in hot_list:
        title = title.lower()
        array = title.split(" ")
        for key_word in word_list:
            key_word = key_word.lower()
            result[key_word] += array.count(key_word)

    # Sort result alphabetically
    result = dict(sorted(result.items(), key=lambda item: item[0]))

    # Sort result numerically
    result = dict(sorted(
        result.items(),
        reverse=True,
        key=lambda item: item[1]))

    for key, value in result.items():
        if value > 0:
            print("{}: {}".format(key, value))
