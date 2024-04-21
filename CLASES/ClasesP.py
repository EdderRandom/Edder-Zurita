#Clase persona que sera utilizada para crear trabajadores y clientes.
#En creacion para ser agregado al menu

class Persona():
    def __init__(self, nombre_completo, rut, direccion, telefono):
        self.nombre_completo = nombre_completo
        self.__rut = rut #Rut lo usare como metodo privado, ya que lo ingresare publico para dejarlo registrado pero luego no es necesario que lo muestre, si no es necesario
        self.direccion = direccion
        self.telefono = telefono

    def dueño_mascota():
        pass
    def numero_rut(self):
        return self.__rut 
    #metodo de pago a usar en otro lado para convertirlo en publico en esta clase lo coloco privado, luego lo uso en otro lado publico
    def __metodo_pago(self):
        return self.__metodo_pago
    
    