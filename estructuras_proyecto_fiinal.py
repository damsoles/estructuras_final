# Definimos la clase Tarea que representa una tarea individual
class Tarea:
    # Método inicializador, crea una nueva tarea con nombre, descripción y prioridad
    def __init__(self, nombre: str, descripcion: str, prioridad: str):
        # Verifica que el nombre y la descripción no estén vacíos
        if not nombre or not descripcion:
            raise ValueError("El nombre y la descripción no pueden estar vacíos.")
        # Valida que la prioridad sea correcta usando el método validar_prioridad
        if not self.validar_prioridad(prioridad):
            raise ValueError("La prioridad debe ser 'alta', 'media' o 'baja'.")

        # Asigna los atributos a la tarea
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    # Método para validar que la prioridad sea 'alta', 'media' o 'baja'
    def validar_prioridad(self, prioridad: str):
        return prioridad in ["alta", "media", "baja"]

    # Método para retornar una representación en texto de la tarea
    def __str__(self):
        return f"Tarea: {self.nombre} || Prioridad: {self.prioridad} \nDescripción: {self.descripcion}"


# Definimos la clase GestorTareas para gestionar una lista de tareas
class GestorTareas:
    # Inicializa el gestor, recibe el nombre del archivo y carga las tareas desde él
    def __init__(self, archivo: str):
        self.archivo = archivo  # Archivo donde se guardarán las tareas
        self.tareas = []  # Lista para almacenar las tareas
        self.cargar_de_archivo()  # Carga las tareas desde el archivo al iniciar

    # Método para agregar una nueva tarea y guardarla en el archivo
    def agregar_tarea(self, nombre: str, descripcion: str, prioridad: str):
        tarea = Tarea(nombre, descripcion, prioridad)  # Crea una nueva instancia de Tarea
        self.tareas.append(tarea)  # Agrega la tarea a la lista
        self.guardar_en_archivo()  # Guarda la lista actualizada en el archivo

    # Método para eliminar una tarea por su nombre y actualizar el archivo
    def eliminar_tarea(self, nombre: str):
        # Filtra las tareas dejando solo las que no coincidan con el nombre dado
        self.tareas = [tarea for tarea in self.tareas if tarea.nombre != nombre]
        self.guardar_en_archivo()  # Guarda la lista actualizada en el archivo

    # Método para procesar las tareas por prioridad y vaciar la lista al final
    def procesar_tareas(self):
        # Itera sobre las prioridades en orden de importancia
        for prioridad in ["alta", "media", "baja"]:
            for tarea in self.tareas:
                if tarea.prioridad == prioridad:
                    print(f"Procesando {tarea}")  # Muestra la tarea que se está procesando
        self.tareas.clear()  # Limpia la lista de tareas procesadas
        self.guardar_en_archivo()  # Guarda la lista vacía en el archivo

    # Método para mostrar todas las tareas en pantalla
    def mostrar_tareas(self):
        if not self.tareas:  # Si no hay tareas, muestra un mensaje
            print("No hay tareas pendientes.")
        else:
            for tarea in self.tareas:  # Itera y muestra cada tarea en la lista
                print(tarea)

    # Método para guardar la lista de tareas en el archivo
    def guardar_en_archivo(self):
        with open(self.archivo, 'w') as f:  # Abre el archivo en modo de escritura
            for tarea in self.tareas:
                # Escribe cada tarea en una línea en formato "nombre|descripción|prioridad"
                f.write(f"{tarea.nombre}|{tarea.descripcion}|{tarea.prioridad}\n")
        print("Tareas guardadas en el archivo.")  # Confirma que las tareas se guardaron

    # Método para cargar tareas desde el archivo al iniciar
    def cargar_de_archivo(self):
        try:
            with open(self.archivo, 'r') as f:  # Intenta abrir el archivo en modo de lectura
                for linea in f:
                    # Separa la línea en nombre, descripción y prioridad
                    nombre, descripcion, prioridad = linea.strip().split('|')
                    self.tareas.append(Tarea(nombre, descripcion, prioridad))  # Agrega la tarea a la lista
        except FileNotFoundError:
            # Si el archivo no existe, muestra un mensaje
            print("El archivo no existe. Asegúrate de agregar tareas primero.")
        except Exception as e:
            # Muestra cualquier error inesperado
            print(f"Se ha producido un error al cargar el archivo: {e}")

# Función del menú principal para interactuar con el usuario
def menu():
    gestor = GestorTareas('tareas.txt')  # Crea una instancia del gestor y especifica el archivo de tareas
    while True:
        # Muestra las opciones del menú
        print("\n--- Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Mostrar todas las tareas")
        print("4. Procesar todas las tareas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")  # Pide al usuario que elija una opción

        if opcion == '1':
            # Solicita datos para agregar una nueva tarea
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            prioridad = input("Prioridad (alta/media/baja): ")
            try:
                gestor.agregar_tarea(nombre, descripcion, prioridad)  # Intenta agregar la tarea
            except ValueError as e:
                print(e)  # Muestra el error si la validación falla

        elif opcion == '2':
            # Solicita el nombre de la tarea a eliminar
            nombre = input("Nombre de la tarea a eliminar: ")
            gestor.eliminar_tarea(nombre)  # Elimina la tarea del gestor

        elif opcion == '3':
            gestor.mostrar_tareas()  # Muestra todas las tareas

        elif opcion == '4':
            gestor.procesar_tareas()  # Procesa todas las tareas

        elif opcion == '5':
            print("Saliendo del programa.")
            break  # Sale del bucle y termina el programa

        else:
            print("Opción no válida.")  # Informa de una opción incorrecta

# Ejecuta el menú solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu()


