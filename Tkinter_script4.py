#!/usr/bin/python
#-*- coding:utf-8 -*-
import Tkinter


window = Tkinter.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
def clicked():
    messagebox.showinfo('Message title', 'Message content')
btn = Tkinter.Button(window,text='Click here', command=clicked)
btn.grid(column=0,row=0)
window.mainloop()
