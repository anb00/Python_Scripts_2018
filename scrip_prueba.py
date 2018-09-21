#!/usr/bin/python
#-*- coding:utf-8 -*-
import Tkinter

def miClose():
    texto1 = Tkinter.Label(principal, text="Are you Sure,Close ?").pack()
    
def saludar():
    texto['text']= "Holaa"
    
principal = Tkinter.Tk()
#principal2 = Tkinter.Tk()
#Crear etiqueta
#etiqueta=Tkinter.Label(principal2,text="Segunda ventana")
#etiqueta.pack()
#etiqueta.mainloop()
principal.geometry('450x450+500+400')
principal.title('MyProgram AV')
texto = Tkinter.Label(principal, text="My Primer programa",bg='blue',fg='white')
texto.pack()
# Creamos dos botones de maeras parecidas
boton_saluda = Tkinter.Button(principal, text="PULSAR",command=saludar)
otro_boton = Tkinter.Button(text = 'Cerrar',command = miClose,fg='yellow',bg='black').pack()
boton_minimizar = Tkinter.Button(principal, text="Minimizar",command=principal.iconify)

boton_minimizar.pack()
boton_saluda.pack()
principal.mainloop()
