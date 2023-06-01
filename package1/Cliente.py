import json

class Cliente:
    def __init__(self, nombre, usuario, password, email, direccion):
        self.nombre = nombre
        self.usuario = usuario
        self.password = password
        self.email = email
        self.direccion = direccion

    def registrarse(self, base_de_datos):
        if self.usuario not in base_de_datos:
            base_de_datos[self.usuario] = {
                "nombre": self.nombre,
                "usuario": self.usuario,
                "password": self.password,
                "email": self.email,
                "direccion": self.direccion
            }
            print(f"¡El usuario {self.usuario} ha sido registrado correctamente!")
            return self.nombre, self.email, self.direccion 
        else:
            print(f"El usuario {self.usuario} ya existe en la base de datos.")
            return None, None, None
    def mostrar_datos (self, nombre, email, direccion):
        return self.nombre, self.email, self.direccion

    def iniciar_sesion(self, base_de_datos):
        if self.usuario in base_de_datos and base_de_datos[self.usuario]["password"] == self.password:
            print(f"¡Bienvenid@ a CeluWorld, {self.usuario}! Los mejores celulares para vos😎")
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            return False

# Cargar la base de datos desde un archivo JSON
def cargar_base_de_datos():
    try:
        with open("./base_de_datos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

# Guardar en el JSON
def guardar_base_de_datos(base_de_datos):
    with open("./base_de_datos.json", "w") as archivo:
        json.dump(base_de_datos, archivo)

base_de_datos = cargar_base_de_datos()