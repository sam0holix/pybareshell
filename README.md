# 🐚 pybareshell

`pybareshell` is a minimalist, educational shell implemented in Python. It supports basic built-in commands, executes external programs.

This project is built from scratch with a focus on learning how shells work — from command parsing and execution to simulating a basic interactive prompt.

---

## ✨ Features

- ✅ Interactive shell prompt (`$`)
- ✅ Built-in commands:
  - `echo`
  - `pwd`
  - `cd`
  - `exit`
  - `type`
  - `listcommands`
- ✅ External command execution (e.g. `ls`, `python`, `cat`)
- ✅ Custom error handling (e.g. unknown command)
- ✅ Registry-based command pattern (easy to add new commands)
- 🧪 Keyboard interrupt handling (`Ctrl+C`)
- 🧰 Extensible via abstract `Command` base class

---

## 🛠 Built-in Commands

| Command      | Description                          |
|--------------|--------------------------------------|
| `echo`       | Print arguments to the terminal      |
| `pwd`        | Show current working directory       |
| `cd`         | Change directory                     |
| `exit [n]`   | Exit the shell with optional code    |
| `type name`  | Show if command is builtin or external |
| `listcommands` | List available built-in commands   |

---

## 🚀 Getting Started

### Requirements

- Python 3.10+

### Run the Shell

```bash
python pybareshell.py
