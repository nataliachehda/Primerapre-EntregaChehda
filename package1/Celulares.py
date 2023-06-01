from package1 import Cliente
from package1.Cliente import Cliente

class Celulares:
    def __init__(self, marca, nombre, precio):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"{self.marca} - {self.nombre} - ${self.precio}"

    def comprar(self, cliente, base_de_datos):
        if not cliente.iniciar_sesion(base_de_datos):
            return

        celulares_disponibles = [
            Celulares("Iphone", "12 Pro Max", 75000),
            Celulares("Motorola", "E32", 65000),
            Celulares("Samsung", "Galaxy A14", 80000),
            Celulares("LG", "K22", 50000),
            Celulares("Xiaomi", "Redmi Note 11 (Snapdragon)", 105000)
        ]
        
        celulares_elegidos = []
        
        # Mostrar el menú de celulares disponibles
        print("Seleccione los celulares que desea comprar:")
        for i, celular in enumerate(celulares_disponibles, 1):
            print(f"{i}. {celular}")
        
        # Pedir al usuario que elija los celulares
        while True:
            opcion = input("Ingrese el número del celular que desea agregar >(0 PARA FINALIZAR)< : ")
            if opcion == "0":
                break
            elif opcion.isdigit() and 1 <= int(opcion) <= len(celulares_disponibles):
                celular_elegido = celulares_disponibles[int(opcion) - 1]
                celulares_elegidos.append(celular_elegido)
                print(f"¡El celular '{celular_elegido.marca} - {celular_elegido.nombre}' ha sido agregado a su compra!")
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
        
        # Mostrar el resumen de la compra
        if celulares_elegidos:
            print("\nResumen de la compra:")
            total = 0
            for celular in celulares_elegidos:
                print(f"{celular.marca} - {celular.nombre} - ${celular.precio}")
                total += celular.precio
            print(f"\nTotal: ${total}")
            print("Orden de Compra:")
            print(f"Cliente: {cliente.nombre}")
            print(f"Email: {cliente.email}")
            print(f"Dirección: {cliente.direccion}")
            print("¡La orden de compra será enviada a su email para ser abonada!")
        else:
            print("No se han seleccionado celulares. La compra ha sido cancelada.")
        
        input("Presione Enter para continuar...")