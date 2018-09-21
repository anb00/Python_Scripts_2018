#!/usr/bin/python
#-*- coding:utf-8 -*-
def filtra(dato):
    if dato > 5:
        return True
    else:
        return False
salida = filter(filtra,[ 1,7,9,2,0,4,7,9,0,6,5,1,45,22])
print salida
