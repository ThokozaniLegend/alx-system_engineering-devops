#!/usr/bin/python3
"""
Uses Reddit API to print the number of subscribers of a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.
    
    Returns:
    int: Number of subscribers or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    num_subs = data.get("subscribers", 0)  # Handle missing 'subscribers'

    return num_subs

