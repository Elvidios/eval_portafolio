def area_romboide():
    print('\n||| Ingrese los parametros de su figura: romboide |||')
    altura = float(input('Altura: '))
    base = float(input('Base: '))

    area = (altura * base)
    print(f'El area de su romboide es igual a {area:.2f}cm cuadrados')

def main():
    area_romboide()


