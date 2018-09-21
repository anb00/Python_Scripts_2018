#!/usr/bin/python
#-*- coding:utf-8 -*-
import Tkinter
def saludar():
    texto['text']="Hola amigo"
    def despedir():
        texto['text']="Hasta la vista"

        principal =Tkinter.Tk()

        principal.wm_title("programilla")
        texto= Tkinter.Label(principal,text="saluda")

        boton_saluda=Tkinter.Button(principal,text="Hola",command=saludar)
        boton_despide=Tkinter.Button(principal,text="Adios",command=despedir)

        texto.pack()
        boton_saluda.pack()
        boton_despide.pack()

        principal.mainloop()
