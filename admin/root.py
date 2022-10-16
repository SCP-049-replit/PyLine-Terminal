from admin import admin

def text():
    print("\033[0;32mWelcome to the PyLine root terminal"), print(
    "")
    print('Type "admin.help" to see list of commands'), print("")

def run():
    userInput = input("\033[0;30m~/root> \033[0;0m")
  
    if userInput == "admin.help":
        admin.help()
    elif userInput == "admin.list":
        admin.list()
    elif userInput == "admin.create":
        admin.create()
    elif userInput == "admin.edit":
        admin.edit()
    elif userInput == "admin.delete":
        admin.delete()
    elif userInput == "admin.quit":
        admin.quit()
    else:
        print('\033[1;31m\nUnknown command:', userInput), print("\033[0;0m")
