import mysql.connector

#Modulo que me servirá para hacer la conexión a la base de datos
def conex():
    try:
        myconn = mysql.connector.connect(host="localhost",
                                         user="edder",
                                         passwd="asdf",
                                         database="adopciones")
        print("Conectado....")
        cur = myconn.cursor()
        cur.execute("select nombre, email, fecha from tabla_registro_usuario") # luego lo utilizare en el código para la conexión, 
        #tener cuidado con los nombres para que me conecten todos 
        result = cur.fetchall() #captura los registros de la tabla (fetchall), se almacenan en resul
        #for row in result: # se ocupa en este lugar #ESTA PARTE ME MUESTRA LOS USUARIOS QUE TENGO
            #print("%s\t%s\t%s" % (row[0], row[1], row[2])) #% me concatena la tupla, (,)Tupla
        return myconn
    except:
        #registrar un log....
        #myconn.rollback()
        print("Error")
    #myconn.close()
#conex()#OCUPAR EN OTRO MODULO NO ACTIVA EN ESTE MODULO PORQUE SE DUPLICA INFORMACION