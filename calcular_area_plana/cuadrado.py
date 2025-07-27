def area_cuadrado():
    print('\n||| Ingrese los parametros de su figura: Cuadrado |||')
    lado = float(input('Lado: '))

    area = (lado ** 2)
    print(f'El area de su cuadrado es igual a {area}cm cuadrados')

def main():
    area_cuadrado()