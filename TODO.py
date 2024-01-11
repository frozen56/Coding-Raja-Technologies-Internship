from datetime import datetime


class Task:

  def __init__(self, description, priority, due_date=None, completed=False):
    self.description = description
    self.priority = priority 
    self.completed = completed
    self.due_date = due_date


class TodoList:

  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)

  def remove_task(self, index):
    if 0 <= index < len(self.tasks):
      del self.tasks[index]
    else:
      print("Invalid task index.")

  def complete_task(self, index):
    if 0 <= index < len(self.tasks):
      self.tasks[index].completed = True
    else:
      print("Invalid task index.")

  def display_tasks(self):
    if not self.tasks:
      print("No tasks.")
    else:
      for i, task in enumerate(self.tasks):
        status = "Completed" if task.completed else "Pending"
        due_date = task.due_date.strftime(
            "%d-%m-%Y") if task.due_date else "Not set"
        print(
            f"{i + 1}. [{status}] {task.description} (Priority: {task.priority},Due:{due_date})"
        )

  def save_tasks_to_file(self, filename):
    with open(filename, "w") as file:
      for task in self.tasks:
        completed = "\ndone" if task.completed else "\nnot done"
        due_date = task.due_date.strftime("%d-%m-%Y") if task.due_date else ""
        file.write(
            f"{task.description},{task.priority},{due_date},{completed}\n")

  def load_tasks_from_file(self, filename):
    try:
      with open(filename, "r") as file:
        for line in file:
          description, priority, due_date_str, completed = line.strip().split(
              ",")
          due_date = datetime.strptime(due_date_str,
                                       "%d-%m-%Y") if due_date_str else None
          completed = completed == "1"
          task = Task(description, priority, due_date, completed)
          self.add_task(task)
    except FileNotFoundError:
      print("No tasks file found. Starting with an empty list.")


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
      description = input("Enter task description: ")
      priority = input("Enter priority (high/medium/low): ")
      due_date_str = input(
          "Enter due date (DD-MM-YYYY), leave empty if not set: ")
      due_date = datetime.strptime(due_date_str,
                                   "%d-%m-%Y") if due_date_str else None
      task = Task(description, priority, due_date)
      todo_list.add_task(task)
      print("Task added.")

    elif choice == "2":
      index = int(input("Enter task index to remove: ")) - 1
      todo_list.remove_task(index)

    elif choice == "3":
      index = int(input("Enter task index to mark as completed: ")) - 1
      todo_list.complete_task(index)

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
