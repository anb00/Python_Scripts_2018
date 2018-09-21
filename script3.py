#!usr/bin python
def imprime_lista(nombre_lista, *items):
    print("Lista de " + nombre_lista)
    for algo in items:
        print algo
imprime_lista("Piezas","tornillo","tuerca","otro tornillo","cable")
