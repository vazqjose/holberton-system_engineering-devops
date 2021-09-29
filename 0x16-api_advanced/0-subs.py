#!/usr/bin/python3
'''
    query the Reddit API and returns number of subscribers for
    given subreddit
'''


import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {'user-agent': 'my-app/0.0.1'}

    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return
