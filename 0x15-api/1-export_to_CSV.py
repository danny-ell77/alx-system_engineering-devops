import sys
import csv
import requests

url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

user = requests.get(url).json()
todos = requests.get(url + "/todos").json()

user_id = user["id"]
username = user["username"]

with open("{}.csv".format(user_id), "w") as f:
    writer = csv.writer(f)
    for task in todos:
        writer.writerow([user_id, username, task["completed"], task["title"]])
