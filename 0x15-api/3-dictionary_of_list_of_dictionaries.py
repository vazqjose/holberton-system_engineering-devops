#!/usr/bin/python3
'''
    Using what you did in the task #0, extend your Python
    script to export data in the CSV format.
'''

if __name__ == "__main__":

    import requests
    import csv
    import json

    url = 'https://jsonplaceholder.typicode.com/todos?userId='
    todoList = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        todos = requests.get(url + "{}".format(user_id)).json()

        tasks = []
        for i in todos:
            task = {"username": username, "task": i.get("title"),
                    "completed": i.get("completed")}
            tasks.append(task)

        todoList[user_id] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(todoList, f)
