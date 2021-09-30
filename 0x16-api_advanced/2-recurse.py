#!/usr/bin/python3
'''
    Write a recursive function that queries the
    Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
'''


import requests


def recurse(subreddit, hot_list=[]):

    url = 'https://www.reddit.com/r/' + subreddit + '/hot/.json'
    headers = {'user-agent': 'my-app/0.0.1'}

    parameters = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=parameters)

    if response.status_code == 200:
        results = response.json().get('data')
        after = results.get('after')
        count += results.get('dist')

        for line in results.get('children'):
            hot_list.append(line.get('data').get('title'))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list

    else:
        return None
