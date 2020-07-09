#Simulacion de probabilidades de un dado
import random
from bokeh.plotting import figure, show


def tirar_dado(numero_de_intentos):
    secuencia_de_tiros = []

    for _ in range(numero_de_intentos):
        tiro = random.randint(1, 6)
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_uno = 0
    tiros_sin_uno = 0

    for tiro in tiros:
        if 1 in tiro:
            tiros_con_uno += 1
        else:
            tiros_sin_uno += 1
    
    probabilidad_tiros_con_uno = tiros_con_uno/numero_de_intentos
    probabilidad_tiros_sin_uno = tiros_sin_uno/numero_de_intentos
    
    print(f'La probabilidad de obtener por lo menos un 1 en {numero_de_tiros} = {probabilidad_tiros_con_uno}')
    print(f'La probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} = {probabilidad_tiros_sin_uno}')


if __name__ == "__main__":
    numero_de_tiros = int(input('Ingrese el número de tiros del dado: '))
    numero_de_intentos = int(input('Ingrese el número de corridas de la simulación: '))

    main(numero_de_tiros, numero_de_intentos)
