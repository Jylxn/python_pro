import os


class ToDoList:
  TASKS_FILE = 'tasks.txt'

  def __init__(self):
    self.tasks = self.load_tasks()

  def load_tasks(self):
    tasks = {}
    if os.path.exists(self.TASKS_FILE):
      with open(self.TASKS_FILE, 'r') as file:
        for line in file:
          id, task = line.strip().split(',', 1)
          tasks[int(id)] = task
    return tasks

  def save_tasks(self):
    with open(self.TASKS_FILE, 'w') as file:
      for id, task in self.tasks.items():
        file.write(f"{id},{task}\n")

  def add_task(self):
    task = input("Enter the task: ")
    id = max(self.tasks.keys(), default=0) + 1
    self.tasks[id] = task
    self.save_tasks()
    print(f"Task added with ID {id}.")

  def view_tasks(self):
    if not self.tasks:
      print("No tasks found.")
      return
    for id, task in self.tasks.items():
      print(f"{id}: {task}")

  def update_task(self):
    try:
      id = int(input("Enter the task ID to update: "))
      if id in self.tasks:
        new_task = input("Enter the new task: ")
        self.tasks[id] = new_task
        self.save_tasks()
        print(f"Task {id} updated.")
      else:
        print(f"No task found with ID {id}.")
    except ValueError:
      print("Invalid input. Please enter a numeric task ID.")

  def delete_task(self):
    try:
      id = int(input("Enter the task ID to delete: "))
      if id in self.tasks:
        del self.tasks[id]
        self.save_tasks()
        print(f"Task {id} deleted.")
      else:
        print(f"No task found with ID {id}.")
    except ValueError:
      print("Invalid input. Please enter a numeric task ID.")


def main():
  todo_list = ToDoList()
  while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      todo_list.add_task()
    elif choice == '2':
      todo_list.view_tasks()
    elif choice == '3':
      todo_list.update_task()
    elif choice == '4':
      todo_list.delete_task()
    elif choice == '5':
      break
    else:
      print("Invalid choice. Please try again.")

main()