#!/usr/bin/python3
"""Function to recursively query hot posts in a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ returns a list containing the titles
    of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_\
        64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    }
    if after == '':
        response = requests.get(url, headers=headers, allow_redirects=False)
    else:
        response = requests.get(url, headers=headers, after=after, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    aft = response.json().get('data').get('after')
    for res in results.get('children'):
        hot_list.append(res.get('data').get('title'))
    if after != '':
        return recurse(subreddit, hot_list, after=aft)
    return hot_list
