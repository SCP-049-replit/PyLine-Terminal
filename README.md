# PyLine Terminal

![python logo](https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png)


## Table of contents
1. Introduction
2. Linux install
3. How to use
4. PyLine in-depth
5. Future Additions
6. Usage rights

## 1. Introduction

This is a python-made terminal to make doin terminal stuff as simple as possible, it even includes a easy to use command language, and a text editor!

You can do all sorts of stuff with the terminal, manage files and folders, create and edit files, and of course run them! (Works with python, c, and bash)

## 2. Linux Install

Before you start using it, theres a few things you need to install (for full functionality) Below is the linux commands to help you get it

```
$ sudo apt-get install python3.8
$ sudo apt-get install idle3
$ sudo apt install python3-pip
$ pip install pytz
```

Now install the zip file from this repl and move it to your linux directory

## 3. How To Use

Once you did all of the above, unzip the file then type in the linux terminal `python3 main.py` and then it will start the PyLine terminal. Type a command in the `~/user>` input field and press enter to run it (more info on commands below)

> If you want to change the boring `~/user>` to something more unique, type `terminal.name` and change it to something that fits you more


## 4. PyLine In-Depth 
PyLine is the terminals very own command line language that simplys file management. More will be added in the future

Below is every command, with more detailed explanations

### Terminal Commands

- `terminal.help`: Displays a list of all the commands in the terminal

- `terminal.time`: Displays the time and date in the date format month/day/year, and in the am/pm time format (In the eastern time zone)

- `terminal.name`: Changes the `~/user>` input field to something unique, type the command then enter your new name

- `terminal.refresh`: Refreshes the terminal, erasing command history and reprinting the welcome message

- `terminal.quit`: Stops the PyLine Terminal and returns you to the linux terminal

### File Commands
> IMPORTANT! All commands below ONLY work with files in the userfiles directory.

> Make sure to add file extentions `.py`, `.txt`, etc. when requested to input file name

> If you have a file in a custom made folder, make sure to include the path. Example: ./folder/file

- `file.list`: Lists all the available to use files

- `file.create`: Creates a file from user input

- `file.edit`: Asks for file then opens up the text editor, when done typing click "save" to save the changes. The editor will automatically close

- `file.delete`: Asks for file then deletes it

### Folder (Directory) Commands

- `folder.create`: Creates a new folder

- `folder.add`: Moves a already existing file into a folder

- `folder.remove`: Moves a file from a folder to `userfiles`

- `folder.delete`: Deletes a folder and its contents

### Run Commands
> IMPORTANT! All commands below ONLY work with files in the userfiles directory.

> Make sure to add file extentions `.py`, `.txt`, etc. when requested to input file name

> If you have a file in a custom made folder, make sure to include the path. Example: ./folder/file

- `run.py`: Runs any Python file (`.py`)

- `run.c`: Runs any C file (`.c`)

- `run.sh`: Runs any Bash file (`.sh`)

## 5. Future Additions

This section is just for additions for the future, if you want something added, comment on the repl and itll be taken to consideration

- [x] Folder management -Myself

## 6. Usage Rights

To use the PyLine Terminal commercially you must give proper credit, a link to this repl will do fine

Example:

https://replit.com/@SCP-049/PyLine-Terminal?v=1

---
### Footnotes

PyLine version 2.3

Made by https://replit.com/@SCP-049 for use by anyone who stumbles upon this

![python powered logo](https://www.python.org/static/community_logos/python-powered-w-100x40.png)