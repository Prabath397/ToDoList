# Simple To-Do List App (Version 2)
# Features: Add, View, Delete tasks

# empty list to store tasks
tasks = []

while True:
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added ✅")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Task '{removed}' deleted ✅")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
