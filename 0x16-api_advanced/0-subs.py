#!/usr/bin/python3
'''
this module imports
the number of subscribers
in a subreddit
'''
import requests


def number_of_subscribers(subreddit):
    '''
    function to get no of subscribers
    '''
    headers = {'User-Agent': 'subs'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
