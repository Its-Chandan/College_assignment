# Name    : Biswal Chandan Ramachandra
# Div     : A
# Enroll  : E20110192000310012
# sem     : 6
# subject : python
# pc no   : 53






# # import tkinter
# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
# mainloop()

# from tkinter import *
# import time

# root= Tk()
# root.geometry("400x100")
# root.config(bg='black')

# def update():
#     clock.config(text=time.strftime("%I:%M:%S"))
#     clock.after(1000,update)


# clock = Label(root, background = 'black',foreground = 'white', font = ('arial', 40, 'bold'))
# clock.pack()
# update()
# root.title('clock')
# root.mainloop()

from tkinter import *
from tkinter import messagebox

root =Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert Box","Stop Virus found")


but= Button(root,text="ok",command=msg)
but.place(x=100,y=100)
root.mainloop()                                                                                   
