import csv
import datetime

def cargar_datos_csv(ruta):
    canciones = []
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                canciones.append(row)
    except FileNotFoundError:
        print(f"\n  ERROR: no se encontró el archivo '{ruta}'.")
    return canciones

def guardar_resultados_csv(ruta, resultados):
    if not resultados:
        return
    encabezados = list(resultados[0].keys())
    try:
        with open(ruta, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=encabezados)
            writer.writeheader()
            writer.writerows(resultados)
        print(f"  Resultados guardados exitosamente en '{ruta}'.")
    except Exception as e:
        print(f"  Error al guardar: {e}")

def registrar_historial(accion, cantidad_resultados):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    archivo = "historial.csv"
    try:
        with open(archivo, mode='a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([fecha_hora, accion, f"{cantidad_resultados} resultados"])
    except Exception as e:
        print(f"  Error al guardar en el historial: {e}")

def leer_historial():
    try:
        with open("historial.csv", mode='r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "  El historial está vacío."