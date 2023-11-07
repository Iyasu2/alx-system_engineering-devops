#!/usr/bin/python3
'''
this module imports
the all hot articles
in a subreddit
'''
import requests


def recurse(subreddit, hot_list=[]):
    '''
    function to get hot articles recursively
    '''
    headers = {'User-Agent': '0x16-api_advanced'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']

        if after is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
