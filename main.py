import json
import os
from package1 import Cliente
from package1.Cliente import Cliente
from package1.Cliente import base_de_datos
from package1 import Celulares
from package1.Celulares import Celulares

cliente = None 

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
        print("Opción inválida. Por favor, seleccione un número válido.")
        input("Presione Enter para continuar...")