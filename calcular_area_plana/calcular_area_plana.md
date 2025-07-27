# Herramienta para calculo de areas de figuras planas.

Este script en Python permite calcular el area de figuras planas a traves de un menu interactivo.

El programa depende de los siguientes archivos/módulos (uno por figura):

- `circulo.py`
- `cuadrado.py`
- `hexagono.py`
- `pentagono.py`
- `rectangulo.py`
- `rombo.py`
- `romboide.py`
- `trapecio.py`
- `triangulo.py`
- `salir.py` 

Cada módulo contiene una función `main()` que realiza el cálculo del área solicitando los datos necesarios al usuario.

## Funcionamiento

Al ejecutar `menu.py`, se presenta un menú numerado con las siguientes opciones:

||| Calcular el Área de la Siguiente Figura: |||
[1] Circulo
[2] Cuadrado
[3] Hexagono
[4] Pentagono
[5] Rectangulo
[6] Rombo
[7] Romboide
[8] Trapecio
[9] Triangulo
[10] Salir

El usuario debe ingresar el número de la figura que desea calcular. Si la opción es válida, se ejecuta la función `main()` del módulo correspondiente, que debe manejar la entrada de datos y mostrar el resultado.

Si la opción ingresada no es válida, se muestra un mensaje de error y el menú vuelve a mostrarse.

## Requisitos

- Cada módulo debe estar en el mismo directorio que `menu.py`.

## Notas

- Cada módulo tiene implementada una función `main()` sin argumentos.
- La opción `[10] Salir` llama a un módulo llamado `salir.py`.
