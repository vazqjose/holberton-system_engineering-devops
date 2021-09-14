#!/usr/bin/python3
'''
    Using what you did in the task #0, extend your Python
    script to export data in the CSV format.
'''

if __name__ == "__main__":

    import requests
    import sys
    import csv

    employeeID = sys.argv[1]

    myData = requests.get('https://jsonplaceholder.typicode.com/users/' +
                          employeeID)
    name = myData.json()['username']

    myTasks = requests.get(
              'https://jsonplaceholder.typicode.com/todos?userId=' +
              employeeID)
    myTasks = myTasks.json()

    with open("{}.csv".format(employeeID), 'w') as csvfile:
        for val in myTasks:
            csvfile.write(
                    '"{}","{}","{}","{}"\n'.format(
                        employeeID, name, val['completed'], val['title']))
