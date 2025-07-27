# Generador de Tablas de Multiplicar

Este proyecto en Python permite generar tablas de multiplicar de un número elegido por el usuario, dentro de un rango definido.

---

## Funcionamiento

1. El usuario debe ingresar:
   - Un número base para la tabla de multiplicar.
   - Un número de inicio del rango (mínimo del multiplicador).
   - Un número tope del rango (máximo del multiplicador).

2. El programa imprime la tabla de multiplicar del número seleccionado dentro del rango definido por el usuario.

---

## Estructura iterativa

Se utiliza un bucle `for` con la función `range()`:

```python
for i in range(rango_base, rango_tope + 1):
    print(numero, '*', i, 'es igual a', numero * i)