import json
from utils import returnToHome

def viewAllTask():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found.")
        return
    print(data["tasks"])
    returnToHome()

