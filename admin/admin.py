# Pops up all commands; admin.help
def help():
    print('''\nCommands:
    admin.help          displays help menu
    admin.list          lists terminal files
    admin.create        creates a terminal file
    admin.edit          edit terminal files
    admin.delete        deletes a terminal file
    admin.quit          return to the main terminal
  ''')

# Lists all files; admin.list
def list():
    import glob
    print("")
    print(glob.glob("*"))
    print("")
  
# Creates a new file named via user; admin.create
def create():
    name = input("\033[0;34mEnter file name: \033[0;0m")
    file = open(name, "w")
    file.close()
    print("\nFile created")
    print("")

# Opens text editor; admin.edit
def edit():
    exec(open('./admin/editor.py').read())

# Deletes a terminal file; admin.delete
def delete():
    file = input("\033[0;34mEnter file name: \033[0;0m")
    try:
        import os
        os.remove(file)
        print("\nFile deleted")
        print("")
    except:
        print("\n\033[1;31mFile not found:", file)
        print("")

# Exits root; admin.quit
def quit():
    import main
    main.start()