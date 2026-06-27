tasks = []

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

    elif choice == '2':
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == '3':
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            index = int(input("Enter task number to mark completed: ")) - 1

            if 0 <= index < len(tasks):
                tasks[index] += " ✓ Completed"
                print("Task updated successfully.")
            else:
                print("Invalid task number.")

    elif choice == '4':
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

            index = int(input("Enter task number to delete: ")) - 1

            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"'{removed}' deleted successfully.")
            else:
                print("Invalid task number.")

    elif choice == '5':
        print("Exiting To-Do List Manager...")
        break

    else:
        print("Invalid choice. Please try again.")
