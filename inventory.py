# import dependencies
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import  ttk
from inventory_database import *

# instantiate database object
db = Database()


def populate_list():
    """This function fills the textbox with entries"""
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    """This function adds new entries into the table"""
    if partNum_text.get() == '' or description_text.get() == '' or quantityReceived_text.get() == '' \
            or quantityDelivered_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(partNum_text.get(), description_text.get(), quantityReceived_text.get(),
              quantityDelivered_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (partNum_text.get(), description_text.get(),
                            quantityReceived_text.get(), quantityDelivered_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    """This function activates the selected row for removal or updating"""
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        partNum_entry.delete(0, END)
        partNum_entry.insert(END, selected_item[1])
        description_entry.delete(0, END)
        description_entry.insert(END, selected_item[2])
        quantityReceived_entry.delete(0, END)
        quantityReceived_entry.insert(END, selected_item[3])
        quantityDelivered_entry.delete(0, END)
        quantityDelivered_entry.insert(END, selected_item[4])

    except IndexError:
        pass


def remove_item():
    """This function removes a row from the table"""
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    """for editing row data"""
    db.update(selected_item[0], partNum_text.get(), description_text.get(), quantityReceived_text.get(), quantityDelivered_text.get())
    populate_list()


def clear_text():
    """This clears enttries"""
    partNum_entry.delete(0, END)
    description_entry.delete(0, END)
    quantityReceived_entry.delete(0, END)
    quantityDelivered_entry.delete(0, END)


# create window object
app = Tk()


# partNum
partNum_text = StringVar()
partNum_label = Label(app, text="Part Number", font=('bold', 14), pady=10, padx=10)
partNum_label.pack(ipadx=30, ipady=30)
partNum_label.grid(row=0, column=0, sticky='w')
partNum_entry = Entry(app, textvariable=partNum_text)
partNum_entry.grid(row=0, column=1)

# desription
description_text = StringVar()
description_label = Label(app, text="Description", font=('bold', 14))
description_label.grid(row=0, column=2, sticky='W')
description_entry = Entry(app, textvariable=description_text)
description_entry.grid(row=0, column=3)


# Quantity Received
quantityReceived_text = StringVar()
quantityReceived_label = Label(app, text="Quantity Received", font=('bold', 14), padx=10)
quantityReceived_label.grid(row=1, column=0, sticky='w')
quantityReceived_entry = Entry(app, textvariable=quantityReceived_text)
quantityReceived_entry.grid(row=1, column=1)

# Quantity Delivered
quantityDelivered_text = StringVar()
quantityDelivered_label = Label(app, text="Quantity Delivered", font=('bold', 14))
quantityDelivered_label.grid(row=1, column=2, sticky='W')
quantityDelivered_entry = Entry(app, textvariable=quantityDelivered_text)
quantityDelivered_entry.grid(row=1, column=3)

# Parts List (listBox)
font = ("Arial", 12, "bold")
parts_list = Listbox(app, height=20, width=100, border=0, font=font, background="Gainsboro")
parts_list.grid(row=4, column=0, columnspan=3, rowspan=3, pady=20, padx=20, sticky=tkinter.EW)

# create scrollbar
scrollbar = ttk.Scrollbar(app, orient=tkinter.VERTICAL, command=parts_list.yview)
scrollbar.grid(row=4, column=3,sticky=tkinter.NS)

parts_list['yscrollcommand'] = scrollbar.set


# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
fonts = ("Arial", 10, "bold")
add_btn = Button(app, text='Add Part', width=12, activebackground='blue', command=add_item, font=fonts)
add_btn.grid(row=3, column=0, pady=20)

remove_btn = Button(app, text='Remove Part', width=12, activebackground='red', command=remove_item, font=fonts)
remove_btn.grid(row=3, column=1)

update_btn = Button(app, text='Update Part', width=12, activebackground='blue',command=update_item, font=fonts)
update_btn.grid(row=3, column=2)

clear_btn = Button(app, text='Clear Input', width=12, activebackground='blue',command=clear_text, font=fonts)
clear_btn.grid(row=3, column=3)


app.title('Inventory Manager')
app.geometry('1200x700')

# instantiates textbox population
populate_list()

# start program
app.mainloop()
