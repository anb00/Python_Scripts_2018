#!/usr/bin/python
# -*- coding: utf-8 -*-
class Animal(object):
    def __init__(self,nombre,patas):
        self.nombre=nombre
        self.patas=patas
        def muestra(self):
            print("el" + self.nombre+"tiene"+ self.patas + "patas.")
            chucho = Animal("perro",4)
            chucho.muestra()
