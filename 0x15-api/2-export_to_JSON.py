import sys
import json
import requests

url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

user = requests.get(url).json()
todos = requests.get(url + "/todos").json()

user_id = user["id"]
username = user["username"]

payload = {
    user_id: [
        {"task": task["title"], "completed": task["completed"], "username": username}
        for task in todos
    ]
}
import pprint

pprint.pprint(payload)

with open("{}.json".format(user_id), "w") as f:
    json.dump(payload, f)
