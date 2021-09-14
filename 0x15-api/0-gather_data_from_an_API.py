#!/usr/bin/python3
'''
    Write a Python script that, for a given employee ID
    returns information about his/her TODO list progress.
'''

if __name__ == "__main__":

    import requests
    import sys
    employeeID = sys.argv[1]

    myData = requests.get('https://jsonplaceholder.typicode.com/users/' +
                          employeeID)
    myData = myData.json()

    myTasks = requests.get(
              'https://jsonplaceholder.typicode.com/todos?userId=' +
              employeeID)
    myTasks = myTasks.json()

    tasksDone = 0
    doneList = []

    for n in myTasks:
        if n['completed']:
            tasksDone += 1
            doneList.append(n['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(myData['name'], tasksDone, len(myTasks)))

    for i in range(len(doneList)):
        print('\t {}'.format(doneList[i]))
