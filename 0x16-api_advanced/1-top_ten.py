#!/usr/bin/python3
'''
    Function that queries the Reddit API and
    prints the titles of the first 10 hot posts
    for a given subreddit.
'''


import requests


def top_ten(subreddit):

    url = 'https://www.reddit.com/r/' + subreddit + '/top.json?limit=10'
    #headers = {'user-agent': 'my-app/0.0.1'}
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
               Safari/537.36"}
    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:

        for post in response.json().get('data').get('children'):
            line = post.get('data').get('title')
            print(line)

    else:
        print('None')
