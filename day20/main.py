# Day 20 – Mini Project: To-Do List (Python)

tasks = []
# adding task
def add_task():
    task = input("Enter Your New Tasks: ")
    tasks.append(task)
    print("Task Added Successfully !!")

# view all task
def view_tasks():
    if not tasks:
        print("No tasks available!!")
    else:
        print("Your Tasks: ")
        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)

# Delete Task
def delete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed}' deleted.")
        else:
            print("Invalid task number.")
while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
