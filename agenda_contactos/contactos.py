contactos = []

def agregar_contacto():
    global contactos
    print('\n || Agregar Contacto ||')
    nombre_contacto = str(input('Nombre del contacto: '))
    telefono_contacto = int(input('Numero de telefono: '))

    contacto = {
        'Nombre completo':nombre_contacto,
        'telefono':telefono_contacto
    }

    contactos.append(contacto)
    print(contactos)

def mostrar_contactos():
    global contactos
    if not contactos:
        print("No hay contactos registrados.")
        return
    
    print('\n || Lista de Contactos ||')
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto['Nombre completo']} - {contacto['telefono']}")

def eliminar_contacto():
    global contactos
    if not contactos:
        print("No hay contactos para eliminar.")
        return
    
    print('\n || Eliminar Contacto ||')
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto['Nombre completo']} - {contacto['telefono']}")
    
    numero = int(input("Ingrese el número del contacto a eliminar: ")) - 1
    
    if 0 <= numero < len(contactos):
        contactos.pop(numero)
        print("Contacto eliminado.")
        print(contactos)
    else:
        print("Número inválido.")

while True:
    accion = input("\n¿Qué desea hacer? (AGREGAR/MOSTRAR/ELIMINAR/SALIR): ").upper()
    
    if accion == 'AGREGAR':
        agregar_contacto()
    elif accion == 'MOSTRAR':
        mostrar_contactos()
    elif accion == 'ELIMINAR':
        eliminar_contacto()
    elif accion == 'SALIR':
        break
    else:
        print("Opción inválida. Use: AGREGAR, MOSTRAR, ELIMINAR o SALIR")

print(f"\nTotal final: {len(contactos)} contactos")