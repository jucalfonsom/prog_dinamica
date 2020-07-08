from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho) #Retorna la coordenada de origen (0, 0)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho) #Mueve el borracho

    return inicio.distancia(campo.obtener_coordenada(borracho)) #Retorna nueva coordenada


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(name = 'Juan') #Inicializa Borracho tradicional con nombre Juan
    origen = Coordenada(0, 0) #Origen del borracho
    distancias = [] #Arreglo de las distancias recorridas

    for _ in range(numero_de_intentos):
        campo = Campo() #Inicializa clase campo
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias


def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    
    #Cálculo de cada una de las distancias
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/ len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)

        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')


if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

     