import json
from utils import returnToHome

def viewCompleteTask():
    
    with open("tasks.json", "r") as file:
        data = json.load(file)
        for task in data["tasks"]:
            if task["status"] == True:
                print(task)
    returnToHome()
