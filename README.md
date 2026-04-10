# JsonShell-CLI

A simple command-line task manager built in Python using JSON for storage.

> This is my first GitHub project 🚀

---

## Features

- Add tasks
- Mark tasks as done
- Delete tasks
- View all tasks
- Save tasks to a file
- Load tasks from a file

---

##  Demo (CLI Preview)

```
╭─user@host
╰─$ show -l

[1]: Buy milk [-]
[2]: Finish homework [+]
```

---

##  Usage

Clone the program

```bash
git clone https://github.com/Nizu-Rainee/JsonShell-CLI/edit/main/README.md
```

Run the program:

```bash
python jsonshell.py
```

Then type:

```bash
help or -h
```

to see all available commands.

---

## Commands

### File Management
- `save -l` → Save tasks
- `load -l` → Load tasks
- `remove -l` → Delete a file

### Task Management
- `show -l` → Show all tasks
- `done -l` → Mark task as done
- `delete -l` → Delete a task

### System
- `clear` → Clear screen
- `help` or `-h` → Show help menu
- `exit -l` → Exit program

---

## How it works

Tasks are stored in a JSON format like this:

```json
{
  "1": {
    "task": "Buy milk",
    "done": false
  }
}
```

---

## 🔍 Task Status

Each task shows a status indicator:

- `[+]` → Task is completed
- `[-]` → Task is not completed (pending)

### Example

```
[1]: Buy milk [-]
[2]: Finish homework [+]
```

---

## Version

v0.1.0 (4/10/2026)

---

## Programmed by:

Nizu-Rainee

---

## License

MIT License
