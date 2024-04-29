from tkinter import *
from tkinter import messagebox
import pickle

# Set up the main window
window = Tk()
window.title("TO DO LIST")
window.geometry("400x500")
window.config(bg="#343a40")  # Dark gray background

# Function to add a new task
def add_task():
    task = entrybox.get()
    if task:
        listbox.insert(END, task)
        entrybox.delete(0, END)
    else:
        messagebox.showwarning(title="Warning", message="You must enter a task!")

# Function to delete a selected task
def del_task():
    try:
        selected_item = listbox.curselection()[0]
        listbox.delete(selected_item)
    except IndexError:
        messagebox.showwarning(title="Warning", message="You must select a task to delete")

# Function to load tasks from a file
def load_task():
    try:
        with open("tasks.dat", "rb") as task_file:
            tasks = pickle.load(task_file)
        listbox.delete(0, END)
        for task in tasks:
            listbox.insert(END, task)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No file found!!!")

# Function to save tasks to a file
def save_task():
    tasks = listbox.get(0, END)
    with open("tasks.dat", "wb") as task_file:
        pickle.dump(tasks, task_file)

# Listbox to display tasks
Framebox = Frame(window, bg="#495057")  # Darker gray for the frame
Framebox.pack(pady=20)
listbox = Listbox(Framebox, height=10, width=53, bg="#adb5bd", fg="black")  # Light gray listbox
scroll_bar = Scrollbar(Framebox, orient="vertical")
scroll_bar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=True)
listbox.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=listbox.yview)

# Entry widget to enter new tasks
entrybox = Entry(window, width=40, bg="#ced4da", fg="black")  # Very light gray entry box
entrybox.pack(pady=10)

# Frame for buttons
Framebox2 = Frame(window, bg="#6c757d")  # Light gray frame for buttons
Framebox2.pack(fill=X, padx=20, pady=20)

# Buttons to add, delete, load, and save tasks
addbutton = Button(Framebox2, text="Add Task", width=15, command=add_task, bg="#dee2e6", fg="black")  # Very light gray buttons
delbutton = Button(Framebox2, text="Delete Task", width=15, command=del_task, bg="#dee2e6", fg="black")
loadbutton = Button(Framebox2, text="Load Task", width=15, command=load_task, bg="#dee2e6", fg="black")
savebutton = Button(Framebox2, text="Save Task", width=15, command=save_task, bg="#dee2e6", fg="black")

addbutton.grid(row=0, column=0, padx=10, pady=10)
delbutton.grid(row=0, column=1, padx=10, pady=10)
loadbutton.grid(row=1, column=0, padx=10, pady=10)
savebutton.grid(row=1, column=1, padx=10, pady=10)

# Start the main event loop
window.mainloop()
