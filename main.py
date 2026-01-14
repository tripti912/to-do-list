# To do list application

while True:

    print("===== TO-Do List Menu =====\n"
        "1:- Add Task\n"
        "2:- View Tasks\n"
        "3:- Mark Tasks as Completed\n"
        "4:- Delete Task\n"
        "5:- Exit\n")
    
    choice = int(input("Enter your choice:-"))

    if choice == 1:
        task = input("Enter your task:-")
        with open("todo.txt","a")as file:
            file.write(f"{task} , Pending")
        print("Task added successfully!\n")

    elif choice == 2:
        with open("todo.txt","r")as read:
            tasks = read.readlines()
            print("Your Tasks:")
            for i, task in enumerate(tasks,start=1):
                print(f"{i}. {task.strip()}")

    elif choice == 3:
        task_no = int(input("Enter task number to mark as completed:"))

        with open("todo.txt","w")as file:
            tasks = file.writelines(tasks)
        print("Task marked as completed!")

    elif choice == 4:
        with open("todo.txt","r")as file:
            tasks = file.readlines()
        task_no = int(input("Enter task no to delete:-"))
        tasks.pop(task_no - 1)
        with open("todo.txt","w")as file:
            file.writelines(tasks)
        print("Task deleted successfully!")

    elif choice == 5:
        print("Thank you for using to-do application!")
        break

    else:
        print("Invalid choice! Please try again.")

        





