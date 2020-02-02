from tkinter import *
from tkinter import messagebox
from random import choice
from tkinter.simpledialog import askstring

items = []
root = Tk()
root.title("Raffle")
root.geometry("245x265")

item = Entry(root)
item.grid(row=0, column=0, pady=10)


def add():
    if item.get() == "":
        return
    items.append(item.get())
    item_list.insert(END, item.get())
    item.delete(0, END)


addButton = Button(root, text="add", command=add)
addButton.grid(row=0, column=1, pady=10)

item_list = Listbox(root)
item_list.grid(row=2, column=0, pady=8)


def raffle():
    rndm_item = choice(items)
    messagebox.showinfo("", f"{rndm_item}")


raffleButton = Button(root, text="choose item", command=raffle)
raffleButton.grid(row=3, column=0, pady=8)


def delete():
    selection = item_list.curselection()
    pos = 0
    for i in selection:
        idx = int(i) - pos
        item_list.delete(idx, idx)
        pos = pos + 1
    items.pop(selection[0])


delButton = Button(root, text="delete selected item", command=delete)
delButton.grid(row=2, column=1, pady=8)

root.mainloop()
