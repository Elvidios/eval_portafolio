def area_trapecio():
    print('\n||| Ingrese los parametros de su figura: Trapecio |||')
    altura = float(input('Altura: '))
    base_mayor = float(input('Base mayor: '))
    base_menor = float(input('Base menor: '))

    area = ((base_mayor + base_menor) * altura / 2)
    print(f'El area de su trapecio es igual a {area:.2f}cm cuadrados')

def main():
    area_trapecio()





















