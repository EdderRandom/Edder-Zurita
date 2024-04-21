from ClasesP import Persona
#Clase trabajador en contruccion
class Trabajador(Persona):
    def __init__(self, nombre_completo, rut, direccion, telefono, cargo, titulo):
        super().__init__(self, nombre_completo, rut, direccion, telefono)
        self.cargo = cargo
        self.__titulo = titulo

    def __str__(self):
        return'''
        Nombre Completo:\t{}
        Rut:\t{}
        Direccion:\t{}
        Telefono de contacto:\t{}
        Cargo:\t{}
        Titulo:\t{}'''.format(self.nombre_completo, self.__rut, self.direccion, self.telefono,self.cargo, self.__titulo)
    
    def area_trabajo():
        pass
    def titulo_prof(self):
        return self.__titulo
    
    def ingresar_al_hogar(self):
        pass