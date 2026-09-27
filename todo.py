tasks = []

while True :
    print("Welcome to your To-Do List")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Exit")


    choice = input("Enter your choice: ")
    if choice == "1":
     task_name = input("Enter the task you want to add :")
     tasks.append(task_name)
     print ("Task Added")


    elif choice == "2":
      print("Your Tasks:")
      for task in tasks:
        print(task) 




    elif choice == "3":
      task_name = input("Enter the task you want to Remove :")
      tasks.remove(task_name)
      print("Task Removed")
      


    elif choice == "4": 
     print("Good Bye")
     break


