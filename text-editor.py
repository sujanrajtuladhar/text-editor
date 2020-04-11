from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
# import tkinter.scrolledtext
from tkinter.scrolledtext import ScrolledText

# creation of object
root = Tk(className="Simple Text Editor")
# textPad = ScrolledText(root, Width=600, height=600)
textPad = tkinter.scrolledtext.ScrolledText(root, width=40, height=10)

# function to open file


def open_command():
    file = filedialog.askopenfile(
        parent=root, mode="rb", title="select a file")
    if file != None:
        contents = file.read()
        textPad.insert("1.0", contents)
        file.close()


def save_command():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        data = textPad.get("1.0", END + "-1c")
        file.write(data)


def exit_command():
    # askokcancel -- title and message
    if tkinter.messagebox.askokcancel("Quit", "Do you really want to quite?"):
        # close gui
        root.destroy()


def about_command():
    # it also contain title and message
    label = tkinter.messagebox.showinfo(
        "About", "This Simple Text Editor is created for Python learning")


def work():
    print("Its Working")


def res():
    print("GUI window resized")
    root.geometry("200x100")


def norm():
    print("GUI window back to normal")
    root.geometry("400x300")


menu_1 = Menu(root)
root.config(menu=menu_1)


# first menu
file_menu = Menu(menu_1)
menu_1.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New file", command=work)
file_menu.add_command(label="Open", command=open_command)
file_menu.add_command(label="Save", command=save_command)
file_menu.add_command(label="Exit", command=exit_command)


# second menu
edit_menu = Menu(menu_1)
menu_1.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Resize", command=res)
edit_menu.add_command(label="Normal", command=norm)
edit_menu.add_cascade(label="Cut")
edit_menu.add_cascade(label="Copy")
edit_menu.add_cascade(label="Paste")


# third menu
view_menu = Menu(menu_1)
menu_1.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="About", command=about_command)


# fourth menu
code_menu = Menu(menu_1)
menu_1.add_cascade(label="Code", menu=code_menu)


# fifth menu
run_menu = Menu(menu_1)
menu_1.add_cascade(label="Run", menu=run_menu)


# sixth menu
help_menu = Menu(menu_1)
menu_1.add_cascade(label="Help", menu=help_menu)


# add status bar
status = Label(root, text="Run", bg="yellow", relief=SUNKEN, bd=1)

status.pack(side=BOTTOM, fill=X)


textPad.pack()

root.mainloop()
