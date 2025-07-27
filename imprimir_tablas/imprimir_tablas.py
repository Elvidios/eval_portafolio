"""Utilizar sentencias iterativas para la elaboración de un algoritmo que resuelve un problema acorde al lenguaje Python.

Crear un programa que utilice bucles for y while para repetir acciones.

Ejemplo: Un generador de tablas de multiplicar o una calculadora de factoriales."""

print('\n Parametros de la tabla')
numero = int(input('Ingrese un numero: '))
rango_base = int(input('Ingrese la base del rango: '))
rango_tope = int(input('Ingrese el tope del rango: '))
print('\n Su tabla:')
for i in range(rango_base, rango_tope + 1): 
    print(numero, '*', i, 'es igual a', numero*i)

