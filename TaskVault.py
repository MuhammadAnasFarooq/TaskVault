tasks = []

while True:
    print(" \n1 - Add a task")
    print(" 2 - View all tasks")
    print(" 3 - Delete a task")
    print(" 4 - Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour tasks: ")
        for i in range(len(tasks)):
            print(i + 1, tasks[i])

    elif choice == "3":
        number = int(input("Enter number of task you want to delete: "))
        tasks.pop(number - 1)
        print("Task deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
