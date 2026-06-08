from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("500x600")
root.config(bg="#DBCDCD")

tasks = []

# Functions
def add_task():
    task = task_entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        task_listbox.insert(END, "⬜ " + task)
        task_entry.delete(0, END)
        status_label.config(text="Task Added Successfully")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        status_label.config(text="Task Deleted")
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def mark_complete():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)

        if "✅" not in task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, task.replace("⬜", "✅"))
            status_label.config(text="Task Completed")
    except:
        messagebox.showwarning("Warning", "Select a task first!")

# Heading
title = Label(
    root,
    text="📋 Smart To-Do List",
    font=("Arial", 22, "bold"),
    bg="#f4f4f4"
)
title.pack(pady=15)

# Entry
task_entry = Entry(
    root,
    font=("Arial", 14),
    width=30
)
task_entry.pack(pady=10)

# Add Button
Button(
    root,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=add_task
).pack(pady=5)

# Frame for Listbox + Scrollbar
frame = Frame(root)
frame.pack(pady=20)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

task_listbox = Listbox(
    frame,
    width=40,
    height=15,
    font=("Arial", 13),
    yscrollcommand=scrollbar.set,
    selectbackground="#6A5ACD"
)

task_listbox.pack(side=LEFT)
scrollbar.config(command=task_listbox.yview)

# Buttons
Button(
    root,
    text="✅ Mark Complete",
    font=("Arial", 12),
    bg="#2196F3",
    fg="white",
    command=mark_complete
).pack(pady=5)

Button(
    root,
    text="🗑 Delete Task",
    font=("Arial", 12),
    bg="#f44336",
    fg="white",
    command=delete_task
).pack(pady=5)

# Status Label
status_label = Label(
    root,
    text="Welcome!",
    font=("Arial", 11),
    bg="#f4f4f4",
    fg="green"
)
status_label.pack(pady=20)

root.mainloop()