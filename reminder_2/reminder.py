from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database


db = Database('reminder.db')
window = Tk()
window.title("Reminder Management System")
window.geometry("1920x1080+0+0")
window.config(bg="#2c3e50")
window.state("normal")


date = StringVar()
time = StringVar()
remadetail = StringVar()
mobno = StringVar()
email = StringVar()
alerttime = StringVar()

# Entries Frame
entries_frame = Frame(window, bg="#535c68")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Remainder", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

lbldate = Label(entries_frame, text="Date", font=("Calibri", 16), bg="#535c68", fg="white")
lbldate.grid(row=1, column=0, padx=10, pady=10, sticky="w")
txtdate = Entry(entries_frame, textvariable=date, font=("Calibri", 16), width=30)
txtdate.grid(row=1, column=1, padx=10, pady=10, sticky="w")

lbltime = Label(entries_frame, text="time", font=("Calibri", 16), bg="#535c68", fg="white")
lbltime.grid(row=1, column=2, padx=10, pady=10, sticky="w")
txttime = Entry(entries_frame, textvariable=time, font=("Calibri", 16), width=30)
txttime.grid(row=1, column=3, padx=10, pady=10, sticky="w")

lblremadetail = Label(entries_frame, text="Remainder_detail", font=("Calibri", 16), bg="#535c68", fg="white")
lblremadetail.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtremadetail = Entry(entries_frame, textvariable=remadetail, font=("Calibri", 16), width=30)
txtremadetail.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblmobno = Label(entries_frame, text="Contact no", font=("Calibri", 16), bg="#535c68", fg="white")
lblmobno.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtmobno = Entry(entries_frame, textvariable=mobno, font=("Calibri", 16), width=30)
txtmobno.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
lblEmail.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
txtEmail.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblalerttime = Label(entries_frame, text="AlertTime", font=("Calibri", 16), bg="#535c68", fg="white")
lblalerttime.grid(row=3, column=2, padx=10, pady=10, sticky="w")
comboalerttime = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=alerttime, state="readonly")
comboalerttime['values'] = ("10min","30min", "1hour")
comboalerttime.grid(row=3, column=3, padx=10, sticky="w")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    date.set(row[1])
    time.set(row[2])
    remadetail.set(row[3])
    mobno.set(row[4])
    email.set(row[5])
    alerttime.set(row[6])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_employee():
    if txtdate.get() == "" or txttime.get() == "" or txtremadetail.get() == "" or txtmobno.get() == "" or txtEmail.get() == "" or comboalerttime.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtdate.get(),txttime.get(), txtremadetail.get() , txtmobno.get() ,txtEmail.get(), comboalerttime.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_employee():
    if txtdate.get() == "" or txttime.get() == "" or txtremadetail.get() == "" or txtmobno.get() == "" or txtEmail.get() == "" or comboalerttime.get()== "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtdate.get(), txttime.get(), txtremadetail.get(), txtmobno.get(), txtEmail.get(), comboalerttime.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def delete_employee():
    db.remove(row[0])
    clearAll()
    dispalyAll()


def clearAll():
    date.set("")
    time.set("")
    remadetail.set("")
    mobno.set("")
    email.set("")
    alerttime.set("")
    



btn_frame = Frame(entries_frame, bg="#535c68")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, text="Add Details",command=add_employee, width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame,  text="Update Details",command=update_employee, width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, text="Delete Details",command=delete_employee, width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame,text="Clear Details",command=clearAll, width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)


# Table Frame
tree_frame = Frame(window, bg="#ecf0f1")
tree_frame.place(x=0, y=480, width=1980, height=520)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 18),
                rowheight=50)  # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=3)
tv.heading("2", text="Date")
tv.column("2", width=3)
tv.heading("3", text="time")
tv.column("3", width=3)
tv.heading("4", text="Remainder_detail")
tv.column("4", width=3)
tv.heading("5", text="Contact no")
tv.column("5", width=3)
tv.heading("6", text="Email")
tv.column("6", width=3)
tv.heading("7", text="Alert Time")
#tv.heading("8", text="Address")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

dispalyAll()




window.mainloop()