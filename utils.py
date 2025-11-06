# utils.py
def mostrar_pais(item):
    """Imprime un país en formato legible."""
    print(f"- {item['nombre']} | Población: {item['poblacion']} | Superficie: {item['superficie']}")

def mostrar_lista_paises(paises, titulo=None):
    """Imprime una lista de países con formato legible y un título opcional."""
    if titulo:
        print(titulo)
    if not paises:
        print("No hay datos para mostrar.")
        return
    for p in paises:
        mostrar_pais(p)
