#!/usr/bin/python3
"""Contains the recursive function to count sorted keywords"""

import requests


def def count_words(subreddit, word_list)
    """queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by space"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_\
        64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    }
    params = {
        "after": after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    for thread in results.get("children"):
        hot_list.append(thread.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
