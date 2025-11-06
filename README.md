# 📦 Proyecto Catálogo de Países

CLI modular en Python para gestionar un catálogo jerárquico de países almacenado en CSV. Soporta alta, modificación, eliminación, lectura recursiva, filtrado, ordenamiento y estadísticas globales. Listo para commitear al repositorio.
Estructura de archivos

---

## 📁 Estructura de archivos
- `config.py` — constantes del proyecto (`BASE_DIR`, `ENCABEZADO`)
- `utils.py` — presentación (`mostrar_pais`, `mostrar_lista_paises`)
- `persistence.py` — E/S: recorrido recursivo, lectura/escritura de CSV, helpers
- `crud.py` — operaciones CRUD: `alta_item`, `modificar_item`, `eliminar_item`, `sobrescribir_item`
- `stats.py` — estadísticas globales y ordenamiento
- `main.py` — entrypoint y menú interactivo
- `data/` — carpeta creada automáticamente en tiempo de ejecución donde se guardan subcarpetas y archivos CSV

## ⚙️ Requisitos

- Python **3.10+** (uso de `match/case`)
- Solo módulos estándar: `os`, `csv`, `collections`

---

Instalación y ejecución
- Clona o copia los archivos al mismo directorio del proyecto.
- Abre una terminal en esa carpeta.
- Ejecuta:

 ---
```bash
python main.py
 - El programa creará la carpeta data/ automáticamente si no existe.

- Menú y funcionalidades

- Al ejecutar verás el menú:

1 - Alta de ítem  
2 - Modificar ítem  
3 - Eliminar ítem  
4 - Mostrar estadísticas  
5 - Ordenar por clave  
6 - Mostrar todos los ítems  
7 - Filtrar ítems  
8 - Salir

```

# Comportamiento clave:

- -->Alta: obliga a completar Continente, Región, Tipo de gobierno, Nombre (no vacíos), Población y Superficie (enteros > 0).

- -->Modificar / Eliminar: identificación por nombre exacto (case-insensitive). Al modificar se sobrescribe únicamente el CSV que contiene el ítem.

- -->Lectura global: función recursiva que consolida todos los CSV en memoria como lista de diccionarios.

- -->Formato de salida legible: "Nombre | Población: X | Superficie: Y".

- -->Ordenamiento: disponible por nombre, poblacion, superficie.

- -->Filtrado: búsqueda exacta case-insensitive por cualquiera de esas claves.

- -->Estadísticas: cantidad total, suma y promedio de población, país con mayor/menor población, recuento por continente (primer nivel extraído desde la jerarquía de carpetas).
```
Estructura en disco (ejemplo):
data/ 
├─ América/ 
│ ├─ Sur/ 
│ │ ├─ Democracia/ 
│ │ │ └─ catalogo.csv 
│ └─ Norte/ 
└─ Europa/ 
└─ ...
```

# Cada catalogo.csv tiene encabezado: nombre,poblacion,superficie
# Robustez y consideraciones
- I/O protegido con try/except en persistence.py y funciones relacionadas.

- Al modificar o eliminar, solo se reescribe el CSV hoja correspondiente (modo "w").

- Filas con datos numéricos inválidos son notificadas y saltadas para evitar corrupción.

- Si querés soporte para Python <3.10, reemplaza match/case por if/elif en main.py..

# Personalización rápida
- Cambiar ruta de datos: editar BASE_DIR en config.py.

- Añadir campos: actualizar ENCABEZADO en config.py y adaptar persistence/crud/utils.

- Convertir a paquete: mover a subcarpeta, agregar __init__.py y usar imports relativos.

# Ejemplo de flujo rápido
Alta:
- -->Continente: América
- -->Región: Sur
- -->Tipo de gobierno: Democracia
- -->Nombre del país: Argentina
- -->Población: 45000000
- -->Superficie: 2780400
- -->Mostrar todos: Argentina | Población: 45000000 | Superficie: 2780400

# Estadísticas:
- -->Cantidad total de ítems: 1
- -->Suma total de población: 45000000
- -->Promedio de población: 45000000.00
- -->País con mayor población: Argentina (45000000)
- -->País con menor población: Argentina (45000000)
- -->Recuento por continente: América: 1


# Troubleshooting rápido
- -->ModuleNotFoundError: ejecuta python main.py desde la carpeta que contiene los .py.
- -->Permisos: asegúrate de tener permisos de escritura donde se crea data/.
- -->CSV bloqueado por otra app: cierra editores que tengan abiertos los CSV.

  # VIDEO

  https://www.youtube.com/watch?v=mndvSDk663k

