ARCHIVO_DATASET = "spotify_pequeno.csv"

def cargar_datos(ruta):
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

    encabezados = [h.strip() for h in lineas[0].split(",")]

    for numero, linea in enumerate(lineas[1:], start=2):
        linea = linea.strip()
        if not linea:          # saltar filas vacías
            continue
        valores = linea.split(",")
       
        if len(valores) < len(encabezados):
            continue
        cancion = {}
        for i, clave in enumerate(encabezados):
            cancion[clave] = valores[i].strip()
        canciones.append(cancion)

    return canciones


def buscar_por_termino(canciones, termino):
 
    termino_lower = termino.lower()
    resultados = []
    for c in canciones:
        for valor in c.values():
            if termino_lower in valor.lower():
                resultados.append(c)
                break  
    return resultados


def estadisticas_campo(canciones, campo):
   
    valores = []
    for c in canciones:
        if campo not in c:
            continue
        texto = c[campo].strip()
        # intentar convertir a float sin usar librerías externas
        try:
            valores.append(float(texto))
        except ValueError:
            pass   

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

    conteo = {}
    for c in canciones:
        if campo not in c:
            continue
        clave = c[campo].strip()
        if clave == "":
            continue
        conteo[clave] = conteo.get(clave, 0) + 1

    items = list(conteo.items())
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[j][1] > items[i][1]:
                items[i], items[j] = items[j], items[i]
    return items

def imprimir_cancion(cancion, encabezados):
    
    partes = []
    for clave in encabezados:
        if clave in cancion:
            partes.append(f"{clave}: {cancion[clave]}")
    print("  " + " | ".join(partes))


def obtener_encabezados(canciones):
  
    if not canciones:
        return []
    return list(canciones[0].keys())


def listar_campos_numericos(canciones):
    
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
    
    if not canciones:
        return []
    todos = list(canciones[0].keys())
    numericos = set(listar_campos_numericos(canciones))
    return [c for c in todos if c not in numericos]


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
    for c in resultados[:20]:       
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
        barra = "█" * min(conteo, 40)   
        print(f"  {valor:<25} {conteo:>4}  {barra}")

def opcion_preview(canciones, encabezados):
    print(f"\n  Primeras 10 canciones del dataset:\n")
    for c in canciones[:10]:
        imprimir_cancion(c, encabezados)

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
