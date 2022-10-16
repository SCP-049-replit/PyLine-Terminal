# Pops up all commands; terminal.help
def help():
    print('''\nFull documentation available at: https://github.com/SCP-049-replit/PyLine-Terminal
    
Commands:
    terminal.help      displays help menu
    terminal.time      displays the time (est)
    terminal.name      changes the username
    terminal.refresh   refreshes the terminal
    terminal.root      become root user
    terminal.quit      exits the terminal
           
    file.list          lists all files
    file.create        creates a new file
    file.edit          opens the text editor
    file.delete        deletes a file

    folder.create      creates a new directory
    folder.add         moves a file to a directory
    folder.remove      removes a file from a directory
    folder.delete      deletes a directory

    run.py             runs any python file
    run.c              runs any c file
    run.sh             runs any bash file 
  ''')


# Displays the time in the eastern standard time zone; terminal.time
def time():
    import datetime
    import pytz

    est = pytz.timezone("America/New_York")
    getTime = datetime.datetime.now(est)
    getDate = datetime.date.today()
    print(getDate.strftime("\n%m/%d/%y,"), getTime.strftime("%I:%M %p\n"))

# Changes display name; terminal.name
def name():
    name = input("\033[0;34mEnter new name: \033[0;0m")
    user = open("user.txt", "w")
    user.write(name)
    user.close()
    print("")


# Refreshes the terminal; terminal.refresh
def refresh():
    import main
    main.start()

# Become root user; terminal.root
def root():
    import os
    os.system("clear")
    from admin import root
    root.text()
  
    while True:
        root.run()
  
# Stops the terminal; terminal.quit
def quit():
    import sys
    print("\033[1;31m\nLogged out of PyLine Terminal")
    sys.exit()


# Lists all user files; file.list
def list():
    import glob
    print("")
    print(glob.glob("./userfiles/*"))
    print("")


# Creates a new file named via user; file.create
def create():
    name = input("\033[0;34mEnter file name: \033[0;0m")
    file = open("./userfiles/" + name, "w")
    file.close()
    print("\nFile created")
    print("")


# Opens text editor; file.edit
def edit():
    exec(open('editor.py').read())


# Deletes a file; file.delete
def delete():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    try:
        import os
        os.remove("./userfiles/%s" % file)
        print("\nFile deleted")
        print("")
    except:
        print("\n\033[1;31mFile not found:", file)
        print("")


# Creates a new folder named via user; folder.create
def folcreate():
    import os
    name = input("\033[0;34mEnter directory name: \033[0;0m")
    os.makedirs("./userfiles/%s" % name)
    print("\nDirectory created")
    print("")


# Moves a file into a folder; folder.add
def foladd():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    folder = input("\033[0;34mEnter directory name: \033[0;0m")
    filedir = "./userfiles/" + file
    folderdir = "./userfiles/" + folder
    try:
        import shutil
        shutil.move(filedir, folderdir)
        print("\nFile moved")
        print("")
    except:
        print("\n\033[1;31mFile/folder not found")
        print("")


# removes a file from a folder; folder.remove
def folremove():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    folder = input("\033[0;34mEnter directory name: \033[0;0m")
    filedir = "./userfiles/" + "/" + folder + "/" + file
    folderdir = "./userfiles/"
    try:
        import shutil
        shutil.move(filedir, folderdir)
        print("\nFile moved")
        print("")
    except:
        print("\n\033[1;31mFile/folder not found")
        print("")


# Deletes a folder; folder.delete
def foldelete():
    folder = input("\033[0;34mEnter directory name: \033[0;0m")
    folderdir = "./userfiles/" + folder
    try:
        import shutil
        shutil.rmtree(folderdir)
        print("\nDirectory deleted")
        print("")
    except:
        print("\n\033[1;31mFile/folder not found")
        print("")

# Runs a python file in userfiles; run.py
def runpy():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    print("")
    try:
        exec(open("./userfiles/" + file).read())
        print("")
    except:
        print("\033[1;31mFile not found/Error:", file)
        print("")


# Runs a c file in userfiles; run.c
def runc():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    print("")
    try:
        import subprocess
        subprocess.call(["gcc", "./userfiles/%s" % file])
        subprocess.call("./a.out")
        print("")
        print("")
    except:
        print("\033[1;31mFile not found/Error:", file)
        print("")


# Runs a bash file in userfiles; run.sh
def runsh():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    print("")
    try:
        import subprocess
        subprocess.call(["bash", "./userfiles/%s" % file])
        print("")
    except:
        print("\033[1;31mFile not found/Error:", file)
        print("")