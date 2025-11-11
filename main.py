import argparse
from datetime import datetime
import json

"""
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. 

The user should be able to:
    Add, Update, and Delete tasks
    Mark a task as in progress or done
    List all tasks
    List all tasks that are done
    List all tasks that are not done
    List all tasks that are in progress

Here are some constraints to guide the implementation:
    You can use any programming language to build this project.
    Use positional arguments in command line to accept user inputs.
    Use a JSON file to store the tasks in the current directory.
    The JSON file should be created if it does not exist.
    Use the native file system module of your programming language to interact with the JSON file.
    Do not use any external libraries or frameworks to build this project.
    Ensure to handle errors and edge cases gracefully.

Task Properties:
    Each task should have the following properties:
        id: A unique identifier for the task
        description: A short description of the task
        status: The status of the task (todo, in-progress, done)
        createdAt: The date and time when the task was created
        updatedAt: The date and time when the task was last updated

    Make sure to add these properties to the JSON file when adding a new task and update them when updating a task.


"""
class Task:
    def __init__(self, id=-1, description="N/A", status="N/A", createdAt="N/A", updatedAt="N/A"):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def __repr__(self):
        return f"Task(id={self.id}, description={self.description}, status={self.status}, createdAt={self.createdAt}, updatedAt={self.updatedAt})"
    
    def __str__(self):
        return f"id: {self.id} | description: {self.description} | status: {self.status} | createdAt: {self.createdAt} | updatedAt: {self.updatedAt}"

def add_task(id, descrption):
    status = "todo"
    raw_date_time = datetime.now()
    clean_date_time = raw_date_time.strftime("%d/%m/%Y, %I:%M %p")
    createdAt = clean_date_time
    updatedAt = "Has not been updated yet"
    new_task = Task(id, descrption, status, createdAt, updatedAt)
    
    return new_task

def update_task(new_description, selected_task):
    raw_date_time = datetime.now()
    clean_date_time = raw_date_time.strftime("%d/%m/%Y, %I:%M %p")
    selected_task.update({"description": new_description})
    selected_task.update({"updatedAt": clean_date_time})

    return None

def delete_task(task_data, id):
    task_data.pop(args.attribute1)

    return None

if __name__ == "__main__":
    task_data = {} # initalize task_data at the start

    try: # checks if data.json exists
        with open("data.json", "r") as file:
            task_data = json.load(file) # currently loads back id as a string. NEED TO REMEMBER THAT!
    except FileNotFoundError: # if it does not exist, that means it is the first time so we need to create the file.
        with open("data.json", "w") as file:
            json.dump(task_data, file, indent=2)
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as file:
            json.dump(task_data, file, indent=2)

    if not bool(task_data): # if dict is empty
        id_counter = 1
    else: # check the dictionary for the biggest key, since that key will be the max id in that moment
        id_counter = len(task_data) + 1

    parser = argparse.ArgumentParser(prog="task-cli")

    parser.add_argument("command")
    parser.add_argument("attribute1", nargs="?") #? makes it a opitional positional argument
    parser.add_argument("attribute2", nargs="?") #? makes it a opitional positional argument

    args = parser.parse_args()
    
    match args.command:
        case "add":
            added_task = add_task(id_counter, args.attribute1) #should take id and the optional positional command
            task_data.update(  {added_task.id : 
                               {"description": added_task.description,
                                "status": added_task.status, 
                                "createdAt": added_task.createdAt, 
                                "updatedAt": added_task.updatedAt}})
        case "update": #should be done update id_number "new_description"
            if args.attribute1 not in task_data.keys():
                print(f"Task ID {args.attribute1} does not exist, meaning the task does not exist and can not be updated.")
            else:
                update_task(args.attribute2, task_data.get(args.attribute1))
        case "delete":
            try:
                delete_task(task_data, args.attribute1)
            except KeyError:
                print(f"Task ID {args.attribute1} does not exist, meaning the task does not exist.")
        case _:
            print("Command not found")

    with open("data.json", "w") as file:
        json.dump(task_data, file, indent=2)