
from ClasA import Animal
#Clase gato que hereda atributos de animal y se le agregan los propios
class Gato(Animal):
    def __init__(self, especie, color, edad, tamaño, raza):
        super().__init__(especie, color, edad, tamaño)
        self.raza = raza
        
    #Metodos de gatos
    def ronronea(self):
        pass    
    def casa_ratones(self):
        pass
    def gato_feliz(self):
        pass
    def gato_triste(self):
        pass