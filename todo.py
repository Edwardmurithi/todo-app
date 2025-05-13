"""
TODO:
    Implement function to add  a todo
    Implement function to update the todo list
    Implement function to delete a todo
    Implement function to mark a task as complete
    Integrate the todo app with postgresQL database for task storage
    Integrate a display screen
"""
tasks = []

def add_task(tasks):
    print(f"\n{"ADD TASK":*^20}\n")
    while(True):
        try:
            task = input("task: ")
            if task.lower() == 'q':
                break
            elif task == "":
                print("Enter atleast 4 character todo")
                continue
            tasks.append(task)
        except ValueError as e:
            print(f"Error: {e}")

def display():
    print(f"\n{"WELCOME TO TODO LIST APPLICATION":*^50}\n")
    print(f"{"1. Add todo task.":>20}")
    print(f"{"2. Remove a task.":>20}")
    print(f"{"3. Mark Complete.":>20}")
    print(f"{"4. Edit the List.":>20}")
    print(f"{"5. Save and Exit.":>20}\n");
    
    choice = int(input(f"{"Select Option: ":->20}"))
    if choice == 1:
        add_task(tasks)