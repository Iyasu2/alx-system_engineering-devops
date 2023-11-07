#!/usr/bin/python3
"""
this module imports the number of subscribers in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    '''
    function to get no of subscribers
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {'User-Agent': '0x16-api_advanced:project:\
            v1.0.0 (by/u/Iyasu Asnake)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        if response.status_code == 200:
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception as e:
        return 0
