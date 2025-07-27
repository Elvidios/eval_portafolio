def area_rectangulo():
    print('\n||| Ingrese los parametros de su figura: Rectangulo |||')
    altura = float(input('Altura: '))
    base = float(input('Base: '))

    area = (altura * base)
    print(f'El area de su rectangulo es igual a {area:.2f}cm cuadrados')

def main():
    area_rectangulo()