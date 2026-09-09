""""
Desarrollar un programa que solicite n cantidad de numeros enteros y almacene en una lista numeros aleatorios entre
0 y 99. Usando funciones definidas po el usuario
a) Calcular el elemanto mayor
b) Calcular el elemento menor
c) Calcular el promedio de los elementos
d) Calcular la mediana de los elementos
e) Calcular la moda de los elementos (incluyendo bimodal, multimodal)
f) Calcular la desviación estándar poblacional
"""
import os, random
os.system ("cls")   
n = int(input("Ingrese la cantidad de numeros enteros que desea generar: "))
lista = []
for _ in range(n):
    lista.append(random.randint(0, 101))
print(lista)

def mayor(lista):
    may = lista[0]
    for i in lista:
        if i > may: 
            may = i 
    #for i in range(len(lista)):
        #if lista[i] == max(lista):
        #return lista[i]
    return may

def menor(lista):
    may = lista[0]
    for i in lista:
        if i< may:
            may = i
    return may
    #for i in range(len(lista)):
    #    if lista[i] == min(lista):
    #        return lista[i]

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def mediana(lista):
    lista.sort() # el sort ordena la lista de menor a mayor y no necesita una varaible auxiliar
    if len(lista) % 2 == 0:
        aux = len(lista) // 2
        med =(lista[aux] + lista[aux - 1]) / 2
    else:
        pos = len(lista) // 2
        med = lista[pos]
    return med
def moda(lista):
    for i in lista:
        if lista.count(i) > 1:
            return i

def desviacion_estandar(lista):
    pass

print("El elemento mayor es: ", mayor(lista))
print("El elemento menor es: ", menor(lista))
print("El promedio de los elementos es: ", promedio(lista))
print("La mediana de los elementos es: ", mediana(lista))