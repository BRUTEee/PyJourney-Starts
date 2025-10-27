tasks = []

def show_menu():
    print("\n To-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        new_task = input("Enter new task: ")
        tasks[task_num - 1] = new_task
        print("Task updated successfully!")
    except (IndexError, ValueError):
        print("Invalid input!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_num - 1)
        print(f"Deleted: {deleted}")
    except (IndexError, ValueError):
        print("Invalid input!")

while True:
    show_menu()
    choice = input("Choose option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting To-Do App... Bye!")
        break
    else:
        print("Invalid choice! Try again.")
