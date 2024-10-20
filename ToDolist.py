import tkinter as tk
import sqlite3

root = tk.Tk()
root.title('To-Do List App')

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (task TEXT)''')


def add_task():
    task = entry.get()
    if task:
        c.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
        conn.commit()
        entry.delete(0, tk.END)
        update_listbox()

def delete_task(): 
    # Delete button will delete the first task added 
    # Works in FIFO
    task = listbox.get(tk.ACTIVE)
    c.execute('DELETE FROM tasks WHERE task = ?', (task,))
    conn.commit()
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for row in c.execute('SELECT task FROM tasks'):
        listbox.insert(tk.END, row[0])

frame = tk.Frame(root)
frame.pack()

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT)

add_button = tk.Button(frame, text='Add Task', command=add_task)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(frame, text='Delete Task', command=delete_task)
delete_button.pack(side=tk.LEFT)

listbox = tk.Listbox(root)
listbox.pack()

update_listbox()

root.mainloop()