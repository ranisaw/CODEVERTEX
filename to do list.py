import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():  # Ensure the task is not empty
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# Setting up the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# UI Components
title_label = tk.Label(root, text="To-Do List", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task, bg="green", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=delete_task, bg="red", fg="white")
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 12), command=clear_tasks, bg="blue", fg="white")
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 14))
task_listbox.pack(pady=10)

# Start the main event loop
root.mainloop()
