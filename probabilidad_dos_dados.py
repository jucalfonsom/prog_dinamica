#Simulacion de probabilidades de dos dados
import random
from bokeh.plotting import figure, show


def tirar_dado(numero_de_intentos):
    secuencia_de_tiros = []

    for _ in range(numero_de_intentos):
        tiro_A = random.randint(1, 6)
        tiro_B = random.randint(1, 6)
        total = tiro_A + tiro_B
        secuencia_de_tiros.append(total)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
        

    tiros_con_doce = 0
    tiros_sin_doce = 0

    for tiro in tiros:
        if 12 in tiro:
            tiros_con_doce += 1
        else:
            tiros_sin_doce += 1
    
    probabilidad_tiros_con_doce = tiros_con_doce/numero_de_intentos
    probabilidad_tiros_sin_doce = tiros_sin_doce/numero_de_intentos
    
    print(f'La probabilidad de obtener por lo menos un 12 en {numero_de_tiros} = {probabilidad_tiros_con_doce}')
    print(f'La probabilidad de no obtener por lo menos un 12 en {numero_de_tiros} = {probabilidad_tiros_sin_doce}')


if __name__ == "__main__":
    numero_de_tiros = int(input('Ingrese el número de tiros de los dados A y B: '))
    numero_de_intentos = int(input('Ingrese el número de corridas de la simulación: '))

    main(numero_de_tiros, numero_de_intentos)
