#imports
import json
import os
import socket
import getpass

#tinkering-----------------------------------

os.system("cls" if os.name == "nt" else "clear")

person = getpass.getuser()
host = socket.gethostname()

#interace
interface = r"""
      _                 ____  _          _ _ 
     | |___  ___  _ __ / ___|| |__   ___| | |
  _  | / __|/ _ \| '_ \\___ \| '_ \ / _ \ | |
 | |_| \__ \ (_) | | | |___) | | | |  __/ | |
  \___/|___/\___/|_| |_|____/|_| |_|\___|_|_|
  
  JsonShell CLI
  
  version: v0.1.0
  Programmed by: Nizu-Rainee
  CRUD (Create, Read, Update, Delete) Application
  JSON-based storage
  
  Type 'help' or '-h' to view commands.                              
"""

help_menu = f"""
Available Commands:

 File Management:
  save -l        → Save current tasks to a JSON file
  load -l        → Load tasks from a JSON file
  remove -l      → Delete a saved JSON file

 Task Management:
  show -l        → Display all tasks
  done -l        → Mark a task as completed (requires ID)
  delete -l      → Delete a specific task (requires ID)

 System:
  clear          → Clear the screen
  help / -h      → Show this menu
  exit        → Exit the program

User: {person}
Host: {host}

Notes:
 • This program saves files into a JSON file:
 
 • When using save/load/remove:
   → Only type the file name (no ".json")

 • Example:
   save -l → mytasks
   load -l → mytasks

 • Task IDs are shown in [brackets]
"""

#welcome
print(interface)

#list
to_do = {}
task_id = 1

#CLI-------------------------------------------------------

while True:
    print()
    user = input(f"╭─{person}@{host} ~\n╰─$ ").lower()

    #exiting
    if user == "exit":
        print("Exiting...")
        os.system("cls" if os.name == "nt" else "clear")
        break

    #user saving/creating
    if user == "save -l":
        name = input("Enter a name for your file: ")
        with open(f"{name}.json", "w") as file:
            json.dump(to_do, file, indent=4)
    #user loading
    elif user == "load -l":
        name = input("Enter a name you want to load: ")

        try:
            with open(f"{name}.json", "r") as file:
                to_do = json.load(file)

            # overwrite
            if to_do:
                task_id = max(map(int, to_do.keys())) + 1

                for key, value in to_do.items():
                    status = "[+]" if value["done"] else "[-]"
                    print(f"[{key}]: {value} {status}")
            else:
                task_id = 1
                print("No tasks found.")

            print("Data loaded!!!")

        except FileNotFoundError:
            print(f"File {name} not found")
    #user removing
    elif user == "remove -l":
        name = input("Enter a name you want to delete: ")

        try:
            os.remove(f"{name}.json")

        except FileNotFoundError:
            print(f"File {name} not found")
    #view
    elif user == "show -l":
        if not to_do:
            print("No task yet")
        else:
            for key in sorted(to_do, key=int):
                value = to_do[key]

                task_text = value.get("task") or value.get("task_id") or "UNKNOWN"
                status = "[+]" if value.get("done") else "[-]"

                print(f"[{key}]: {task_text} {status}")
    #done
    elif user == "done -l":
        task_num = input("Enter a task ID: ")

        if task_num in to_do:
            to_do[task_num]["done"] = True
            print("Task marked as Done.")
        else:
            print("Task not found.")
    #deleting items
    elif user == "delete -l":
        task_num = input("Enter a task ID to delete: ")

        if task_num in to_do:
            del to_do[task_num]
            print("Task deleted.")
        else:
            print("Task not found.")
    #stuff
    elif user == "help":
        print(help_menu)
    elif user == "-h":
        print(help_menu)
    elif user == "clear":
        os.system("cls" if os.name == "nt" else "clear")
    #adding
    else:
        to_do[str(task_id)] = {
            "task": user,
            "done": False
        }
        task_id += 1