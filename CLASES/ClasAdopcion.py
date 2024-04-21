from ClasM import Mascota

#Funciones del Menu
class Adopcion():
    def __init__(self,patitas):
        self.patitas = patitas
        self.mascotas=[]
        
    def agreagar_mascota(self,mascota):
        if isinstance(mascota,Mascota):
            self.mascotas.append(mascota)
            print("Se ha agregado el michi al hogar")
        else:
            print("solo adoptamos gatos")
            
    #Donde muestro las mascotas y que se usa en el menu
    def mostar_mascotas(self,):
        print("Michis en adopcion")
        for mascota in self.mascotas:
            print(mascota)
            print("Elige un michi!")
        if not self.mascotas:
            print("lista vacia, adoptemos!")
        
    #Metodo para eliminar mascotas, y que se usara en el menu mas adelante 
    def eliminar_mascota(self, chip_a_eliminar):
        print("Gracias por adoptarnos!")
        mascotas_eliminadas = []

        for i, mascota in enumerate(self.mascotas):
            if mascota.numero_chip() == chip_a_eliminar:
                mascotas_eliminadas.append(self.mascotas.pop(i))

        if mascotas_eliminadas:
            print(f"Se han eliminado las siguientes mascotas con chip {chip_a_eliminar}:")
            for mascota_eliminada in mascotas_eliminadas:
                print(f"- {mascota_eliminada.nombre} (Chip: {chip_a_eliminar})")
        else:
            print(f"No se encontraron mascotas con el chip {chip_a_eliminar}.")
