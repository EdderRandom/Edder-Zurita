#Clase animal que posteriormente heredara a otras clases si es necesario
class Animal:
    def __init__(self, especie, color, edad, tamaño):
        self.especie = especie
        self.color = color
        self.edad = edad
        self.tamaño = tamaño
        
    #Metodos de animales, utilizar mas tarde 
    def lamer_pelaje(self):
        pass
    def comer(self):
        pass
    def dormir(self):
        pass
    def tomar_agua(self):
        pass

