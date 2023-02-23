from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('Chandan')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

    
Label(
    ws,
    text="Dashboard",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)



ws.mainloop()
