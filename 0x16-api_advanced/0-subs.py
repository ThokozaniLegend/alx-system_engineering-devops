#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for a 404 status code which indicates that the subreddit doesn't exist
        if response.status_code != 200:
            return 0

        # Parse the response and safely access the data
        results = response.json().get("data", {})
        return results.get("subscribers", 0)  # Return 0 if 'subscribers' key is missing

    except requests.RequestException:
        # Return 0 if there is any request-related error (network issues, etc.)
        return 0


