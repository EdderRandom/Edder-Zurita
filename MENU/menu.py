from CRUD.encriptador import encode, decode
from CRUD.crud import *
from CONEX.conex import *
#from CLASE.clase import Persona
variable_conexion = conex


class Registro():
        
        def registro_usuario(self):      
            print("Registro de usuario")
            nombre = input("Ingrese el usuario: ")
            #email = input("Ingrese correo: ")
            clave = input("Ingrese una clave: ")
            print(f"La clave del usuaurio es ",{encode(clave)})
            registroUsuarios(nombre, encode(clave))

class MenuMascota:
    #MENU PARA LA CREACION DE LAS MASCOTAS A LA BASE DE DATOS
    def Menu():
        while True:
            #Menu del ingreso de los datos de mascota a una base de datos
            #Todas las funciones estan funcionando 
            print("\nMenu de registro de mascotas")
            print("\n1. Agregar mascotas a la lista")
            print("2. Mostar mascotas en la lista")
            print("3. Buscar mascotas por Numero de chip")
            print("4. Actualizar datos de la mascota")
            print("5. Eliminar mascota de la base de datos")
            print("6. Exportar desde la bd")
            print("7. importar a Json")
            print("8. Mostar datos Json")
            print("0. Salir del menu")
            opc = int(input("Ingrese una opción : "))
            
            if opc ==1:

                print("Ingrese mascotas desde: ")
                opc = input("1 .Insertar directo: \n2 .Insertar desde la clase: \n>> ")

                if opc == "1": #Funcionando
                    while True:
                        try:
                            especie = input("Ingrese la especie: ") 
                            color = input("Ingrese el color: ") 
                            edad = int(input("Ingrese la edad: ")) 
                            tamaño = input("Ingrese el tamaño: ") 
                            raza = input("Ingrese la raza: ") 
                            nombre= input("ingrese el nombre: ") 
                            numero_chip = int(input("Ingrese el chip: "))
                            insertarMascota(especie, color, edad, tamaño, raza, nombre, numero_chip)
                        except ValueError:
                            print("Ingrese valores correctos")
    

                elif opc == "2": # ingresar mascota desde la clase, en construccion
                    print("mostrar desde la clase")
            
            elif opc ==2: #Funcionado
                print("Mostar la lista de mascotas en la base de datos")
                mostrarMascota(variable_conexion)

            elif opc ==3: #Funcionando
                print("Buscar mascota por numero de chip")
                try:
                    buscardor_chip = int(input("Ingrese el chip de la mascota: "))
                    numero_chip = BuscarMascota(buscardor_chip, variable_conexion)
                except ValueError: #Manejo de error por si se ingresa una letra
                    print("Ingrese un valor valido")

                if numero_chip:
                    print("Mascota no encontrada")
                    
                else:
                    print("Mascota encontrada")

            elif opc == 4: #Funcionado
                try:
                    print("Actualizar datos de mascota")
                    numero_chip = int(input("Ingrese el chip de la mascota a actualizar datos: "))
                    encontrada =BuscarMascota(numero_chip, variable_conexion)

                except ValueError:
                    print("Valores invalidos")

                if encontrada is None:
                    print("Mascota encontrada, ingrese los nuevos datos")
                    nuevo_nombre = input("ingrese el nuev nombre de la mascota: ")

                    filas_actualizada = updateMascota(numero_chip, nuevo_nombre,variable_conexion)

                    if filas_actualizada is not None and filas_actualizada > 0:
                        print("Mascota actualizada exitosamente")
                    else:
                        print("no se encontro la mascota")
                    

            elif opc == 5: #Funcionando
                try:
                    print("Quitar mascota de la base de datos")
                    chip_eliminar = int(input("Ingrese el chip de la mascota: "))
                    eliminarMascota(chip_eliminar)
                    print("Mascota Eliminada")
                except ValueError:
                    print("ingrese valores validos")

            elif opc==6: #Funcionando
                print("Vamos a exportar a JSON")
                prepararexportarMascota()

            elif opc ==7: #Funcionando
                print("Vamos a importar desde JSON hacia la base de datos")
                importarMascotaJson()

            elif opc ==8:#Funcionando
                print("Datos existentes")
                mostrarJson("Mascotas.json")

            elif opc == 0:

                print("""Has salido del menu muchas gracias""") #Salida
                break
            else:
                print("Selecciona una opcion valida")
