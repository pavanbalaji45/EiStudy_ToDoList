class ToDoList:
    def __init__(self):
        self.task_status = []  # storing status of all tasks
        self.tasks = []  # list of all tasks stored in a list

    def add_task(self, title, due_date):
        self.tasks.append(title + " - Due: " + due_date)
        self.task_status.append(False)  # As initially, tasks are not completed

    def is_empty(self):
        return not self.tasks

    def mark_as_completed(self, title):
        for i in range(len(self.tasks)):
            if title in self.tasks[i]:
                self.task_status[i] = True
                return True
        return False

    def delete_task(self, title):
        indices_to_remove = [i for i, task in enumerate(self.tasks) if title in task]
        for index in reversed(indices_to_remove):
            self.tasks.pop(index)
            self.task_status.pop(index)

    def view_tasks(self, filter_type=1):
        print("\n\nList of Tasks:\n\n")
        for i in range(len(self.tasks)):
            if filter_type == 1 or (filter_type == 2 and self.task_status[i]) or (filter_type == 3 and not self.task_status[i]):
                print(f"{i+1}\t{self.tasks[i]} - {'Completed' if self.task_status[i] else 'Pending'}\n\n")


def main():
    todo_list = ToDoList()
    while True:
        print("\t\t\t--------------************--------------")
        print("\n\n\t\t\t    Personal To-Do List Manager\n")
        print("\t\t\t--------------************--------------\n")
        print("\t1.   Add a Task\n"
              "\t2.   Mark task Completed\n"
              "\t3.   Delete a Task\n"
              "\t4.   View all Tasks\n"
              "\t5.   Exit\n")
        choice = input("\n\t\tEnter a command: ")

        if choice == '1':
            title = input("\nEnter the Task Title:\t")
            due_date = input("Enter due date: ")
            todo_list.add_task(title, due_date)

        elif choice == '2':
            if todo_list.is_empty():
                print("\nList is empty")
            else:
                title = input("\nEnter Task Title to mark as Completed:\t")
                if todo_list.mark_as_completed(title):
                    print("\nTask completed successfully!")
                else:
                    print("\nTask deleted")
            input("\nPlease Enter to continue to the main menu...")

        elif choice == '3':
            if todo_list.is_empty():
                print("\nList is empty.")
            else:
                title = input("\nEnter Task Title to Delete:\t")
                if todo_list.delete_task(title):
                    print("\nTask deleted successfully!")
                else:
                    print("\nTask not found")
            input("\nPlease Enter to continue to the main menu...")

        elif choice == '4':
            if not todo_list.is_empty():
                print("\nFilter Options: ")
                print("\n1. All filters\n2. Completed\n3. Pending")
                filter_type = input("\nEnter Filter (1/2/3):\t")
                todo_list.view_tasks(int(filter_type))
            else:
                print("\n\tList is empty.")
            input("\nPlease Enter to continue to the main menu...")

        elif choice == '5':
            exit()

        else:
            print("\nInvalid Command.\nTry again.\n")
            input("Press Enter to continue...")
        print("\n" + "-" * 30)


if __name__ == "__main__":
    main()
