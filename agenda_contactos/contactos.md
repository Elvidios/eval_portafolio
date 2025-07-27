# Gestor Básico de Contactos en Consola

Este script en Python permite gestionar una lista de contactos desde la consola, utilizando un menú interactivo para **agregar**, **mostrar** y **eliminar** contactos.

## Características principales

- Los contactos se almacenan en una lista (`contactos`).
- Cada contacto es un diccionario con dos claves:
  - `'Nombre completo'`
  - `'telefono'`
- El programa corre en un bucle `while` hasta que el usuario decide salir.

## Funcionalidades

### 1. Agregar Contacto

La función `agregar_contacto()` solicita al usuario:

- Nombre completo del contacto.
- Número de teléfono (solo acepta números enteros).

Luego, guarda esta información como un diccionario dentro de la lista `contactos`.

### 2. Mostrar Contactos

La función `mostrar_contactos()` recorre la lista y muestra todos los contactos registrados. Si no hay contactos, muestra un mensaje indicando que la lista está vacía.

### 3. Eliminar Contacto

La función `eliminar_contacto()` presenta los contactos numerados y permite eliminar uno, ingresando el número correspondiente. Verifica que la entrada sea válida antes de eliminar.

### 4. Menú interactivo

El script muestra un menú con las siguientes opciones:

- `AGREGAR`: Llama a `agregar_contacto()`.
- `MOSTRAR`: Llama a `mostrar_contactos()`.
- `ELIMINAR`: Llama a `eliminar_contacto()`.
- `SALIR`: Termina la ejecución.

Cualquier opción no reconocida muestra un mensaje de error.

## Notas

- El script usa la palabra clave `global` para modificar la lista `contactos` desde dentro de las funciones.
- La información no se guarda en archivos ni bases de datos; al salir del programa, los contactos se pierden.

Desarrollado como ejercicio de práctica en Python para manipulación de listas, diccionarios y entrada/salida en consola.