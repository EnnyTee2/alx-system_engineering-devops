#!/usr/bin/python3
"""Contains Function to query subscribers on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot
       posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_\
        64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
