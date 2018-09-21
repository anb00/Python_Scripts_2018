#!/usr/bin python
#-*- coding: utf-8 -*-
dividendo = "A"
divisor = 2
try:
    resultado = dividendo/divisor

except ZeroDivisionError:
        if divisor == 0:
            print "No puedes dividir oir cer,animal"
except TypeError:
            print "Hay que ser bruto: eso no es un número"
else:
            print "la división resulta:",resultado
            
a = 0
while a < 10:
    a = a + 1
    if a == 6:
        break
    print a

