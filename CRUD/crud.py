from CONEX.conex import *
from datetime import datetime
import traceback

#La "tabla_usuario" es donde almacenare los datos de lops usuario que ire creando, eliminado, actualizando
#que tiene que llamarse de la misma forma que el "sql" para que se cree de buena forma
#ocupar el commit para para guardar los datos que se estén creando actualizando y eliminado

def selectAll(connection):
    try:
        connection = conex()
        cur = connection.cursor()
        cur.execute("select nombre, email, fecha from tabla_registro_usuario") #recordar cambiar el "user" para la tabla de sql
        result = cur.fetchall()
        print("Nombre\t\tEmail\t\tFecha") #Date time se maneja desde python. 
        for row in result:
            print("{}   {}  {}  ".format(row[0], row[1], row[2]))
        #connection.close() #este me cierra la conexión y me genera problemas
    except Exception as ex:
        connection.rollback()
        print("error", ex)

def selectOne(nombre, connection): #esta selection la pregunta en el def de selectOne
    sql="select nombre, email, fecha from tabla_registro_usuario where nombre = %s" #que viene de la tabla que de poo verano
    try:
        connection = conex()
        cur = connection.cursor()
        cur.execute(sql, (nombre,)) #la , hace la diferencia entre una tupla y una variable cualquiera, la coma la convierte en tupla
        resultado = cur.fetchone()
        if resultado is not None:
            print("Nombre\t\tEmail\t\tFecha")
            print("{} {} {}".format(resultado[0],resultado[1],resultado[2]))
            return True
        else:
            print("no hay datos que mostrar")
    except Exception as ex:
        connection.rollback()
        print("error", ex)

#INSERTAR A LA BASE DE DATOS PARA LOS ANIMES, RECONOCER LOS DATOS PARA QUE QUEDEN BIEN 
def insertarMascota(especie, color, edad, tamaño, raza, nombre, numero_chip):
    sql = "insert into hogar_adopcion(especie, color, edad, tamaño, raza, nombre, numero_chip) values (%s,%s,%s, %s, %s, %s, %s) "
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql,(especie, color, edad, tamaño, raza, nombre, numero_chip))
        conexion.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Datos ingresados OK")
        else:
            print("No hubo cambios")
    except Exception as ex:
        conexion.rollback()
        print("error", ex, traceback.print_exc())

def mostrarMascota(conection):
    try:
        conection = conex()
        cur = conection.cursor()
        cur.execute("select especie, color, edad, tamaño, raza, nombre, numero_chip from hogar_adopcion")
        result = cur.fetchall()

        if not result:
            print("No hay mascotas para mostrar. ")

        for row in result:

            print("\nMascotas en la lista....")
            
            print("Especie:\t{}".format(row[0]))
            print("Color:\t\t{}".format(row[1]))
            print("Edad:\t\t{} años".format(row[2]))
            print("Tamaño:\t\t{}".format(row[3]))
            print("Raza:\t\t{}".format(row[4]))
            print("Nombre:\t\t{}".format(row[5]))
            print("Numero de chip:\t{}".format(row[6]))
            #conection.close()
    except Exception as ex:
        conection.rollback()
        print("Error", ex)

def BuscarMascota(numero_chip,conection):
    sql = ("select especie, color, edad, tamaño, raza, nombre, numero_chip from hogar_adopcion where numero_chip = %s ")
    try:
        conection = conex()
        cur = conection.cursor()
        cur.execute(sql,(numero_chip,))
        result = cur.fetchone()

        if result is not None:

            print("\nInformación de la mascota:")
            print("Especie:\t{}".format(result[0]))
            print("Color:\t\t{}".format(result[1]))
            print("Edad:\t\t{} años".format(result[2]))
            print("Tamaño:\t\t{}".format(result[3]))
            print("Raza:\t\t{}".format(result[4]))
            print("Nombre:\t\t{}".format(result[5]))
            print("Numero Chip:\t{}".format(result[6])) 

        else:
                print("No se encontraron datos para el chip: {}".format(numero_chip))
            #conection.close()
    except Exception as ex:
        conection.rollback()
        print("Error", traceback.print_exc())
    
def eliminarMascota(numero_chip):

    sql = "delete from hogar_adopcion where numero_chip = %s"
    try:
        conection = conex()
        cursor = conection.cursor()
        cursor.execute(sql, (numero_chip,))
        conection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Registro eliminado exitosamente")
        else:
            print("No hubo cambios")
    except Exception as ex:
        print("Error", ex)

def updateMascota(numero_chip, nombre, conection):
    sql = "update hogar_adopcion set nombre=%s where numero_chip = %s"
    try:
        conection = conex()
        cursor = conection.cursor()
        cursor.execute(sql, (nombre, numero_chip))
        filas_actualizada = cursor.rowcount
        conection.commit()
        print(f"Se actualizo los datos {filas_actualizada}de la mascota")
        return filas_actualizada
    except Exception as ex:
        print("Error", ex)

####################################################################################################################################################
def registroUsuarios(nombre,clave): #inserto usuarios a la tabla
    sql = "insert into tabla_registro_usuario (nombre,clave) values (%s,%s)" #ser iguales a la base de datos, cambiar si son necesarios
    try:
        conection = conex()
        cursor = conection.cursor()
        cursor.execute(sql,(nombre,clave ))
        conection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Datos ingresados OK")
        else:
            print("No hubo cambios")
    except Exception as ex:
        print("Error:",ex,traceback.print_exc())

def eliminarUsuario(nombre):
    sql = "delete from tabla_registro_usuario where nombre = %s"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql,(nombre,))
        conexion.commit()
        filas = cursor.rowcount
        conexion.close()
        if filas > 0:
            return 0
        else:
            return 1 
    except:
        print("Error")

def actualizarUsuario(nombre, email):
    sql = "update tabla_registro_usuario set email =%s where nombre = %s"
    try:
        conexion = conex()
        cursor = conexion.cursor()
        cursor.execute(sql, (email, nombre))
        conexion.commit()
        filas = cursor.rowcount
        conexion.close()
        return filas
    except:
        print("error")

#####################################################################################################################################
def insertCredencial(nombre,clave):
    sql = "insert into credencial_usuario (nombre,clave) values (%s, %s)" #ser iguales a la base de datos, cambiar si son necesarios
    try:
        conection = conex()   
        cursor = conection.cursor()
        cursor.execute(sql,(nombre,clave))
        conection.commit()
        filas = cursor.rowcount
        if filas > 0:
            print("Datos ingresados OK")
        else:
            print("No hubo cambios")

    except Exception as ex:
        conection.rollback()
        print("error",ex ,traceback.print_exc())

def buscarClave(nombre):    
    sql = "select clave from tabla_registro_usuario where nombre = %s"
    try:
        conection = conex()
        cursor = conection.cursor()
        cursor.execute(sql, (nombre,))
        result = cursor.fetchone()
        return result[0] #para mostrar el contenido 
    
    except Exception as ex:
        conection.rollback()
        print("Error", ex)

##########################################################################################################
######JSON############
import json

#Para la exportacion de los datos por Json
        
def prepararexportarMascota():
    lista = []
    dic = {}
    connection = conex()

    try:
        cursor = connection.cursor()
        cursor.execute("select especie, color, edad, tamaño, raza, nombre, numero_chip from hogar_adopcion")
        result = cursor.fetchall()

        for mascota in result:
            datos_mascota = {
                "especie": mascota[0],
                "color":mascota[1], 
                "edad":mascota[2], 
                "tamano":mascota[3], 
                "raza":mascota[4], 
                "nombre":mascota[5], 
                "numero_chip":mascota[6]}
            lista.append(datos_mascota)

        dic ["Mascotas"] = lista
        print("Recursos importados")
        exportarMascota("Mascotas.json", dic)

    except Exception as ex:
        print(ex)
    return lista

def exportarMascota(archivo, obj):
    resu={}#solo para almacenar el mensaje
    try:
        out_file = open(archivo, "w", encoding="utf-8")
        json.dump(obj, out_file, indent=4)
        out_file.close()
    except Exception as ex:
        print("Error al exportar a Json:{}".format(ex))

def importarMascotaJson():
    try:
        ruta = "Mascotas.json"
        with open(ruta) as file:
            data = json.load(file)

        mascotas = data.get("Mascotas", [])

        for mascota in mascotas:
            insertarMascota(
                mascota['especie'], 
                mascota['color'], 
                mascota['edad'], 
                mascota['tamano'],
                mascota["raza"],
                mascota["nombre"],
                mascota["numero_chip"])
        print("Datos importados satisfactoriamente")

    except Exception as ex:
        print(f"Error al importar desde JSON: {ex}")
        
def mostrarJson(ruta):
    try:
        with open(ruta) as file:
            data = json.load(file)
        print(json.dumps(data, indent=4))

    except Exception as ex:
        print("Error al mostrar Json:{}".format(ex))