import tkinter as tk
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        refresh_task_list()
        entry.delete(0, tk.END) 
def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        del tasks[selected_task]
        refresh_task_list()
    except IndexError:
        pass
def update_task():
    try:
        selected_task = task_list.curselection()[0]
        updated_task = entry.get()
        if updated_task:
            tasks[selected_task] = updated_task
            refresh_task_list()
            entry.delete(0, tk.END)
    except IndexError:
        pass
def refresh_task_list():
    task_list.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{index}. {task}")
root = tk.Tk()
root.title("To-Do List")
tasks = []
label = tk.Label(root, text="To-Do List")
label.pack()
entry = tk.Entry(root, width=55)
entry.pack(pady=5)  
task_list = tk.Listbox(root, width=50)
task_list.pack(pady=5)  
button_frame = tk.Frame(root)
button_frame.pack()
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5, pady=5)
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5, pady=5)
update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=5, pady=5)
root.geometry("400x300") 
root.mainloop()
