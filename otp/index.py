from tkinter import *
import tkinter.messagebox as tsmg
import random
import requests
import json

root=Tk()

rand=random.randint(1,999999)

msg=f"Your One Time Password(OTP) is {rand}"

def nextPage():
    root.destroy()
    import index

root.geometry("500x500")
root.title("OTP-Checker")

num=StringVar()
otp=StringVar()

f1=Frame(root)
Label(f1,text="Index Page",font="SegoeUI 30 bold",fg="purple").pack(padx=5,pady=10)
f1.pack(fill=BOTH)


root.mainloop()