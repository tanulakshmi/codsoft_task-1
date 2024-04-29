from tkinter import *
from tkinter import font, messagebox
import pickle

# Initialize the main window
window = Tk()
window.geometry("400x500")
window.config(bg="#343a40")
window.overrideredirect(True)  # Remove default window frame to use custom title bar

# Custom Font for Title Bar
custom_font = font.Font(family="Helvetica", size=12, weight="bold")

# Functions for Window Controls
def minimize_window():
    window.state('iconic')

def maximize_window():
    if window.state() == 'normal':
        window.state('zoomed')
    else:
        window.state('normal')

def close_window():
    window.destroy()

# Create the custom title bar
title_bar = Frame(window, bg='#495057', relief='raised', bd=0)
title_bar.pack(fill=X)

# Title Label
title_text = Label(title_bar, text="TO DO LIST", bg='#495057', fg='white', font=custom_font)
title_text.pack(side=LEFT, padx=10)

# Control Buttons
close_button = Button(title_bar, text='X', command=close_window, bg='red', fg='white', padx=10, pady=2, borderwidth=0)
close_button.pack(side=RIGHT)

minimize_button = Button(title_bar, text='-', command=minimize_window, bg='gray', fg='white', padx=10, pady=2, borderwidth=0)
minimize_button.pack(side=RIGHT)

maximize_button = Button(title_bar, text='□', command=maximize_window, bg='gray', fg='white', padx=10, pady=2, borderwidth=0)
maximize_button.pack(side=RIGHT)

# Enable dragging of the window by clicking on the title bar
def drag_window(event):
    x = window.winfo_pointerx() - event.widget.winfo_rootx()
    y = window.winfo_pointery() - event.widget.winfo_rooty()
    window.geometry(f"+{x}+{y}")

title_bar.bind("<ButtonPress-1>", drag_window)
title_bar.bind("<B1-Motion>", drag_window)

# Functionality for To-Do List
def add_task():
    task = entrybox.get()
    if task:
        listbox.insert(END, task)
        entrybox.delete(0, END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def del_task():
    try:
        selected_item = listbox.curselection()[0]
        listbox.delete(selected_item)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def load_task():
    try:
        with open("tasks.dat", "rb") as task_file:
            tasks = pickle.load(task_file)
        listbox.delete(0, END)
        for task in tasks:
            listbox.insert(END, task)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No file found!")

def save_task():
    tasks = listbox.get(0, END)
    with open("tasks.dat", "wb") as task_file:
        pickle.dump(tasks, task_file)

# GUI Layout for Tasks
framebox = Frame(window, bg="#495057")
framebox.pack(pady=20, fill=BOTH, expand=True)
listbox = Listbox(framebox, height=10, width=50, bg="#adb5bd", fg="black")
scroll_bar = Scrollbar(framebox)
scroll_bar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=True)
listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)

entrybox = Entry(window, width=40, bg="#ced4da", fg="black")
entrybox.pack(pady=10)

framebox2 = Frame(window, bg="#6c757d")
framebox2.pack(fill=X, padx=20, pady=20)

addbutton = Button(framebox2, text="Add Task", width=15, command=add_task, bg="#dee2e6", fg="black")
delbutton = Button(framebox2, text="Delete Task", width=15, command=del_task, bg="#dee2e6", fg="black")
loadbutton = Button(framebox2, text="Load Task", width=15, command=load_task, bg="#dee2e6", fg="black")
savebutton = Button(framebox2, text="Save Task", width=15, command=save_task, bg="#dee2e6", fg="black")

addbutton.grid(row=0, column=0, padx=10, pady=10)
delbutton.grid(row=0, column=1, padx=10, pady=10)
loadbutton.grid(row=1, column=0, padx=10, pady=10)
savebutton.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()
