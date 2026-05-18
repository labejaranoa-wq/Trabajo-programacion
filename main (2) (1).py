import archivos
import analisis

def imprimir_cancion(cancion, encabezados):
    partes = [f"{clave}: {cancion.get(clave, '')}" for clave in encabezados if clave in cancion]
    print("  " + " | ".join(partes))

def preguntar_guardado(resultados):
    if not resultados: return
    opcion = input("\n  ¿Deseas guardar estos resultados para usarlos después? (s/n): ").strip().lower()
    if opcion == 's':
        ruta = input("  Nombre del archivo (ej. resultados.csv): ").strip()
        if not ruta.endswith('.csv'): ruta += '.csv'
        archivos.guardar_resultados_csv(ruta, resultados)

def mostrar_menu():
    print("\n" + "─" * 50)
    print("  DataLab  ·  Spotify Analyzer (Entrega 2)")
    print("─" * 50)
    print("  1. Buscar canciones por término")
    print("  2. Estadísticas de un campo numérico")
    print("  3. Filtrar por valor numérico")
    print("  4. Agrupar por categoría")
    print("  5. Comparar dos grupos (Nuevo)")
    print("  6. Ver historial de consultas (Nuevo)")
    print("  7. Cambiar dataset (Cargar resultados previos)")
    print("  8. Salir")
    print("─" * 50)

def main():
    archivo_actual = "spotify_completo.csv" # Cambia a spotify_pequeno.csv si usas el subconjunto
    print(f"\n  Cargando dataset: {archivo_actual}...")
    canciones = archivos.cargar_datos_csv(archivo_actual)
    if not canciones:
        return

    encabezados = analisis.obtener_encabezados(canciones)
    print(f"  Dataset cargado: {len(canciones)} canciones.")

    while True:
        mostrar_menu()
        opcion = input("  Elige una opción (1-8): ").strip()

        if opcion == "1":
            termino = input("\n  Término a buscar: ").strip()
            if termino:
                resultados = analisis.buscar_por_termino(canciones, termino)
                print(f"\n  Se encontraron {len(resultados)} registros:\n")
                for c in resultados[:10]: imprimir_cancion(c, encabezados)
                archivos.registrar_historial(f"Búsqueda: '{termino}'", len(resultados))
                preguntar_guardado(resultados)

        elif opcion == "2":
            campos = analisis.listar_campos_numericos(canciones)
            print("\n  Campos:", ", ".join(campos))
            campo = input("  Campo a evaluar: ").strip()
            stats = analisis.estadisticas_campo(canciones, campo)
            if stats:
                print(f"\n  {campo} -> Máx: {stats['maximo']:.2f}, Mín: {stats['minimo']:.2f}, Prom: {stats['promedio']:.2f}")
                archivos.registrar_historial(f"Estadísticas de '{campo}'", stats['total'])

        elif opcion == "3":
            campos = analisis.listar_campos_numericos(canciones)
            print("\n  Campos:", ", ".join(campos))
            campo = input("  Campo a filtrar: ").strip()
            try:
                umbral = float(input(f"  Valor mínimo para {campo}: "))
                resultados = analisis.filtrar_por_valor(canciones, campo, umbral)
                print(f"\n  {len(resultados)} resultados:\n")
                for c in resultados[:10]: imprimir_cancion(c, encabezados)
                archivos.registrar_historial(f"Filtro: {campo} > {umbral}", len(resultados))
                preguntar_guardado(resultados)
            except ValueError:
                print("  Valor no válido.")

        elif opcion == "4":
            campos = analisis.listar_campos_texto(canciones)
            print("\n  Campos:", ", ".join(campos))
            campo = input("  Campo para agrupar: ").strip()
            grupos = analisis.agrupar_por_categoria(canciones, campo)
            for valor, conteo in grupos[:15]:
                print(f"  {valor:<25} {conteo:>4}  {'█' * min(conteo, 40)}")
            archivos.registrar_historial(f"Agrupación por '{campo}'", len(grupos))

        elif opcion == "5":
            campos_txt = analisis.listar_campos_texto(canciones)
            campos_num = analisis.listar_campos_numericos(canciones)
            print("\n  Campos de texto:", ", ".join(campos_txt))
            c_texto = input("  Campo de texto para agrupar (ej. genre): ").strip()
            val1 = input("  Valor del Grupo 1 (ej. pop): ").strip()
            val2 = input("  Valor del Grupo 2 (ej. rock): ").strip()
            
            print("\n  Campos numéricos:", ", ".join(campos_num))
            c_num = input("  Campo numérico a promediar (ej. popularity): ").strip()

            comparacion = analisis.comparar_grupos(canciones, c_texto, val1, val2, c_num)
            print(f"\n  Comparación de promedio de '{c_num}':")
            for grupo, datos in comparacion.items():
                if datos:
                    print(f"  Grupo '{grupo}' ({datos['total']} canciones): {datos['promedio']:.2f}")
                else:
                    print(f"  Grupo '{grupo}': Sin datos.")
            archivos.registrar_historial(f"Comparación: {val1} vs {val2} en {c_num}", 2)

        elif opcion == "6":
            print("\n  --- HISTORIAL DE CONSULTAS ---")
            print(archivos.leer_historial())

        elif opcion == "7":
            nuevo_archivo = input("\n  Nombre del archivo CSV a cargar: ").strip()
            nuevas_canciones = archivos.cargar_datos_csv(nuevo_archivo)
            if nuevas_canciones:
                canciones = nuevas_canciones
                encabezados = analisis.obtener_encabezados(canciones)
                archivo_actual = nuevo_archivo
                print(f"  Ahora estás trabajando con '{archivo_actual}' ({len(canciones)} canciones).")

        elif opcion == "8":
            print("\n  Hasta luego!\n")
            break

if __name__ == "__main__":
    main()