import argparse
from datetime import datetime
import json

class Task:
    def __init__(self, new_id=-1, new_description="N/A"):
        self.id = new_id
        self.description = new_description
        self.status = "todo"
        raw_date_time = datetime.now()
        clean_date_time = raw_date_time.strftime("%d/%m/%Y, %I:%M %p")
        self.created_at = clean_date_time
        self.updated_at = "N/A"

    def __repr__(self):
        return f"Task(id={self.id}, description={self.description}, status={self.status}, createdAt={self.created_at}, updatedAt={self.updated_at})"
    
    def __str__(self):
        return f"id: {self.id} | description: {self.description} | status: {self.status} | createdAt: {self.created_at} | updatedAt: {self.updated_at}"

    def update_task(self, new_description):
        raw_date_time = datetime.now()
        clean_date_time = raw_date_time.strftime("%d/%m/%Y, %I:%M %p")
        self.description = new_description
        self.updated_at = clean_date_time


def delete_task(task_data, id):
    task_data.pop(id)
    return None

if __name__ == "__main__":
    # initialize task_data at the start
    task_data = {}

    # checks if data.json exists
    try:
        with open("data.json", "r") as file:
            # currently loads back id as a int. NEED TO REMEMBER THAT!
            task_data = json.load(file)
            task_data = {int(k): Task(k, v["description"]) for k, v in task_data.items()}
    # if it does not exist, that means it is the first time so we need to create the file.
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(task_data, file, indent=2)
    except json.decoder.JSONDecodeError:
        with open("data.json", "w") as file:
            json.dump(task_data, file, indent=2)

    # if dict is empty
    if not bool(task_data):
        id_counter = 1
    # check the dictionary for the biggest key, since that key will be the max id in that moment
    else:
        id_counter = max(task_data) + 1

    parser = argparse.ArgumentParser(prog="task-cli")

    parser.add_argument("command")
    # ? makes it a optional positional argument
    parser.add_argument("attribute1", nargs="?")
    # ? makes it a optional positional argument
    parser.add_argument("attribute2", nargs="?")

    args = parser.parse_args()

    match args.command:
        case "add":
            # should take id and the optional positional command
            #TODO: change how the logic on how dict updates.
            # Should take the id as the key but should place the task object as the value.
            added_task = Task(id_counter, args.attribute1)
            task_data.update({added_task.id :
                               {"description": added_task.description,
                                "status": added_task.status, 
                                "createdAt": added_task.created_at,
                                "updatedAt": added_task.updated_at}})
        # should be done update id_number "new_description"
        case "update":
            user_input_id = int(args.attribute1)

            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task does not exist and can not be updated.")
            else:
                #TODO: change logic from used to be function to class method
                update_task(args.attribute2, task_data.get(user_input_id))
        case "delete":
            user_input_id = int(args.attribute1)
            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task does not exist and can not be deleted.")
            else:
                delete_task(task_data, user_input_id)
        # updaters
        case "mark-in-progress":
            user_input_id = int(args.attribute1)

            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task can not have it status changed.")
            else:
                #TODO: mark-in-progress class method
                pass
        # updaters
        case "mark-done":
            user_input_id = int(args.attribute1)

            if user_input_id not in task_data.keys():
                print(f"Task ID {user_input_id} does not exist, meaning the task can not have it status changed.")
            else:
                # TODO: mark-done class method
                pass
        case "list":
            #command list done
            #command list to-do
            #command list in-progress
            #command list <- meant to list all
            pass
        case _:
            print("Command not found")

    with open("data.json", "w") as file:
        #TODO: task data currently takes a plain text dict. Add to_dict() class method to serialize to task objects.
        # Then change task_data in dump.
        json.dump(task_data, file, indent=2)