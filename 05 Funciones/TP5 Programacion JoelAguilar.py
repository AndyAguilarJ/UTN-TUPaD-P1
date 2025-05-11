//1

multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

//2

mis_favoritos = ["promocionae", "esta", "materia", "con", "9"]

# Mostrar el penúltimo elemento
print("El penúltimo elemento es:", mis_favoritos[-2])

//3

palabras = []

palabras.append("aguante")
palabras.append("boke")
palabras.append("y polente")

print("Lista resultante:", palabras)

//4

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print("Lista modificada:", animales)

//5
"""
Se define una lista llamada numeros con los valores [8, 15, 3, 22, 7], max(numeros) encuentra el número más grande de la lista, que es 22.
numeros.remove(22) elimina ese valor de la lista.Finalmente, se imprime la lista sin el número 22.
"""

//6

numeros = list(range(10, 31, 5))
print("Los dos primeros números son:", numeros[0], "y", numeros[1])

//7

autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["lancia", "nisan"]
print("Lista modificada:", autos)

//8

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

//9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")

compras[1][compras[1].index("fideos")] = "tallarines"

compras[0].remove("pan")

print("Lista de compras modificada:", compras)

//10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print("Lista anidada:", lista_anidada)