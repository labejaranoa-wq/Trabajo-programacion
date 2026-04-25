# main.py
# DataLab - Entrega 1: Explorador
# Dataset: Predicción de popularidad de canciones en Spotify

ARCHIVO_DATASET = "spotify_pequeno.csv"


# ──────────────────────────────────────────
#  Carga del dataset
# ──────────────────────────────────────────

def cargar_datos(ruta):
    """
    Lee el archivo CSV línea por línea con open() y split().
    Devuelve una lista de diccionarios, uno por canción.
    """
    canciones = []
    try:
        with open(ruta, encoding="utf-8") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(f"\n  ERROR: no se encontró el archivo '{ruta}'.")
        print("  Asegurate de que esté en la misma carpeta que main.py.\n")
        return []

    if not lineas:
        print("  El archivo está vacío.")
        return []

    # Primera línea = encabezados
    encabezados = [h.strip() for h in lineas[0].split(",")]

    for numero, linea in enumerate(lineas[1:], start=2):
        linea = linea.strip()
        if not linea:          # saltar filas vacías
            continue
        valores = linea.split(",")
        # Si hay más comas que columnas (p.ej. nombre con coma) se trunca al nro de encabezados
        if len(valores) < len(encabezados):
            continue
        cancion = {}
        for i, clave in enumerate(encabezados):
            cancion[clave] = valores[i].strip()
        canciones.append(cancion)

    return canciones


# ──────────────────────────────────────────
#  Funciones de análisis
# ──────────────────────────────────────────

def buscar_por_termino(canciones, termino):
    """
    Recorre todas las canciones y devuelve las que contienen
    el término en cualquiera de sus campos (búsqueda case-insensitive).
    """
    termino_lower = termino.lower()
    resultados = []
    for c in canciones:
        for valor in c.values():
            if termino_lower in valor.lower():
                resultados.append(c)
                break   # no agregar la misma canción dos veces
    return resultados


def estadisticas_campo(canciones, campo):
    """
    Calcula máximo, mínimo y promedio de un campo numérico.
    Devuelve un diccionario con los tres valores, o None si el campo no existe
    o no tiene datos numéricos.
    """
    valores = []
    for c in canciones:
        if campo not in c:
            continue
        texto = c[campo].strip()
        # intentar convertir a float sin usar librerías externas
        try:
            valores.append(float(texto))
        except ValueError:
            pass   # ignorar celdas no numéricas

    if not valores:
        return None

    maximo  = valores[0]
    minimo  = valores[0]
    suma    = 0.0
    for v in valores:
        if v > maximo:
            maximo = v
        if v < minimo:
            minimo = v
        suma += v

    promedio = suma / len(valores)
    return {"maximo": maximo, "minimo": minimo, "promedio": promedio, "total": len(valores)}


def filtrar_por_valor(canciones, campo, umbral):
    """
    Devuelve las canciones donde el campo numérico es mayor al umbral dado.
    """
    resultados = []
    for c in canciones:
        if campo not in c:
            continue
        try:
            if float(c[campo]) > umbral:
                resultados.append(c)
        except ValueError:
            pass
    return resultados


def agrupar_por_categoria(canciones, campo):
    """
    Cuenta cuántas canciones hay por cada valor distinto del campo de texto.
    Devuelve una lista de tuplas (valor, conteo) ordenada de mayor a menor.
    """
    conteo = {}
    for c in canciones:
        if campo not in c:
            continue
        clave = c[campo].strip()
        if clave == "":
            continue
        conteo[clave] = conteo.get(clave, 0) + 1

    # ordenar de mayor a menor sin sorted() con key lambda —
    # usamos burbuja para no depender de funciones avanzadas
    items = list(conteo.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]
    return items


# ──────────────────────────────────────────
#  Utilidades de impresión
# ──────────────────────────────────────────

def imprimir_cancion(cancion, encabezados):
    """Muestra una canción de forma legible en consola."""
    partes = []
    for clave in encabezados:
        if clave in cancion:
            partes.append(f"{clave}: {cancion[clave]}")
    print("  " + " | ".join(partes))


def obtener_encabezados(canciones):
    """Devuelve los encabezados del dataset (claves del primer registro)."""
    if not canciones:
        return []
    return list(canciones[0].keys())


def listar_campos_numericos(canciones):
    """Detecta qué campos parecen numéricos revisando el primer registro."""
    numericos = []
    if not canciones:
        return numericos
    for clave, valor in canciones[0].items():
        try:
            float(valor)
            numericos.append(clave)
        except ValueError:
            pass
    return numericos


def listar_campos_texto(canciones):
    """Detecta campos de texto (los que no son numéricos)."""
    if not canciones:
        return []
    todos = list(canciones[0].keys())
    numericos = set(listar_campos_numericos(canciones))
    return [c for c in todos if c not in numericos]


# ──────────────────────────────────────────
#  Menú principal
# ──────────────────────────────────────────

def mostrar_menu():
    print("\n" + "─" * 45)
    print("  DataLab  ·  Spotify Popularity Explorer")
    print("─" * 45)
    print("  1. Buscar canciones por término")
    print("  2. Estadísticas de un campo numérico")
    print("  3. Filtrar por valor numérico")
    print("  4. Agrupar por categoría")
    print("  5. Mostrar primeras 10 canciones")
    print("  6. Salir")
    print("─" * 45)


def opcion_buscar(canciones, encabezados):
    termino = input("\n  Ingresa el término a buscar: ").strip()
    if not termino:
        print("  No ingresaste nada.")
        return
    resultados = buscar_por_termino(canciones, termino)
    print(f"\n  Se encontraron {len(resultados)} registros para '{termino}':\n")
    for c in resultados[:20]:       # mostrar máximo 20 para no saturar la consola
        imprimir_cancion(c, encabezados)
    if len(resultados) > 20:
        print(f"\n  ... y {len(resultados) - 20} más.")


def opcion_estadisticas(canciones):
    campos = listar_campos_numericos(canciones)
    if not campos:
        print("\n  No se detectaron campos numéricos en el dataset.")
        return
    print("\n  Campos numéricos disponibles:")
    for i, c in enumerate(campos, 1):
        print(f"    {i}. {c}")
    campo = input("\n  Escribe el nombre del campo: ").strip()
    if campo not in campos:
        print(f"  '{campo}' no es un campo numérico reconocido.")
        return
    stats = estadisticas_campo(canciones, campo)
    if stats is None:
        print("  No se pudieron calcular estadísticas.")
        return
    print(f"\n  Campo: {campo}  ({stats['total']} registros)")
    print(f"    Máximo : {stats['maximo']:.2f}")
    print(f"    Mínimo : {stats['minimo']:.2f}")
    print(f"    Promedio: {stats['promedio']:.2f}")


def opcion_filtrar(canciones, encabezados):
    campos = listar_campos_numericos(canciones)
    if not campos:
        print("\n  No hay campos numéricos disponibles.")
        return
    print("\n  Campos numéricos disponibles:", ", ".join(campos))
    campo = input("  Campo a filtrar: ").strip()
    if campo not in campos:
        print(f"  '{campo}' no es válido.")
        return
    try:
        umbral = float(input(f"  Mostrar canciones con {campo} mayor a: "))
    except ValueError:
        print("  Valor no numérico.")
        return
    resultados = filtrar_por_valor(canciones, campo, umbral)
    print(f"\n  {len(resultados)} canciones con {campo} > {umbral}:\n")
    for c in resultados[:20]:
        imprimir_cancion(c, encabezados)
    if len(resultados) > 20:
        print(f"\n  ... y {len(resultados) - 20} más.")


def opcion_agrupar(canciones):
    campos = listar_campos_texto(canciones)
    if not campos:
        print("\n  No hay campos de texto disponibles.")
        return
    print("\n  Campos de texto disponibles:", ", ".join(campos))
    campo = input("  Campo para agrupar: ").strip()
    if campo not in campos:
        print(f"  '{campo}' no es válido.")
        return
    grupos = agrupar_por_categoria(canciones, campo)
    print(f"\n  Distribución por '{campo}':\n")
    for valor, conteo in grupos:
        barra = "█" * min(conteo, 40)   # barra visual proporcional
        print(f"  {valor:<25} {conteo:>4}  {barra}")


def opcion_preview(canciones, encabezados):
    print(f"\n  Primeras 10 canciones del dataset:\n")
    for c in canciones[:10]:
        imprimir_cancion(c, encabezados)


# ──────────────────────────────────────────
#  Punto de entrada
# ──────────────────────────────────────────

def main():
    print("\n  Cargando dataset...")
    canciones = cargar_datos(ARCHIVO_DATASET)
    if not canciones:
        return

    encabezados = obtener_encabezados(canciones)
    print(f"  Dataset cargado: {len(canciones)} canciones, {len(encabezados)} columnas.")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción (1-6): ").strip()

        if opcion == "1":
            opcion_buscar(canciones, encabezados)
        elif opcion == "2":
            opcion_estadisticas(canciones)
        elif opcion == "3":
            opcion_filtrar(canciones, encabezados)
        elif opcion == "4":
            opcion_agrupar(canciones)
        elif opcion == "5":
            opcion_preview(canciones, encabezados)
        elif opcion == "6":
            print("\n  Hasta luego!\n")
            break
        else:
            print("\n  Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
