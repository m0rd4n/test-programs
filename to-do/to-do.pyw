from tkinter import *

root = Tk()
root.title("To-Do")
root.geometry("260x270")

item = Entry(root, width=32)
item.grid(row=0, column=0, pady=10)


def init():
    tasks = open("tasks.txt", 'w+')
    content = tasks.readlines()
    if len(content) != 0:
        if ord(content[-1][-1:]) != 10:
            tasks = open("tasks.txt", 'a')
            tasks.write("\n")
        tasks = open("tasks.txt", 'r')
    for line in tasks:
        item_list.insert(END, line)
    tasks.close()


def add():
    if item.get() == "":
        return
    item_list.insert(END, item.get())
    with open("tasks.txt", "a") as tasks:
        tasks.write(item.get()+"\n")
    tasks.close()
    item.delete(0, END)


addButton = Button(root, text="add", command=add)
addButton.grid(row=0, column=1, pady=10)

item_list = Listbox(root, height=13, width=32)
item_list.grid(row=2, column=0, pady=8)


def done():
    selection = item_list.curselection()
    pos = 0
    for i in selection:
        idx = int(i) - pos
        item_list.delete(idx, idx)
        pos = pos + 1
    new_content = item_list.get(0, END)
    with open("tasks.txt", "w") as tasks:
        for task in new_content:
            tasks.write(task)
    tasks.close()


delButton = Button(root, text="task done", command=done)
delButton.grid(row=2, column=1, pady=8)

init()
root.mainloop()
