# EiStudy_ToDoList

This Python script implements a basic to-do list manager with a command-line interface. Users can perform actions such as adding tasks, marking them as completed, deleting tasks, and viewing tasks with optional filters. The program runs continuously until the user chooses to exit.

Class Definition (ToDoList):

_init_ method initializes task lists (tasks and task_status).
add_task method adds tasks with due dates.
is_empty method checks if the to-do list is empty.
mark_as_completed method marks a task as completed.
delete_task method removes a task.
view_tasks method displays tasks with optional filtering.
Main Function (main):

Creates an instance of ToDoList.
Displays a menu with options to add, complete, delete, or view tasks.
Handles user input and calls corresponding methods.
Corrects a typo (_init_ to __init__) and updates __name__ in the conditional statement.
Instructions:

Run the script.
Choose options to interact with the to-do list.
Follow on-screen prompts for adding, completing, deleting, or viewing tasks.
Exit the program when done.
Note:

Ensure correct input for due dates.
Fix the _init_ typo by replacing it with __init__ in the ToDoList class.
Replace _name_ with __name__ in the last conditional statement for proper script execution.
This script serves as a straightforward tool for managing personal tasks efficiently via the command line.
