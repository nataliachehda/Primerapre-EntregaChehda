import json
import os
from package1 import Cliente
from package1.Cliente import Cliente
from package1.Cliente import base_de_datos
from package1 import Celulares
from package1.Celulares import Celulares

# Pongo una línea separadora para que sea fácil de entender visualmente, porque el while repite el menú
def separador():
    return "_________________________________________"

# Registrar un nuevo usuario o avisar si ya existe
def registrar_usuario(usuario, contraseña, email, base_de_datos):
    print(separador())
    if usuario not in base_de_datos:
        base_de_datos[usuario] = {"contraseña": contraseña, "email": email}
        print(f"¡El usuario {usuario} ha sido registrado correctamente!")
    else:
        print(f"El usuario {usuario} ya existe en la base de datos.")

# Mostrar los usuarios registrados (solo el usuario e email)
def mostrar_usuarios(base_de_datos):
    print(separador())
    print("Usuarios registrados:")
    for usuario, datos in base_de_datos.items():
        print(f" - Usuario: {usuario}, Email: {datos['email']}")
    print(separador())

# Función para inicio de sesión (hago el return true o false para luego hacer el control del inicio de sesión en la función sesion_iniciada)
def iniciar_sesion(usuario, contraseña, base_de_datos):
    if usuario in base_de_datos and base_de_datos[usuario]["contraseña"] == contraseña:
        print(separador())
        print(f"¡Bienvenid@ a π-thonicos, {usuario}! Pronto tendremos novedades para vos😎")
        return True
    else:
        print(separador())
        print("Usuario o contraseña incorrectos.")
        return False

# Cargar la base de datos desde un archivo JSON
def cargar_base_de_datos():
    try:
        with open("base_de_datos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Guardo en el JSON
def guardar_base_de_datos(base_de_datos):
    with open("base_de_datos.json", "w") as archivo:
        json.dump(base_de_datos, archivo)

base_de_datos = cargar_base_de_datos()

# Controlo el estado de inicio de sesión, para que si ya lo hizo no vuelva a pedir
sesion_iniciada = False

# Menú principal del programa
while True:
    os.system("cls")
    print("Bienvenid@ a CeluWorld. Si desea realizar una compra, inicie sesión")
    print("1. Registrar un nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Comprar")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese su nombre completo: ")
        usuario = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        email = input("Ingrese un correo electrónico: ")
        direccion = input("Ingrese su dirección (calle, número, ciudad): ")
        os.system("cls")
        cliente = Cliente(nombre, usuario, password, email, direccion)
        cliente.registrarse(base_de_datos)
        guardar_base_de_datos(base_de_datos)

        
    elif opcion == "2":        
        usuario = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        os.system("cls")
        cliente = Cliente("", usuario, password, "", "")
        cliente.iniciar_sesion(base_de_datos)
        input("Presione Enter para continuar...")

    elif opcion == "3":
        if cliente is None:
            print("Por favor, inicie sesión antes de realizar una compra.")
            input("Presione Enter para continuar...")
        else:
            celulares = Celulares("", "", 0)
            celulares.comprar(cliente, base_de_datos)

    elif opcion == "4":
        print("Gracias por visitarnos. Recuerda volver para conocer nuestras últimas novedades.")
        break

    else:
        print(separador())
        print("Opción inválida. Por favor, seleccione un número del 1 al 4.")
