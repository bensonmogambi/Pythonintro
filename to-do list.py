#assignment oct 30
#Using Python  Develop terminal  code for Either Todolist,Quiz App , Shopping Cat or
#project of your choice ,in peer group or One Man Army,

# Main To-Do List class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        """Displays all tasks in the list."""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\n--- To-Do List ---")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
            print()

    def add_task(self, task):
        """Adds a task to the to-do list."""
        self.tasks.append(task)
        print(f"'{task}' has been added to your to-do list.")

    def delete_task(self, task_number):
        """Deletes a task from the to-do list by its number."""
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")

    def clear_tasks(self):
        """Clears all tasks from the to-do list."""
        self.tasks.clear()
        print("All tasks have been cleared from your to-do list.")


# Child class for Priority To-Do List
class PriorityToDoList(ToDoList):
    def add_priority_task(self, task, priority):
        """Adds a task with priority to the list."""
        self.tasks.append((task, priority))
        print(f"'{task}' (Priority: {priority}) has been added to your to-do list.")

    def view_tasks(self):
        """Overrides view to show tasks with priorities if they exist."""
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\n--- Priority To-Do List ---")
            for index, task_info in enumerate(self.tasks, start=1):
                if isinstance(task_info, tuple):
                    # task with priority
                    task, priority = task_info
                    print(f"{index}. {task} (Priority: {priority})")
                else:
                    # regular task without priority
                    print(f"{index}. {task_info}")
            print()





# Main program
def main():
    todo_list = PriorityToDoList()

    while True:
        print("\nOptions:")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Add Priority Task")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)
        elif choice == '3':
            task = input("Enter the task you want to add: ")
            priority = input("Enter the priority level (High, Medium, Low): ")
            todo_list.add_priority_task(task, priority)
        elif choice == '4':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number you want to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

