#!/usr/bin/python3
'''
    query the Reddit API and returns number of subscribers for
    given subreddit
'''
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    header = 'Mozilla/5.0 (X11; Linux x86_64) ' \
              'AppleWebKit/537.36 (KHTML, like Gecko) ' \
              'Chrome/80.0.3987.87 Safari/537.36'

    response = requests.get(url, allow_redirects=False, headers={'User-Agent': header})

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
