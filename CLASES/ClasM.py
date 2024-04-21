from ClasG import Gato

#Clase mascota que hereda de gato y que a su ves hereda de animal
class Mascota(Gato):
    #Contructor de la clase mascota
    def __init__(self, especie, color, edad, tamaño, raza, nombre, chip):
        super().__init__(especie, color, edad, tamaño, raza)
        self.nombre = nombre
        self.__chip = chip
        self.dueño = None
    
    def __str__(self):
        return'''
        Especie:\t{} 
        Color:\t\t{}
        Edad:\t\t{}
        Tamaño:\t\t{}
        Raza:\t\t{}
        Nombre:\t\t{}'''.format(self.especie, self.color, self.edad, self.tamaño, self.raza, self.nombre) # Chip atributo privado
          
    #Asignar a la mascota el dueño, por hacer...
    def asignar_dueño():
        pass
    def mostrar_dueño():
        pass
    #Donde va el metodo privado 
    def numero_chip(self):
        return self.__chip
    pass

