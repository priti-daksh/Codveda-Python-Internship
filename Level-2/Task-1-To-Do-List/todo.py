import json

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter task: ")

    if task_name.strip() == "":
        print("Task cannot be empty!")
        return

    tasks.append({
        "task": task_name,
        "completed": False
    })

    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
        return

    print("\n===== YOUR TASKS =====")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")  

def mark_completed(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to mark as completed: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number!")      

def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)

        print(f"Task '{deleted_task['task']}' deleted successfully!")

    except ValueError:
        print("Please enter a valid number!")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using To-Do List Application!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


main()                            