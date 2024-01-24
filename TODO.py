from datetime import datetime


class Task:
    def __init__(self, description, priority, due_date=None):
        self.description = description
        self.priority = priority
        self.completed = False
        self.due_date = due_date

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        try:
            del self.tasks[index]
            print("Task removed.")
        except IndexError:
            print("Invalid task index. Task not removed.")

    def complete_task(self, index):
        try:
            self.tasks[index].completed = True
            print("Task marked as completed.")
        except IndexError:
            print("Invalid task index. Task not marked as completed.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "Not set"
                print(f"{i + 1}. [{status}] {task.description} (Priority: {task.priority}, Due: {due_date})")

    def save_tasks_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for task in self.tasks:
                    file.write(f"{task.description},{task.priority},{task.due_date},{task.completed}\n")
            print("Tasks saved to file.")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    description, priority, due_date_str, completed = line.strip().split(",")
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
                    task = Task(description, priority, due_date)
                    task.completed = True if completed.lower() == "true" else False
                    self.add_task(task)
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No tasks file found. Starting with an empty list.")
        except Exception as e:
            print(f"Error loading tasks from file: {e}")


def main():
    filename = "tasks.txt"  # File to store tasks

    todo_list = TodoList()
    todo_list.load_tasks_from_file(filename)

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Save and Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            try:
                description = input("Enter task description: ")
                priority = input("Enter priority (high/medium/low): ")
                due_date_str = input("Enter due date (YYYY-MM-DD), leave empty if not set: ")
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
                task = Task(description, priority, due_date)
                todo_list.add_task(task)
                print("Task added.")
            except ValueError as e:
                print(f"Error adding task: {e}")

        elif choice == "2":
            try:
                index = int(input("Enter task index to remove: ")) - 1
                todo_list.remove_task(index)
            except ValueError:
                print("Invalid input for task index. Please enter a number.")

        elif choice == "3":
            try:
                index = int(input("Enter task index to mark as completed: ")) - 1
                todo_list.complete_task(index)
            except ValueError:
                print("Invalid input for task index. Please enter a number.")

        elif choice == "4":
            print("\nTasks:")
            todo_list.display_tasks()

        elif choice == "5":
            print("Saving and Exiting...")
            todo_list.save_tasks_to_file(filename)
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
