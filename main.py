# main.py
from config import BASE_DIR
from persistence import asegurar_base_dir
from crud import alta_item, modificar_item, eliminar_item
from stats import mostrar_estadisticas, ordenar_por_clave
from persistence import recorrer_directorios
from utils import mostrar_lista_paises
from crud import sobrescribir_item, eliminar_item as eliminar_item_crud
from persistence import recorrer_directorios

def mostrar_menu():
    print("""
========= MENÚ =========
1 - Alta de ítem
2 - Modificar ítem
3 - Eliminar ítem
4 - Mostrar estadísticas
5 - Ordenar por clave
6 - Mostrar todos los ítems
7 - Filtrar ítems
8 - Salir
========================
""")

def filtrar_items_menu():
    from crud import recorrer_directorios as rdir 
    clave = input("Filtrar por (nombre/poblacion/superficie): ").strip().lower()
    valor = input("Valor a buscar: ").strip()
    # import dinámico para usar la función de stats o implementada en otro módulo
    from stats import ordenar_por_clave, mostrar_estadisticas
    from persistence import recorrer_directorios
    datos = recorrer_directorios(BASE_DIR)
    if clave not in ["nombre","poblacion","superficie"]:
        print("Clave inválida.")
        return
    filtrados = [d for d in datos if str(d[clave]).lower() == valor.lower()]
    from utils import mostrar_lista_paises
    mostrar_lista_paises(filtrados, titulo=f"Filtrado por {clave} = {valor}")

def main():
    asegurar_base_dir()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                alta_item()
            case "2":
                nombre = input("Nombre de país a modificar: ").strip()
                modificar_item(nombre)
            case "3":
                nombre = input("Nombre de país a eliminar: ").strip()
                eliminar_item(nombre)
            case "4":
                mostrar_estadisticas()
            case "5":
                clave = input("Ordenar por (nombre/poblacion/superficie): ").strip().lower()
                ordenar_por_clave(clave)
            case "6":
                todos = recorrer_directorios(BASE_DIR)
                from utils import mostrar_lista_paises
                mostrar_lista_paises(todos, titulo="Ítems totales")
            case "7":
                filtrar_items_menu()
            case "8":
                print("Saliendo del sistema.")
                break
            case _:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
