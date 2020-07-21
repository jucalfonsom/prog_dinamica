import random
import collections

PALOS = ['Corazon', 'Trebol', 'Diamante', 'Pica']
VALORES = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas


def obtener_mano(barajas, tamano_mano):
    manos = random.sample(barajas, tamano_mano) #funcion de random para obtener una muestra de una colección sin sustitución

    return manos


def main(tamano_mano, intentos):
    barajas = crear_baraja()
    manos = []

    for _ in range(intentos): #Obtener la mano aleatoria del tamaño dado por el usuario
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)
    
    pares = 0
    for mano in manos: #Obtener si existe algún par dentro de la mano
        valores = []
        for carta in mano:
            valores.append(carta[1]) #Obtengo la posición 1 porque tengo tuplas de (palo, valor)

        counter = dict(collections.Counter(valores)) #Contar la cantidad de veces que hay un valor dentro de un arreglo
        for val in counter.values():
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en {intentos} intentos es: {probabilidad_par}')


if __name__ == "__main__":
    tamano_mano = int(input('¿De cuántas barajas será la mano? '))
    intentos = int(input('¿Cuántos intentos para calcular la probabilidad? '))

    main(tamano_mano, intentos)