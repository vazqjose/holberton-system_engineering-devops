#!/usr/bin/python3
'''
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    for a given subreddit.
'''


import requests


def top_ten(subreddit):

    url = 'https://www.reddit.com/r/' + subreddit + '/top.json?limit=10'
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        count = 10
        for post in response.json().get('data').get('children'):
            line = post.get('data').get('title')
            print(line)
            count = count - 1
            if count == 0:
                break

    else:
        print('None')
