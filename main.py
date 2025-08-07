import json
import time
from interface import interface
from utils import returnToHome
from addTask import addTask
from completeTask import completeTask
from viewAllTask import viewAllTask
from viewCompleteTask import viewCompleteTask
from viewIncompleteTask import viewIncompleteTask

def main():
    while(True):
        interface()
        command = int(input("Enter your choice: "))
        if(command == 1):
            task = input("Enter task to add:")
            addTask(task)
            returnToHome()

        elif(command == 2):
            task = input("Enter the task to mark as complete: ")
            completeTask(task)
            returnToHome

        elif(command == 3):
            print("Showing all tasks")
            time.sleep(0.2)
            viewAllTask()
            returnToHome()
        
        elif(command == 4):
            print("Showing incomplete task")
            time.sleep(0.2)
            viewIncompleteTask()
            returnToHome()
        
        elif(command == 5):
            print("Showing completed task")
            time.sleep(0.2)
            viewCompleteTask()
            returnToHome()
        
        elif(command == 6):
            exit

        else:
            print("Enter valid command!")
            returnToHome()
        
        
if __name__ == "__main__":
    main()