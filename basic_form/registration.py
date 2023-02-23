# Name    : Biswal Chandan Ramachandra
# Div     : A
# Enroll  : E20110192000310012
# sem     : 5
# subject : python
#asgnment : Registration form
# pc no   : 53

from tkinter import *
from functools import partial
from tkinter import messagebox



def validateLogin(username, password, usermail):
	print("username entered :", username.get())
	print("password entered :", password.get())
	print("mail entered :", usermail.get())
	print("mobile entered :", mobile.get())
	


	return

def exit_app():
    confex = messagebox.askquestion(
        'Quit Confirmation', 'are you sue you want to quit?')
    if confex.upper() == "YES":				
        tkWindow.destroy()
    else:
        pass


	
#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Reg Form by - chandan')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  


#usermail label and text entry box
useremailLabel = Label(tkWindow, text="User Email").grid(row=1, column=0)
usermail = StringVar()
usermailEntry = Entry(tkWindow, textvariable=usermail).grid(row=1, column=1)  


#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)  

validateLogin = partial(validateLogin, username, password, usermail)

#mobile label and text entry box
usermobile = Label(tkWindow, text="User mobile").grid(row=3, column=0)
mobile = StringVar()
usermobileEntry = Entry(tkWindow, textvariable=mobile).grid(row=3, column=1)  

#Register button
loginButton = Button(tkWindow, text="Register", command=lambda:[validateLogin(), exit_app()]).grid(row=4, column=0)  

tkWindow.mainloop()
# root.mainloop()
