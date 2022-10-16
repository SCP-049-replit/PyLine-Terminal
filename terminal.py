import pyline

def text():
    print("\033[0;32mWelcome to the PyLine terminal"), print(
    "")
    print('Type "terminal.help" to see list of commands'), print("")

def run():
    namefile = open("user.txt", "r")
    name = namefile.read()
    userInput = input("\033[0;33m~/%s> \033[0;0m" % name)
  
    # Command checker and runner
  
    # Terminal commands
    if userInput == "terminal.help":
        pyline.help()
    elif userInput == "terminal.time":
        pyline.time()
    elif userInput == "terminal.name":
        pyline.name()
    elif userInput == "terminal.refresh":
        pyline.refresh()
    elif userInput == "terminal.root":
        pyline.root()
    elif userInput == "terminal.quit":
        pyline.quit()
      
    # File commands
    elif userInput == "file.list":
        pyline.list()
    elif userInput == "file.create":
        pyline.create()
    elif userInput == "file.edit":
        pyline.edit()
    elif userInput == "file.delete":
        pyline.delete()

    # Folder commands
    elif userInput == "folder.create":
        pyline.folcreate()
    elif userInput == "folder.add":
        pyline.foladd()
    elif userInput == "folder.remove":
        pyline.folremove()
    elif userInput == "folder.delete":
        pyline.foldelete()

    # Run commands
    elif userInput == "run.py":
        pyline.runpy()
    elif userInput == "run.c":
        pyline.runc()
    elif userInput == "run.sh":
        pyline.runsh()
    else:
        print('\033[1;31m\nUnknown command:', userInput), print("\033[0;0m")

