"""Utilizar sentencias condicionales para el control del flujo de un algoritmo que resuelve un problema simple acorde al lenguaje Python.

Implementar estructuras if, elif, else para la toma de decisiones.

Ejemplo: Un programa que determine si un número es positivo, negativo o cero."""



def positivo_negativo_cero():

    import random as rd

    numero = rd.randint(-5, 5)
    print(numero)
    if numero >= 1:
        print('Es positivo')
    elif numero <= -1:
        print('Es negativo')
    else:
        print('Es cero')

positivo_negativo_cero()