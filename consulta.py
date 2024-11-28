import requests

# URL de la API
url = "https://api-test-2-vnx1.onrender.com/" 

# Función para realizar la solicitud GET
def get_estudiantes():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\nLista de estudiantes:")
        for estudiante in data:
            print(f"No Control: {estudiante['no_control']}, Nombre: {estudiante['nombre']} {estudiante['ap_paterno']} {estudiante['ap_materno']}, Semestre: {estudiante['semestre']}")
    else:
        print(f"Error al hacer GET. Código de estado: {response.status_code}")

# Función para realizar la solicitud POST
def post_estudiante():
    print("\nIngresar datos del nuevo estudiante:")
    no_control = input("Número de control: ")
    nombre = input("Nombre: ")
    ap_paterno = input("Apellido paterno: ")
    ap_materno = input("Apellido materno: ")
    semestre = input("Semestre: ")
    
    estudiante = {
        "no_control": no_control,
        "nombre": nombre,
        "ap_paterno": ap_paterno,
        "ap_materno": ap_materno,
        "semestre": semestre
    }

    response = requests.post(url, json=estudiante)
    if response.status_code == 201:
        print("Estudiante creado exitosamente.")
        print(f"No Control: {estudiante['no_control']}, Nombre: {estudiante['nombre']} {estudiante['ap_paterno']} {estudiante['ap_materno']}, Semestre: {estudiante['semestre']}")
    else:
        print(f"Error al hacer POST. Código de estado: {response.status_code}")

# Función para realizar la solicitud PUT
def put_estudiante():
    id_estudiante = input("\nNúmero de control del estudiante a actualizar: ")
    nombre = input("Nuevo nombre: ")
    ap_paterno = input("Nuevo apellido paterno: ")
    ap_materno = input("Nuevo apellido materno: ")
    semestre = input("Nuevo semestre: ")
    
    estudiante = {
        "nombre": nombre,
        "ap_paterno": ap_paterno,
        "ap_materno": ap_materno,
        "semestre": semestre
    }

    response = requests.put(f"{url}/{id_estudiante}", json=estudiante)
    if response.status_code == 200:
        print("Estudiante actualizado exitosamente.")
        print(f"Num Control: {id_estudiante}, Nombre: {estudiante['nombre']} {estudiante['ap_paterno']} {estudiante['ap_materno']}, Semestre: {estudiante['semestre']}")
    else:
        print(f"Error al hacer PUT. Código de estado: {response.status_code}")

# Función para realizar la solicitud PATCH
def patch_estudiante():
    id_estudiante = input("\nNúmero de control del estudiante a modificar: ")
    campo = input("Campo a modificar (nombre/ap_paterno/ap_materno/semsst): ")
    valor = input(f"Nuevo valor para {campo}: ")
    
    estudiante = {campo: valor}

    response = requests.patch(f"{url}/{id_estudiante}", json=estudiante)
    if response.status_code == 200:
        print("Estudiante modificado exitosamente.")
        print(f"Num Control: {id_estudiante}, {campo} actualizado a: {valor}")
    else:
        print(f"Error al hacer PATCH. Código de estado: {response.status_code}")

# Función para realizar la solicitud DELETE
def delete_estudiante():
    id_estudiante = input("\nNúmero de control del estudiante a eliminar: ")
    
    response = requests.delete(f"{url}/{id_estudiante}")
    if response.status_code == 200:
        print("Estudiante eliminado exitosamente.")
    else:
        print(f"Error al hacer DELETE. Código de estado: {response.status_code}")

# Menú para seleccionar la solicitud
def menu():
    while True:
        print("\n--- Menú de solicitudes ---")
        print("1. GET - Consultar estudiantes")
        print("2. POST - Agregar nuevo estudiante")
        print("3. PUT - Actualizar estudiante")
        print("4. PATCH - Modificar estudiante")
        print("5. DELETE - Eliminar estudiante")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            get_estudiantes()
        elif opcion == "2":
            post_estudiante()
        elif opcion == "3":
            put_estudiante()
        elif opcion == "4":
            patch_estudiante()
        elif opcion == "5":
            delete_estudiante()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, por favor selecciona una opción válida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()