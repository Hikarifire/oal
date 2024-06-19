import csv

contactos = []
def opcion_1():   
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese nombre: ")
    telefono = input ("Ingrese telefono: ")
    correo = input("Ingrese su correo: ")
    contacto = {"nombre":nombre, "telefono":telefono, "correo":correo}
    contactos.append(contacto)
    print("CONTACTO AGREGADO")
def opcion_2():
    if len(contactos)==0:
        print("No existen contactos, primero agregue alguno en la opción 1!")
    else:
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE": {c["nombre"]})
def opcion_3():
    pass

def opcion_4(): 
    pass