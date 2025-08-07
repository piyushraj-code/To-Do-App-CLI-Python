import json
from utils import returnToHome

def viewIncompleteTask():
    
    with open("tasks.json", "r") as file:
        data = json.load(file)
        for task in data["tasks"]:
            if task["status"] == False:
                print(task)
    returnToHome()
