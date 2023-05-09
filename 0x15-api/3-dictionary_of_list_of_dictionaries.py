#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

url = "https://jsonplaceholder.typicode.com/users/"

payload = {}
users = requests.get(url).json()
for user in users:
    user_id = user["id"]
    username = user["username"]
    todos = requests.get(url + "{}/todos".format(user_id)).json()
    payload[user_id] = [
        {"task": task["title"], "completed": task["completed"], "username": username}
        for task in todos
    ]

with open("todo_all_employees.json", "w") as f:
    json.dump(payload, f)
