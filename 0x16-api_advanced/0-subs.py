"""
This module contains a function to query the Reddit API
and return the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers if subreddit exists, 0 otherwise.
    """
    # Define the user agent to avoid 'Too Many Requests' errors
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Send a GET request to the Reddit API to fetch subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)

    # Check if the subreddit exists and if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        # If subreddit does not exist or any other error occurs
        return 0
