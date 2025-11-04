import argparse

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # how argparse works in terminal
    # python3 main.py commands
    # a positional argument is the default argument when writing the name of the command. It forces you to input for that argument.
    # if you add -- in front of the command, it becomes optional, meaning it does not have to be written. However if you do write it, it needs
    # to be done by doing --command_name input. The terminal will also tell you how to input it if you do the help command. Optional arguments
    # have a changable order, compared to the fixed order of positional as well.
    parser.add_argument("--add", help="Adds a task to the tracker. Takes a string.")
    parser.add_argument("--update", nargs=2, help="Updates a task. Takes the id of the task and a new string")
    # parser.add_argument("delete", help="Deletes a selected task. Takes the id of the task.")
    # parser.add_argument("mark_in_progress", help="Marks a selected task as in progress. Takes the id of the task.")
    # parser.add_argument("mark_done", help="Marks a selected task as done. Takes the id of the task.")
    # parser.add_argument("list_all", help="Lists all the tasks.")
    # parser.add_argument("list_done", help="Lists all the tasks that are done.")
    # parser.add_argument("list_todo", help="Lists all the tasks that are not started.")
    # parser.add_argument("list_in_progress", help="Lists all the tasks that are in progress.")

    args = parser.parse_args()

    print(args.add)

    args.update[0] = int(args.update[0]) # Converts first argument of update into an int from the list.
    print(args.update)