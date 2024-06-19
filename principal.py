from funciones import *

while True:
    print("MENÚ CONTACTOS")
    print("1. agregar contacto\n2.mostrar contactos\n3.guardar archivo CSV\n4.salir")
    opc=int(input("Ingrese opción: "))
    if opc==1:
       opcion_1()

    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3()
    elif opc==4:
        pass
    else:
        pass