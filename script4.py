
class Animal:
 """Clase base para mostrar la herencia"""
def __init__(self, nombre, patas):
 self.nombre= nombre
 self.patas = patas
def saluda(self):
 print("El animal llamado " + str(self.nombre) + " saluda")
mi_masscota.saluda()
