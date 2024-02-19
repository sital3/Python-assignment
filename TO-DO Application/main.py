
tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")

def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Task: ")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task #{index}. {task['task']} - Status: {status}")
def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("enter the # to delete: "))
        if taskToDelete>=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid Input.")

def markTaskCompleted():
    listTask()
    try:
        taskToMark = int(input("Enter the task number to mark as completed: "))
        if 0 <= taskToMark < len(tasks):
            tasks[taskToMark]["completed"] = True
            print(f"Task {taskToMark} marked as completed.")
        else:
            print(f"Task #{taskToMark} was not found.")
    except ValueError:
        print("Invalid Input.")

if __name__ =="__main__":
# creating a loop to run the app
    print("Welcome the the TO-DO List App")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("---------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List of tasks")
        print("4. Mark a task as completed")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if (choice=="1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTask()
        elif (choice == "4"):
            markTaskCompleted()
        elif(choice == "5"):
            break
        else:
            print ("Invalid input. Please try again")

    print("Have a great day!!!")

