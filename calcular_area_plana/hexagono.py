def area_hexagono():
    print('\n||| Ingrese los parametros de su figura: Hexagono |||')
    lado = float(input('Lado: '))
    apotema = float(input('Apotema: '))

    area = (6 * lado * apotema / 2)
    print(f'El area de su hexagono es igual a {area:.2f}cm cuadrados')

def main():
    area_hexagono()
