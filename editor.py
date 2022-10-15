fileName = input("\033[0;30mEnter file name: \033[0;0m")

# Lotta imports
from tkinter import *
import terminal
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re

window = Tk()
editor = Text()

def done():
    global window
    while True:
      print("")
      terminal.run()

# Saves edits then closes the window
def save():
    global fileName, command, done
    with open("./userfiles/" + fileName, "w") as file:
        global editor, terminal
        code = editor.get("1.0", "end")
        file.write(code)
        file.close()
        print("\nSaved edits")
        window.destroy()
        done()

# Config for the window
menuBar = Menu(window)
fileBar = Menu(menuBar, tearoff=0)

fileBar.add_command(label="Save edits", command=save)
menuBar.add_cascade(label="Save", menu=fileBar)

window.title("Text Editor")
window.config(menu=menuBar, bg="black")
editor.config(bg="black", fg="white", 	
insertbackground="white")
menuBar.config(fg="green", bg="black")

# Syntax Highlighting
cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat(), re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#000000'}

cdg.tagdefs['COMMENT'] = {'foreground': '#0c6e01'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#0286fa'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#ffea03'}
cdg.tagdefs['STRING'] = {'foreground': '#ff9e03'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#ffea03'}

ip.Percolator(editor).insertfilter(cdg)

editor.pack()

# Asks for the file, then opens it
try:
    with open("./userfiles/" + fileName, "r") as file:
        code = file.read()
        editor.delete("1.0", "end")
        editor.insert("1.0", code)
        file.close() 
    print("\nFile loaded")
except:
    print("\033[1;31m\nFile not found:", fileName)
    done()
  
window.mainloop()