def area_pentagono():
    print('\n||| Ingrese los parametros de su figura: Pentagono |||')
    lado = float(input('Lado: '))
    apotema = float(input('Apotema: '))

    area = (5 * lado * apotema / 2)
    print(f'El area de su pentagono es igual a {area:.2f}cm cuadrados')

def main():
    area_pentagono()
