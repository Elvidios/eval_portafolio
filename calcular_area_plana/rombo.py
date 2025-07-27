def area_rombo():
    print('\n||| Ingrese los parametros de su figura: Rombo |||')
    diagonal_mayor = float(input('Diagonal mayor: '))
    diagonal_menor = float(input('Diagonal menor: '))

    area = (diagonal_mayor * diagonal_menor / 2)
    print(f'El area de su rombo es igual a {area:.2f}cm cuadrados')

def main():
    area_rombo()



