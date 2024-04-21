#Donde almacenare los datos del Hogar
class HogarAdopcion():
    def __init__(self, nombre, direccion, numero_contacto , correo):
        self.nombre = nombre
        self.dirreccion = direccion
        self.numero_contacto = numero_contacto
        self.correo = correo
    
    def __str__(self):
        print("""   Datos de contacto del Hogar Patitas Felices
            Adopta y da felicidad""")
        return'''
        Nombre del Hogar:\t{}
        Dirrecion:\t\t{}
        Numero de contacto:\t{}
        Correo electronico:\t{}'''.format(self.nombre, self.dirreccion, self.numero_contacto, self.correo)

datos = HogarAdopcion("Patitas Felices", "Narnia", 999999 , "sinecesitasayuda@contactanos.cl")


