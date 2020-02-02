from tkinter import *
from tkinter import messagebox
from random import choice

items = []
root = Tk()
root.title("Raffle")
root.geometry("208x290")

item = Entry(root)
item.grid(row=0, column=0, pady=30)


def add():
    if item.get() == "":
        return
    items.append(item.get())
    item_list.insert(END, item.get())
    item.delete(0, END)


addButton = Button(root, text="add", command=add)
addButton.grid(row=0, column=1, pady=30)

item_list = Listbox(root)
item_list.grid(row=2, column=0, pady=30)


def raffle():
    rndm_item = choice(items)
    messagebox.showinfo("", f"{rndm_item}")


raffleButton = Button(root, text="choose item", command=raffle)
raffleButton.grid(row=2, column=1, pady=30)

root.mainloop()
