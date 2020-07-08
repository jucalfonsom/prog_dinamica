
class Campo:
    
    def __init__(self):
        self.coordenadas_de_borrachos = {} #diccionario de las coordenadas de los borrachos
    
    #Agregar un nuevo borracho
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    #Mueve el borracho a través de la clase Borracho
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada
    
    #Obtener la coordenada para calcular la distancia
    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]
