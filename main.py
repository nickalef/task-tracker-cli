import argparse
from datetime import datetime
import json

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

    def update_task(self, new_description):
        raw_date_time = datetime.now()
        clean_date_time = raw_date_time.strftime("%d/%m/%Y, %I:%M %p")
        self.description = new_description
        self.updatedAt = clean_date_time


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
    task_data.pop(id)

    return None



if __name__ == "__main__":
    task_data = {} # initalize task_data at the start

    try: # checks if data.json exists
        with open("data.json", "r") as file:
            task_data = json.load(file) # currently loads back id as a int. NEED TO REMEMBER THAT!
            task_data = {int(k): v for k, v in task_data.items()}
    except FileNotFoundError: # if it does not exist, that means it is the first time so we need to create the file.
        with open("data.json", "w") as file:
            json.dump(task_data, file, indent=2)
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as file:
            json.dump(task_data, file, indent=2)

    if not bool(task_data): # if dict is empty
        id_counter = 1
    else: # check the dictionary for the biggest key, since that key will be the max id in that moment
        id_counter = max(task_data) + 1

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
            user_input_id = int(args.attribute1)

            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task does not exist and can not be updated.")
            else:
                update_task(args.attribute2, task_data.get(user_input_id))
        case "delete":
            user_input_id = int(args.attribute1)
            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task does not exist and can not be deleted.")
            else:
                delete_task(task_data, user_input_id)
        case "mark-in-progress": #updaters
            user_input_id = int(args.attribute1)

            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task can not have it status changed.")
            else:
                #TODO: function call
                print("Inside mark-in-progress")
        case "mark-done": #updaters
            print("Inside mark-done")
        case "list":
            print("Inside list")
            #command list done
            #command list todo
            #command list in-progress
            #command list <- meant to list all
        case _:
            print("Command not found")

    with open("data.json", "w") as file:
        json.dump(task_data, file, indent=2)