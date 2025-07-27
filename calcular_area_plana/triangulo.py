def area_triangulo():
    print('\n||| Ingrese los parametros de su figura: Triangulo |||')
    altura = float(input('Altura: '))
    base = float(input('Base: '))

    area = (altura * base / 2)
    print(f'El area de su triangulo es igual a {area:.2f}cm cuadrados')

def main():
    area_triangulo()