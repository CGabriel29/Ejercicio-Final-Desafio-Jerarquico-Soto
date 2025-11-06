# crud.py
import os
from config import BASE_DIR, ENCABEZADO
from persistence import escribir_csv_append, recorrer_directorios, leer_csv_como_lista, sobrescribir_csv
from utils import mostrar_pais

def alta_item():
    print("Alta de nuevo ítem")
    # validaciones fuertes por campo
    while True:
        continente = input("Continente: ").strip().capitalize()
        if continente: break
        print("El campo Continente no puede quedar vacío.")

    while True:
        region = input("Región: ").strip().capitalize()
        if region: break
        print("El campo Región no puede quedar vacío.")

    while True:
        gobierno = input("Tipo de gobierno: ").strip().capitalize()
        if gobierno: break
        print("El campo Tipo de gobierno no puede quedar vacío.")

    while True:
        nombre = input("Nombre del país: ").strip().capitalize()
        if nombre: break
        print("El campo Nombre no puede quedar vacío.")

    while True:
        try:
            poblacion = int(input("Población: "))
            if poblacion > 0: break
            print("La población debe ser un número positivo mayor a cero.")
        except ValueError:
            print("Debés ingresar un número entero válido.")

    while True:
        try:
            superficie = int(input("Superficie: "))
            if superficie > 0: break
            print("La superficie debe ser un número positivo mayor a cero.")
        except ValueError:
            print("Debés ingresar un número entero válido.")

    ruta = os.path.join(BASE_DIR, continente, region, gobierno)
    os.makedirs(ruta, exist_ok=True)
    archivo_csv = os.path.join(ruta, "catalogo.csv")
    nuevo = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie}
    if escribir_csv_append(archivo_csv, nuevo):
        print("Ítem agregado correctamente.")

def modificar_item(nombre_busqueda):
    datos = recorrer_directorios(BASE_DIR)
    for pais in datos:
        if pais["nombre"].lower() == nombre_busqueda.lower():
            print("Nombre del país a modificar:")
            mostrar_pais(pais)
            campo = input("¿Qué campo desea modificar? (poblacion/superficie): ").lower()
            if campo not in ["poblacion", "superficie"]:
                print("Campo no válido.")
                return
            while True:
                try:
                    nuevo_valor = int(input(f"Nuevo valor para {campo}: "))
                    if nuevo_valor > 0:
                        pais[campo] = nuevo_valor
                        sobrescribir_item(pais)
                        print("Modificación exitosa.")
                        return
                    print("Debe ser un número positivo mayor a cero.")
                except ValueError:
                    print("Debés ingresar un número entero válido.")
    print("País no encontrado.")

def sobrescribir_item(item_modificado):
    # Recorre archivos CSV hasta encontrar el item y sobrescribe solo ese CSV
    for raiz, _, archivos in os.walk(BASE_DIR):
        for archivo in archivos:
            if not archivo.endswith(".csv"):
                continue
            ruta_csv = os.path.join(raiz, archivo)
            lector = leer_csv_como_lista(ruta_csv)
            if lector is None:
                continue
            actualizado = False
            for fila in lector:
                if fila.get("nombre","").lower() == item_modificado["nombre"].lower():
                    fila["poblacion"] = str(item_modificado["poblacion"])
                    fila["superficie"] = str(item_modificado["superficie"])
                    actualizado = True
            if actualizado:
                sobrescribir_csv(ruta_csv, lector)
                return

def eliminar_item(nombre_busqueda):
    """Elimina un ítem por nombre con manejo de excepciones y sobrescribe solo el CSV hoja."""
    for raiz, _, archivos in os.walk(BASE_DIR):
        for archivo in archivos:
            if not archivo.endswith(".csv"): continue
            ruta_csv = os.path.join(raiz, archivo)
            lector = leer_csv_como_lista(ruta_csv)
            if lector is None: continue
            nueva_lista = [fila for fila in lector if fila.get("nombre","").lower() != nombre_busqueda.lower()]
            if len(nueva_lista) < len(lector):
                if sobrescribir_csv(ruta_csv, nueva_lista):
                    print("Ítem eliminado.")
                else:
                    print("Error al guardar cambios tras eliminación.")
                return
    print("País no encontrado.")
