#!/usr/bin/python3
'''
    Using what you did in the task #0, extend your Python
    script to export data in the CSV format.
'''

if __name__ == "__main__":

    import requests
    import csv
    import json

    urlString = 'https://jsonplaceholder.typicode.com/todos?userId='
    todoList = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for user in users:
        userID = user['id']
        username = user['username']

        myData = requests.get(urlString + "{}".format(userID)).json()
        tasksList = []

        for item in myData:
            tasksList.append({
                "username": username,
                "task": item['title'],
                "completed": item['completed']
                })
            todoList[userID] = tasksList

    with open('todo_all_employees.json', 'w') as outfile:
        json.dump(todoList, outfile)
