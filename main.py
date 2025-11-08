import argparse
import sys
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
    """
    Initialize values and add functions as needed.
    
    * ADD FUNCTION (either will be in the class or outside function)
        * When a Task object is first created, it needs to be stored in a container so later, we can look at the size of the container, 
          to know what id we are on.
        * Id tracking can work many different ways. My first though is, lets use a to store the ids as keys and the task object data as the value. 
        * Issues that need to be handled. If task 2 is deleted, should the user be able to make a new task 2? Id say no, because no function 
        lets them add a task with a specific id, just update specific ids. 
        * Other idea if dictionary does not work, we can store the id numbers in a container, check the max values of container and add 
          that + 1 to the id.
        * When add is called, a task should be created. The id should increment by 1, the descrption should take the string of add, 
          the status should default to not started, createdAt needs to be grabbed from the computer, and updatedAt defaults to None since is was just created
    """
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
        id_counter = int(max(task_data.keys())) + 1
        print(id_counter)

    parser = argparse.ArgumentParser()

    parser.add_argument("command")
    parser.add_argument("attribute", nargs="?") #? makes it a opitional positional argument

    args = parser.parse_args()
    
    match args.command:
        case "add":
            added_task = (add_task(id_counter, args.attribute)) #should take id and the optional positional command
            task_data.update(      {added_task.id : {
                               "description": added_task.description,
                               "status": added_task.status, 
                               "createdAt": added_task.createdAt, 
                               "updatedAt": added_task.updatedAt}} )
        case _:
            print("Command not found")

    with open("data.json", "w") as file:
        json.dump(task_data, file, indent=2)
    
    # UNCOMMENT LATER: args.update[0] = int(args.update[0]) # Converts first argument of update into an int from the list.