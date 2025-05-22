#!/usr/bin/python3
import sys
import time
import os

# Global variables
START = 0
END = 12
FILE_PATH = 'todos_list.txt'

def load_the_file():
    """Load tasks from a file and appends a list

    Returns:
        task_list: list
    """
    task_list = []

    # Load tasks from a file
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file: 
            for line in file:
                task_list.append(line.strip())
    return task_list

def save_todos(todo_list):
    tasks = todo_list
            



def add_todo(todo_list):
    """Allows user to add todos interactively."""
    while True:
        clear_screen()
        print("+----------------------------------------------------+")
        if todo_list:
            for idx, task in enumerate(todo_list, start=1):
                print(f"|   {idx}. {task}")
        else:
            print("|   No todos yet.                                    |")
        print("+----------------------------------------------------+")

        user_todo = input("Enter todo (or Q to quit): ").strip().title()
        if user_todo == 'Q':
            clear_screen()
            pause_and_return()
            display_options()
            break  # Exit loop
        else:
            todo_list.append(user_todo)


def remove_todo(todo_list):
    """function to delete tasks from task list

    Args:
        todo_list (list): hold user todos
    """
    clear_screen()
    for idx, task in enumerate(todo_list, start=1):
        print("+----------------------------------------------------+")
        if todo_list:
            print(f"|      {idx}. {task}")
        else:
            print("|   No todos yet.                                    |")
        print("+----------------------------------------------------+")

def view_todos(todo_list):
    pass

def mark_todo_complete(todo_list):
    pass


def exit():
    clear_screen()
    print("Exting the application.....")
    time.sleep(1)
    sys.exit()

def pause_and_return():
    """Pause and wait for the user to press return key
    """
    input("\nPress Enter to return to main Menu...")
    clear_screen()


def clear_screen():
    """Uses ASII character codes to clear the screen
    """
    sys.stdout.write("\033[H\033[J")
    sys.stdout.flush()


def user_selection():
    """Prompt user for choice input
    """
    todo_list = load_the_file()

    try:
        user_choice = int(input(f"{"-----Select option: ":>30}"))
    except:
        print(f"{"Invalid Input!!":^40}")
        time.sleep(1)
        clear_screen()
        display_options()
    finally:
        if user_choice == 1:
            print(add_todo(todo_list))
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            view_todos(todo_list)
        elif user_choice == 4:
            mark_todo_complete(todo_list)
        elif user_choice == 5:
            remove_todo(todo_list)
        else:
            exit()

    



def display_options():
    for i in range(END + 1):
        if i == START or i == END:
            print("+----------------------------------------------------+")
        elif i == 3:
            print("|            WELCOME TO TODO MANAGER                 |")
        elif i == 5:
            print("|        1. ➕ ADD New todos                         |")
        elif i == 6:
            print("|        2. 📝 EDIT a todo                           |")
        elif i == 7:
            print("|        3. 📖 VIEW existing todos                   |")
        elif i == 8:
            print("|        4. ✔  Mark a todo COMPLETE                  |")
        elif i == 9:
            print("|        5. ❌ DELETE task                           |")
        elif i == 10:
            print("|        6. 💾 Save and Quit                         |")
        else:
            print("|                                                    |")
    user_selection()


def main():
    display_options()


if __name__ == "__main__":
    main()
