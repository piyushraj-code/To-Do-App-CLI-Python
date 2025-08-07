import json
from utils import returnToHome
def addTask(task):
    # Read existing json file
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

    except(FileNotFoundError, json.JSONDecodeError):
        data = {"tasks":[]}
    # Create new task
    data["tasks"].append({"task": task, "status": False})

    # Add new task to json file
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Task Added")
    returnToHome()