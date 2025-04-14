tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})  # Fixed key
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")  # Fixed key

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True  # Fixed key
            print("Task marked as complete!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Task '{removed_task['task']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']},{task['completed']}\n")  # Removed extra space

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(",")
                tasks.append({"task": task_data[0], "completed": task_data[1] == "True"})  # Fixed key
    except FileNotFoundError:
        pass

def main():
    load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save & Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_tasks()
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

# Fixed main guard indentation
if __name__ == "__main__":
    main()