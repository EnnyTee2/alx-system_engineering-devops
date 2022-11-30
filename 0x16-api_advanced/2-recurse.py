#!/usr/bin/python3
"""Function to recursively query hot posts in a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns a list containing the titles
    of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_\
        64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404 or response.status_code == 301:
        return None
    results = response.json().get("data").get("children")
    after = response.json().get('after')
    for res in results:
        hot_list.append(res.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list=hot_list, after=after)
    else:
        return hot_list
