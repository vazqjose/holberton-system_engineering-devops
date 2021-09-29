#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    header = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(url, headers=header)

    if response.status_code == '404':
        return (0)
    else:
        print(response)
        return (1)
