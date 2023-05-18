import json

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
    print(separador())
    print("Bienvenid@ a nuestra plataforma 'π-thonicos'")
    print("1. Registrar un nuevo usuario")
    print("2. Mostrar usuarios registrados")
    if not sesion_iniciada:
        print("3. Iniciar sesión")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        usuario = input("Ingrese un nombre de usuario: ")
        contraseña = input("Ingrese una contraseña: ")
        email = input("Ingrese un correo electrónico: ")
        registrar_usuario(usuario, contraseña, email, base_de_datos)
        guardar_base_de_datos(base_de_datos)

    elif opcion == "2":
        mostrar_usuarios(base_de_datos)

    elif opcion == "3" and not sesion_iniciada:
        usuario = input("Ingrese su nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        sesion_iniciada = iniciar_sesion(usuario, contraseña, base_de_datos)

    elif opcion == "4":
        print(separador())
        print("Gracias por visitarnos. ¡Hasta luego, amig@ π-thonero! y no olvidés visitarnos pronto para ver nuestras novedades")
        break

    else:
        print(separador())
        print("Opción inválida. Por favor, seleccione un número del 1 al 4.")
