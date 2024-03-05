#!/usr/bin/python3
"""Function to print post given by reddit subreddit"""
import requests

def top_ten(subreddit):
    """will print the title of the hottest posts on subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api_advanced:v1.0.0 (by /u/bdov_)"
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
