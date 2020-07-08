import random

#Clase borracho
class Borracho:

    def __init__(self, name):
        self.name = name
    

class BorrachoTradicional(Borracho):

    #llamado a la super clase
    def __init__(self, name):
        super().__init__(name)
    
    #Crear todas las posibles opciones
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])