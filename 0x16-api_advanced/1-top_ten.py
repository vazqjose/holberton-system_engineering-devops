#!/usr/bin/python3
'''
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    for a given subreddit.
'''


import requests


def top_ten(subreddit):

    url = 'https://www.reddit.com/r/{}/.json?limit=10'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        response = response.json().get('data').get('children')
        for post in response:
            line = post.get('data').get('title')
            print(line)

    else:
        print('None')
