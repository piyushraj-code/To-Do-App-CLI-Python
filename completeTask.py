import json
from utils import returnToHome
def completeTask(task_to_complete):
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found.")
        return
    for task in data["tasks"]:
        if task["task"] == task_to_complete:
            task["status"] = True
            with open("tasks.json", "w") as file:
                json.dump(data, file, indent=4)
                print(task_to_complete, " Mark as complete")

    returnToHome()