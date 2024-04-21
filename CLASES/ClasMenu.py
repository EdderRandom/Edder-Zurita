#Edder Abraham Zurita Cuevas
#18293373-2
#Clase de Poo Verano

from ClasVet import datos
from ClasAdopcion import Adopcion
from ClasM import Mascota

masc=Adopcion("patitas")#Viene de la clase adopcion

print(datos) #Viene de la clase Veterinaria 

while True:
    print("\n*** Ingrese los datos de la mascota ***")
    print("1. Agregar mascotas ")
    print("2. Mostrar mascotas ")
    print("3. Adoptar mascota ") #adoptar es como eliminar la mascota de la lista
    print("4. Salir ")
        
    opcion = input("Elige una opcion: ")
        
    if opcion == "1":
        
        while True:
            try:
                especie = input("Especie: ")
                color = input("Color:\t ")
                edad = int(input("Edad:\t "))
                tamaño = (input("Tamaño:\t "))
                nombre = input("Nombre de la mascota:\t ")
                raza = input("Raza:\t ")
                numero_chip = int(input("Numero de chip:\t "))
                mascota_nueva = Mascota(especie, color, edad, tamaño, raza, nombre, numero_chip)
                masc.agreagar_mascota(mascota_nueva)
            except ValueError:
                print("ingrese un valor correcto")
            break
    
    #Me muestra las mascota en la lista        
    elif opcion == "2":
        masc.mostar_mascotas()
        
    #Esta opcion seria eliminar mascota
    elif opcion == "3":
        try:
            eliminarchip = int(input("Ingrese el chip a adoptar: "))
            masc.eliminar_mascota(eliminarchip)
        except ValueError:
            print("ingrese un chip valido")
        
    elif opcion == "4":
        print("Gracias por adoptar un mishi")
        break