import Tkinter 

window = Tkinter.Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
rad1 = Tkinter.Radiobutton(window,text='First', value=1)
rad2 = Tkinter.Radiobutton(window,text='Second', value=2)
rad3 = Tkinter.Radiobutton(window,text='Third', value=3)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
window.mainloop()
