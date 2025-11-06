# stats.py
import os
import csv
import collections
from config import BASE_DIR
from persistence import recorrer_directorios
from utils import mostrar_lista_paises

def mostrar_estadisticas():
    datos = []
    conteo_por_continente = collections.Counter()
    suma_poblacion = 0

    for raiz, _, archivos in os.walk(BASE_DIR):
        for archivo in archivos:
            if not archivo.endswith(".csv"): continue
            ruta_csv = os.path.join(raiz, archivo)
            try:
                rel = os.path.relpath(ruta_csv, BASE_DIR)
                partes = rel.split(os.sep)
                continente = partes[0] if len(partes) >= 2 else "Desconocido"
            except Exception:
                continente = "Desconocido"
            try:
                with open(ruta_csv, "r", encoding="utf-8") as f:
                    lector = csv.DictReader(f)
                    for fila in lector:
                        try:
                            pobl = int(fila.get("poblacion", 0))
                            sup = int(fila.get("superficie", 0))
                            nombre = fila.get("nombre", "").strip()
                            if not nombre: continue
                            datos.append({"nombre": nombre, "poblacion": pobl, "superficie": sup, "continente": continente})
                            suma_poblacion += pobl
                            conteo_por_continente[continente] += 1
                        except ValueError:
                            print(f"Fila con datos inválidos en {ruta_csv}: {fila}")
            except (FileNotFoundError, OSError, csv.Error) as e:
                print(f"Error leyendo {ruta_csv}: {e}")

    total = len(datos)
    if total == 0:
        print("No hay datos para calcular estadísticas.")
        return

    mayor = max(datos, key=lambda x: x["poblacion"])
    menor = min(datos, key=lambda x: x["poblacion"])
    promedio = suma_poblacion / total

    print("Estadísticas globales")
    print(f"Cantidad total de ítems: {total}")
    print(f"Suma total de población: {suma_poblacion}")
    print(f"Promedio de población: {promedio:.2f}")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print("\nRecuento de ítems por continente (primer nivel):")
    for cont, cnt in conteo_por_continente.most_common():
        print(f"{cont}: {cnt}")

def ordenar_por_clave(clave):
    datos = recorrer_directorios(BASE_DIR)
    if not datos:
        print("No hay datos para ordenar.")
        return
    if clave not in ["nombre","poblacion","superficie"]:
        print("Clave inválida.")
        return
    ordenados = sorted(datos, key=lambda x: x[clave])
    mostrar_lista_paises(ordenados, titulo=f"Lista ordenada por {clave}")
