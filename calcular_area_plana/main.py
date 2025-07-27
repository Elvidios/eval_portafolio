import circulo
import cuadrado
import hexagono
import pentagono
import rectangulo
import rombo
import romboide
import trapecio
import triangulo
import salir


def menu():
    opciones={
        '1':('Circulo', circulo),    
        '2':('Cuadrado', cuadrado),
        '3':('Hexagono', hexagono),
        '4':('Pentagono', pentagono),
        '5':('Rectangulo', rectangulo),
        '6':('Rombo', rombo),
        '7':('Romboide', romboide),
        '8':('Trapecio', trapecio),
        '9':('Triangulo', triangulo),
        '10':('Salir', salir)
    }
    while True:
        print('||| Calcular el Area de la Siguiente Figura: |||')
        for key, (opcion, _) in opciones.items():
            print(f'[{key}] {opcion}')
        seleccion=input('opcion: ')
        if seleccion in opciones:
            opciones[seleccion][1].main()
        else:
            print('opcion invalida intente denuevo')

menu()
