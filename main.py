from MENU.menu import Registro,MenuMascota
from CRUD.encriptador import encode, decode
from CRUD.crud import *
from TIPOSDECOLORESYTEXTO.colores import *
from TIPOSDECOLORESYTEXTO.tipografia import NEGRITA
variable_conexion = conex()


#usuario = edder
#password = asdf

while True:
    print(BLANCO)
    print("-","=".center(52,"="),"-")
    print("|", "\033[1mLogin de Usuario".center(56), "|")
    print("-","=".center(52,"="),"-")
    print(VERDE)
    print("\t\t1- Registrar usuario")
    print("\t\t2- Login ")
    print("\t\t0- Exit ")
    op = input('\t\t>>')
    print(RESET)

    if op == '1':
        a = Registro()
        a.registro_usuario()
    
    elif op == '2':

        print("Login de acceso de usuario")
        nombre = input('Ingrese su usuario: ')
        clave = input('Ingrese su clave: ')
        acceso = decode(clave,buscarClave(nombre))
        #CON ESTO REVISABA LOS ERRORS, ME AYUDO MUCHO A ENCONTRAR EL PROBLEMA
        #print("La clave encriptada: ", encode(clave))
        #print("viene del decode: ", decode(clave, buscarClave(nombre)))
        #print("viene del buscarclave: ", buscarClave(nombre))
        registroUsuarios(nombre, encode(clave))

        if acceso == True:
            print("Has accedido al menu")
            m = MenuMascota.Menu()
        else:

            print('Usuario y/o contraseña invalida')

    elif op == '0':
        print("Vuelva pronto.")
        break
    else:
        print("Ingrese los datos de nuevo")