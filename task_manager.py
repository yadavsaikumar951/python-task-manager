import json
import os


class TaskManager:
    """
    TaskManager handles CRUD operations for tasks
    stored in a JSON file.
    """

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:
            return json.load(file)

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        """Add a new task"""
        if not title.strip():
            raise ValueError("Task title cannot be empty")

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "completed": False
        }

        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        """Return all tasks"""
        return self.tasks

    def update_task(self, task_id, new_title):
        """Update an existing task"""
        for task in self.tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                self.save_tasks()
                return

        raise ValueError("Task not found")

    def delete_task(self, task_id):
        """Delete a task"""
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return

        raise ValueError("Task not found")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                title = input("Enter task title: ")
                manager.add_task(title)
                print("Task added successfully!")

            elif choice == "2":
                tasks = manager.list_tasks()
                if not tasks:
                    print("No tasks available.")
                for task in tasks:
                    status = "Done" if task["completed"] else "Pending"
                    print(f'{task["id"]}. {task["title"]} - {status}')

            elif choice == "3":
                task_id = int(input("Enter task ID: "))
                new_title = input("Enter new task title: ")
                manager.update_task(task_id, new_title)
                print("Task updated successfully!")

            elif choice == "4":
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)
                print("Task deleted successfully!")

            elif choice == "5":
                print("Exiting Task Manager.")
                break

            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
