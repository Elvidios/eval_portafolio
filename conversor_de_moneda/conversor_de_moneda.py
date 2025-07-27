"""Utilizar los conceptos fundamentales del lenguaje Python para la construcción de programas.

Crear un programa que implemente variables, operadores y estructuras básicas del lenguaje Python.

Ejemplo: Un conversor de unidades (temperatura, monedas, longitudes)."""

def convertidor_usd_a_clp():
    tasa_de_cambio = 952.38
    #Pregunta al usuario: Dolares estadounidenses(USD) o Pesos chilenos(CLP)
    divisa= input('Ingrese la abreviacion de la divisa que desea cambiar. Dolares estadounidenses(USD) o Pesos chilenos(CLP)?: ').upper()
    #Si USD
    if divisa == "USD":
        consulta_USDs = input('Ingrese su cantidad de Dolares estadounidenses:')
        cantidad_USDs = float(eval(consulta_USDs))
        #Conversion USD a CLPc 
        conversion_USD= (tasa_de_cambio * cantidad_USDs)
        print(f'{consulta_USDs} Dolares estadounidenses equivalen a {conversion_USD:.2f} Pesos chilenos')

    elif divisa == "CLP":
        consulta_CLPs = input('Ingrese su cantidad de Pesos Chilenos:').upper()
        cantidad_CLPs = float(eval(consulta_CLPs))
        #Conversion CLP a USD
        conversion_CLPs= (cantidad_CLPs / tasa_de_cambio)
        print(f'{consulta_CLPs} Pesos chilenos equivalen a {conversion_CLPs:.2f} Dolares estadounidenses')

    else: 
        print("Divisa invalida. Ingrese 'USD' o 'CLP'")

convertidor_usd_a_clp()