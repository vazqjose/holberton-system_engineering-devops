#!/usr/bin/python3
'''
    Using what you did in the task #0, extend your Python
    script to export data in the CSV format.
'''

if __name__ == "__main__":

    import requests
    import sys
    import csv
    import json

    employeeID = sys.argv[1]

    myData = requests.get('https://jsonplaceholder.typicode.com/users/' +
                          employeeID)
    name = myData.json()['username']

    myTasks = requests.get(
              'https://jsonplaceholder.typicode.com/todos?userId=' +
              employeeID)
    myTasks = myTasks.json()

    data = {}
    data[employeeID] = []

    for item in myTasks:
        data[employeeID].append({
            'task': item['title'],
            'completed': item['completed'],
            'username': name
            })
        with open('{}.json'.format(employeeID), 'w') as outfile:
            json.dump(data, outfile)
