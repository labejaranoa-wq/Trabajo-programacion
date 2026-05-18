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
        if campo not in c: continue
        texto = c[campo].strip()
        try:
            valores.append(float(texto))
        except ValueError:
            pass   

    if not valores: return None

    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)
    return {"maximo": maximo, "minimo": minimo, "promedio": promedio, "total": len(valores)}

def filtrar_por_valor(canciones, campo, umbral):
    resultados = []
    for c in canciones:
        if campo not in c: continue
        try:
            if float(c[campo]) > umbral:
                resultados.append(c)
        except ValueError:
            pass
    return resultados

def agrupar_por_categoria(canciones, campo):
    conteo = {}
    for c in canciones:
        if campo not in c: continue
        clave = c[campo].strip()
        if not clave: continue
        conteo[clave] = conteo.get(clave, 0) + 1

    # Ordenar de mayor a menor
    return sorted(conteo.items(), key=lambda x: x[1], reverse=True)

def comparar_grupos(canciones, campo_texto, valor1, valor2, campo_numerico):
    grupo1 = [c for c in canciones if c.get(campo_texto, "").strip().lower() == valor1.lower()]
    grupo2 = [c for c in canciones if c.get(campo_texto, "").strip().lower() == valor2.lower()]

    def calc_stats(grupo):
        valores = [float(c[campo_numerico]) for c in grupo if c.get(campo_numerico, "").replace('.', '', 1).isdigit()]
        if not valores: return None
        return {"promedio": sum(valores)/len(valores), "total": len(valores)}

    return {
        valor1: calc_stats(grupo1),
        valor2: calc_stats(grupo2)
    }

def obtener_encabezados(canciones):
    if not canciones: return []
    return list(canciones[0].keys())

def listar_campos_numericos(canciones):
    numericos = []
    if not canciones: return numericos
    for clave, valor in canciones[0].items():
        try:
            float(valor)
            numericos.append(clave)
        except ValueError:
            pass
    return numericos

def listar_campos_texto(canciones):
    if not canciones: return []
    todos = list(canciones[0].keys())
    numericos = set(listar_campos_numericos(canciones))
    return [c for c in todos if c not in numericos]