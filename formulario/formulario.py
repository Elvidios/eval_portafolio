"""Distinguir los tipos de datos y sentencias básicas del lenguaje para la construcción de programas.

Desarrollar un script que haga uso de distintos tipos de datos como cadenas, enteros, flotantes y booleanos.

Ejemplo: Un formulario en consola que solicite información del usuario y la almacene en variables adecuadas."""

usuarios = []

def formulario_x():
    global usuarios
    #Variables en base a inputs.
    nombre_completo = str(input('Ingrese su nombre completo: '))

    edad = int(input('Su edad: '))

    estatura = float(input('Ingrese su estatura aproximada: '))

    respuesta_internet=input('Posee acceso a internet? Responda SI/NO: ').upper()

    #Condicionales segun respuesta.
    if respuesta_internet == 'SI':
        internet = True
    elif respuesta_internet == 'NO':
        internet = False
    else:
        print('Respuesta invalida. Responda (SI/NO)')
        return
    
    #Diccionario del formulario.
    usuario = {
        'Nombre completo':nombre_completo,
        'Edad':edad,
        'Estatura':estatura, 
        'Acceso a internet': internet
    }

    print('Informacion ingresada:')
    
    #Lista de diccionarios.
    usuarios.append(usuario)
    print('\n Lista de usuarios:')
    print(usuarios)

while True:
    formulario_x()
    continuar = input("\n¿Desea agregar otro usuario? (SI/NO): ").upper()
    if continuar != 'SI':
        break

print(f"\nTotal final: {len(usuarios)} usuarios")
    