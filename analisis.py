import pandas as pd


def cargar_datos(ruta):
    df = pd.read_csv(ruta)
    return df


def buscar_por_termino(canciones, termino):
    termino_lower = termino.lower()
    resultados = []

    for c in canciones:
        for valor in c.values():
            if isinstance(valor, str) and termino_lower in valor.lower():
                resultados.append(c)
                break

    return resultados


def estadisticas_campo(canciones, campo):
    valores = []

    for c in canciones:
        if campo not in c:
            continue

        try:
            valores.append(float(c[campo]))
        except:
            pass

    if not valores:
        return None

    return {
        "maximo": max(valores),
        "minimo": min(valores),
        "promedio": sum(valores) / len(valores),
        "total": len(valores)
    }


def filtrar_por_valor(canciones, campo, umbral):
    resultados = []

    for c in canciones:
        if campo not in c:
            continue

        try:
            if float(c[campo]) > umbral:
                resultados.append(c)
        except:
            pass

    return resultados


def agrupar_por_categoria(canciones, campo):
    conteo = {}

    for c in canciones:
        if campo not in c:
            continue

        clave = str(c[campo]).strip()
        if not clave:
            continue

        conteo[clave] = conteo.get(clave, 0) + 1

    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)


def comparar_grupos(canciones, campo_texto, valor1, valor2, campo_numerico):
    grupo1 = [
        c for c in canciones
        if str(c.get(campo_texto, "")).strip().lower() == valor1.lower()
    ]

    grupo2 = [
        c for c in canciones
        if str(c.get(campo_texto, "")).strip().lower() == valor2.lower()
    ]

    def calc_stats(grupo):
        valores = []

        for c in grupo:
            try:
                valores.append(float(c[campo_numerico]))
            except:
                pass

        if not valores:
            return None

        return {
            "promedio": sum(valores) / len(valores),
            "total": len(valores)
        }

    return {
        valor1: calc_stats(grupo1),
        valor2: calc_stats(grupo2)
    }


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
        except:
            pass

    return numericos


def listar_campos_texto(canciones):
    if not canciones:
        return []

    todos = list(canciones[0].keys())
    numericos = set(listar_campos_numericos(canciones))

    return [c for c in todos if c not in numericos]
