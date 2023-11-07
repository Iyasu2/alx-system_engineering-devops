#!/usr/bin/python3
'''
this module imports
the 10 hot things
in a subreddit
'''
import requests


def top_ten(subreddit):
    '''
    function to get hot
    '''
    headers = {'User-Agent': 'subs'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
