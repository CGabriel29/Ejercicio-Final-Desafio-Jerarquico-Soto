# persistence.py
import os
import csv
from config import BASE_DIR, ENCABEZADO

def asegurar_base_dir():
    os.makedirs(BASE_DIR, exist_ok=True)

def recorrer_directorios(ruta):
    """Recorre la jerarquía y devuelve lista de dicts con campos convertidos a int donde corresponde."""
    datos = []
    try:
        for elemento in os.listdir(ruta):
            ruta_completa = os.path.join(ruta, elemento)
            if os.path.isdir(ruta_completa):
                datos.extend(recorrer_directorios(ruta_completa))
            elif elemento.endswith(".csv"):
                try:
                    with open(ruta_completa, "r", encoding="utf-8") as archivo:
                        lector = csv.DictReader(archivo)
                        for fila in lector:
                            try:
                                fila["poblacion"] = int(fila.get("poblacion", 0))
                                fila["superficie"] = int(fila.get("superficie", 0))
                                datos.append(fila)
                            except ValueError:
                                print(f"Fila con datos numéricos inválidos en {ruta_completa}: {fila}")
                except (FileNotFoundError, OSError, csv.Error) as e:
                    print(f"Error leyendo {ruta_completa}: {e}")
    except FileNotFoundError:
        print(f"Carpeta no encontrada: {ruta}")
    return datos

def escribir_csv_append(ruta_csv, fila):
    archivo_existe = os.path.exists(ruta_csv)
    try:
        with open(ruta_csv, "a", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=ENCABEZADO)
            if not archivo_existe:
                escritor.writeheader()
            escritor.writerow(fila)
        return True
    except (OSError, csv.Error) as e:
        print(f"Error escribiendo {ruta_csv}: {e}")
        return False

def leer_csv_como_lista(ruta_csv):
    try:
        with open(ruta_csv, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except (FileNotFoundError, OSError, csv.Error) as e:
        print(f"Error leyendo {ruta_csv}: {e}")
        return None

def sobrescribir_csv(ruta_csv, filas):
    try:
        with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=ENCABEZADO)
            escritor.writeheader()
            escritor.writerows(filas)
        return True
    except (OSError, csv.Error) as e:
        print(f"Error escribiendo {ruta_csv}: {e}")
        return False
