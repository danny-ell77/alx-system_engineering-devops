import sys
import requests
from pprint import pprint

url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

user = requests.get(url).json()
todos = requests.get(url + "/todos").json()

employee_name = user["name"]
number_of_done_tasks = len([task for task in todos if bool(task["completed"])])
total_number_of_tasks = len(todos)
print(
    "Employee {} is done with tasks({}/{})".format(
        employee_name, number_of_done_tasks, total_number_of_tasks
    )
)

for task in todos:
    print("\t {}".format(task["title"]))
