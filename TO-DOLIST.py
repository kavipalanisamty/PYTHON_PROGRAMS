import pickle

class Task:
    def __init__(self, name, due_date): 
        self.name = name
        self.due_date = due_date
        self.completed = False
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_due_date(self, new_due_date):
        self.due_date = new_due_date

    def complete(self):
        self.completed = True

tasks = []

menu = {
    1: 'Add new task',
    2: 'View list of tasks',
    3: 'Mark task as completed',
    4: 'Delete task',
    5: 'Save tasks to file',
    6: 'Load tasks from file',
    7: 'Quit'
}

def add_task():
    name = input('ENTER THE TASK NAME: ')
    due_date = input('ENTER THE DUE DATE: ')
    new_task = Task(name, due_date)
    tasks.append(new_task)
    print("Task added successfully!\n")

def view_task():
    if not tasks:
        print("No tasks found.\n")
        return
    print('ALL TASKS:')
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. NAME: {task.name}")
        print(f"   DUE DATE: {task.due_date}")
        print(f"   COMPLETED: {task.completed}\n")

def complete_task():
    view_task()
    index = int(input('ENTER THE TASK NUMBER TO MARK COMPLETED: '))
    if 1 <= index <= len(tasks):
        tasks[index - 1].complete()
        print("Task marked as completed!\n")
    else:
        print("Invalid task number!\n")

def delete_task():
    view_task()
    index = int(input('ENTER THE TASK NUMBER TO DELETE: '))
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        print("Task deleted!\n")
    else:
        print("Invalid task number!\n")

def save_task():
    with open('tasks.dat', 'wb') as file:
        pickle.dump(tasks, file)
    print("Tasks saved successfully!\n")

def load_task():
    global tasks
    try:
        with open('tasks.dat', 'rb') as file:
            tasks = pickle.load(file)
        print("Tasks loaded successfully!\n")
    except FileNotFoundError:
        print("No saved file found!\n")

def display_menu():
    while True:
        print("\nTO-DO LIST MENU")
        for key, value in menu.items():
            print(f"{key} -- {value}")
        
        choice = input("PLEASE ENTER YOUR SELECTION: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_task()
        elif choice == '6':
            load_task()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again!\n")

# Run the program
display_menu()
