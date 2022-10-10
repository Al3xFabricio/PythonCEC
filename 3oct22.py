# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:23:25 2022

@author: Alexander
"""

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
        
def funcion_():
    print("Función")
    
print(1)
funcion_()
funcion_()
funcion_()
print(2)

def funcion_2(primero, segundo, tercero):
    print("Función 1", primero)
    print("Función 2"+ segundo)
    print("Función 3", tercero)
    
    print(primero, " ", segundo, " ", tercero)
    
funcion_2("primero", "segundo", "tercero")

def resta(a, b):
    print(a - b)
    print (b - a)
    
resta(3, 7)

def mult(a, b):
    return a*b

r = mult(5, 4)
print (r)

def crearList(n):
    lista = []
    for item in range(n):
        lista.append(item)
    return lista

print(crearList(10))

