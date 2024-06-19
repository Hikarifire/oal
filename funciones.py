import csv

contactos = []
def opcion_1():   
    print("AGREGAR CONTACTO")
    nombre = input("Ingrese nombre: ")
    telefono = input ("Ingrese teléfono: ")
    correo = input("Ingrese su correo: ")
    contacto = {"nombre":nombre, "teléfono":telefono, "correo":correo}
    contactos.append(contacto)
    print("CONTACTO AGREGADO")
def opcion_2():
    if len(contactos)==0:
        print("No existen contactos, primero agregue alguno en la opción 1!")
    else:
        print("LISTA DE CONTACTOS")
        for c in contactos:
            print(f"NOMBRE: {c['nombre']}")
            print(f"TELÉFONO: {c['teléfono']}")
            print(f"CORREO: {c['correo']}\n")
def opcion_3():
    if len(contactos)==0:
        print("No existen contactos, primero agregue alguno en la opción 1!")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")
        with open(f"{nombre_archivo}.csv","w",newline="") as archivo:
            escritor = csv.DictWriter(archivo, ["nombre","Teléfono","Correo"])
            escritor.writeheader()
            escritor.writerows(contactos)
        print("ARCHIVO CREADO!")

def opcion_4(): 
    pass