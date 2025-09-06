# Simple To-Do List App (Version 1)
# Features: Add and View tasks

# empty list to store tasks
tasks = []

while True:
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Quit")

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
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.")
