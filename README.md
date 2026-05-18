# 👾 Sound Analytics Team
Proyecto de implementación de herramienta de análisis de datos en dataset sobre la predicción de popularidad de canciones en Spotify.
---
🦉**UNIVERSIDAD NACIONAL DE COLOMBIA**
- Programación de computadores  
- **Docente:** David Alberto Herrrera Álvarez 
- **Monitora** Maria Catalina Rodríguez Cardona 
- 2026 
## 👥 Integrantes
* **Laura Jimena Bejarano Arias** - [labejaranoa-wq]
* **Dayanna Leyton Bustos** - [dleyton-collab]
* **Juan Diego Rodriguez Delgado** - [juarodríguezde-bit]
* **Cristian Andres Ortiz Camargo** - [criortizca]
* **Miguel Ricardo Parra Sánchez** - [miparrasa]
* **Maria Andrea Marin Velasco** - [mmarinve]

---

## 🎯 Objetivo del proyecto
El objetivo es construir un DataLab: herramienta de análisis de datos que permite consultar, explorar y visualizar un dataset. El objeto de estudio es un dataset sobre el **potencial de éxito en canciones de Spotify** que usa mediciones de audio para clasificar canciones de la platafroma de musica respecto a la popularidad que pueden alcanzar y asimismo obtener las mejores opciones de inversión en producción, campañas y marketing en la industria musical.
### Preguntas de Investigación
Con el apoyo de esta herramienta se busca dar respuesta a las siguientes preguntas:
1.  ¿Cuántas y cuáles canciones duran más de determinado tiempo?
2.  ¿Cuántas y cuáles canciones salieron después de un año específico?
3.  ¿Cuántas canciones hay por artista?
4.  Mostrar las primeras 10 canciones de la lista.

---

## 💡 Entrega 1: Explorador
Mediante el funcionamiento de un programa de consola se carga el dataset seleccionado y es recorrido mediante bucles y el uso de funciones y condicionales para responder a las preguntas planteadas por el equipo.

### Funcionalidades implementadas:
1.  **Carga de datos:** Leer el archivo `spotify_pequeño.csv` (50 registros) línea por línea.
2.  **Búsqueda:** Encontrar canciones por nombre de la misma o por artista.
3.  **Estadísticas:** Calcula el máximo, mínimo y promedio en los diferentes campos de información presentada.
4.  **Otras (Agrupación por categoría):** Cuenta la cantidad de canciones lanzadas por el artista ingresado.

### 🐾 Instrucciones de Ejecución:
1. **Requisitos previos:**
   * Aseguúrese de tener instalado Python 3.x.
   * Descargue los archivos `main.py` y `spotify_pequeno.csv`, estos deben estar en la misma carpeta.
2. **Ejecución:**
   Abra una terminal o consola de comandos en la carpeta del proyecto y ejecute: python main.py
3. **Guía del menú interactivo:**
   Una vez iniciado, se verá un menú con 6 opciones:
   * **Opción 1 - Buscar canciones por término:** Escriba cualquier palabra (nombre del artista, canción o género). El sistema buscará coincidencias en todas las columnas y mostrará los primeros 20 resultados.
   * **Opción 2 - Estadísticas de un campo numérico:** El programa pondrá en una lista las opciones (ej. popularity, energy, tempo). Para ello debe escribir el nombre del campo tal cual aparece proporcionado. Obtendrá el valor máximo, mínimo y el promedio calculado automáticamente.
   * **Opción 3 - Filtrar por valor numérico:** El programa le proporcionará los campos con valores numéricos disponibles, elija el que desee (ej. popularity) y en seguida dijite el umbral (ej. 80). El programa mostrará solo las canciones que superen ese número.
   * **Opción 4 - Agrupar por categoría:** Dentro de las opciones que se muestran, elija el campo de texto de su preferencia(como genre o artist_name). El programa generará un ranking visual con barras mostrando los resultados con más presencia en el dataset.
   * **Opción 5 - Mostrar primeras 10 canciones:** Una vista rápida para verificar que los encabezados y los datos se cargaron correctamente.
   * **Opción 6 - Salir:** Cierra el programa de forma segura.
--

### 🪁 Producto creativo:
Rutas de acceso al material complementario de la entrega:
* 📑 **Póster creativo:** https://canva.link/xieo0rkkoeokdvs
* 🎬 **Video:** https://drive.google.com/file/d/1OK9nVW5C-IDDBrkKvGPu1FU2IEyhUKyI/view?usp=sharing
* 📄**Documento de contribuciones por integrante:** https://docs.google.com/document/d/1LSCMckuBDdb3TX0yAz6pGdlRR296shXOC53y-VRI0Z0/edit?usp=sharing

---

## 🎵 Entrega 2: Analizador
Ahora se transformará el script básico en una aplicación de software modular, escalable y con persistencia de datos. El sistema debe migrar hacia el uso de herramientas nativas avanzadas (como el módulo csv) para procesar el dataset real completo ('spotify_completo.csv') sin saturar la memoria, organizando la información a través de estructuras de datos justificadas e implementando un sistema interactivo de almacenamiento de resultados.


## Funciones implementadas
1. **Módulos:** Pasar de manejar un archivo único y dividirlo en modulos independientes: main.py (interfaz), analisis.py (lógica) y archivos.py (persistencia).
2. **Lectura avanzada:** Elimina el .split(",") manual e implementar el módulo nativo csv (csv.DictReader) para procesar las más de 200 filas del dataset real de forma robusta.
3. **Persistencia de Resultados:** Agregar una opción interactiva que guarda los resultados de búsquedas o filtros en un nuevo archivo .csv, y una opción que carga estos archivos y los analiza de forma aislada.
4. **Historial de consultas:** Escribir cada consulta en un archivo (registrando fecha, hora, criterio y cantidad de resultados) junto con una opción en el menú para imprimir todo el log en consola.
5. **Combinación de estructuras de datos:** Se usan de manera simultánea y justificada listas (almacenamiento ordenado), diccionarios (mapeo de datos y conteo de frecuencias) y sets (eliminación de duplicados y validación rápida de entradas).
6. **Comparación de Grupos:** Función en el menú que permite al usuario elegir dos categorías (ej: género pop vs. rock) y contrastar directamente sus métricas estadísticas (máximos, mínimos y promedios) en una tabla comparativa.

## Instrucciones de uso

1. **Descargar los archivos del repositorio:** Asegurese de descargar los siguientes archivos del repositorio y organicelos en una misma carpeta:
   * `main.py`(El código principal a ejecutar)
   * `analisis.py` (Lógica algorítmica)
   * `archivos.py` (Gestor de archivos)
   * `spotify_completo.csv` (Dataset principal con más de 200 filas)
   * `spotify_pequeno.csv` (Subconjunto de pruebas de 50 filas)

*Se recomienda usar al menos las primeras 500 filas del dataset completo puesto que el archivo contiene mas de 100.00 filas y puede sobresaturarse.*

2. **Preparación:** Abra su terminal o consola de comandos, diríjase a la carpeta del proyecto y ejecute el archivo principal: python 'main.py'.Le aparecerá el menú principal con 8 opciones numéricas, para ejecutar cualquiera de ellas debe digitar el número correspondiente:
3. **Opción 1 (Búsqueda General):** Le permite escribir cualquier palabra (nombre de canción, artista o género). El sistema buscará coincidencias y enlistará los resultados en pantalla.
4. **Opción 2 (Métricas Estadísticas):** Introduzca el nombre exacto de una columna numérica (ej: popularity, energy, tempo). Usando bucles acumuladores, la consola calculará y mostrará el valor máximo, mínimo y el promedio fiel de los registros cargados.
5. **Opción 3 (Filtrado Numérico):** Se usa para aislar datos, para ello debe ingresar un campo numérico, un operador (> o <) y un valor límite. El sistema imprimirá los registros que superen o queden por debajo de dicho umbral.
6. **Opción 4 (Distribución/Ranking):** Agrupa y cuenta cuántas canciones pertenecen a cada categoría dentro de un campo de texto de forma ordenada (de mayor a menor) generando un histograma visual básico en consola.
7. **Opción 5 (Comparación):** Elija un campo de texto (ej: track_genre), escriba dos grupos diferentes (ej: pop y rock) y una métrica numérica. El programa validará su existencia con conjuntos (sets) y contrastará sus promedios y límites.

*Guardar resultados - persistencia* Cuando realice una búsqueda (Opción 1) o un filtrado (Opción 3), al terminar de listar las canciones, el sistema le preguntará: *¿Desea guardar estos resultados en un nuevo archivo CSV? (s/n).*  Presione s si desea guardarlos y asigne un nombre al nuevo archivo. Se creará un archivo legible separado por comas de forma automática en el directorio.

9. **Opción 6 (Registro automático):** Cada acción realizada por usuario queda registrada automáticamente. Esta opción le permitirá consultar el historial acumulado hasta el momento, para lo cual imprimirá una tabla estructurada directamente desde el archivo autogenerado con el nombre de su elección, detallando: la fecha y hora exacta, la operación realizada, los criterios ingresados y el volumen de filas afectadas.
10. **Opción 7 (Recuperar Archivos Guardados):** Si cerró el programa y desea trabajar únicamente con el subconjunto de datos que guardó en un archivo en el Paso 3 sin procesar la base completa, esta opción le permitirá hacerlo, solo debe ingresar el nombre del archivo guardado. El sistema cambiará la fuente de datos en memoria y todas las búsquedas o estadísticas posteriores se calcularán solo sobre ese archivo.
11. **Opción 8 (Cierre Seguro):** Seleccione esta opción para finalizar la sesión y asegurar el correcto cierre.

### 🪁 Producto creativo:
Rutas de acceso al material complementario de la entrega:
* 📑 **Diagrama de flujo:** Se encuentra adjunto como archivo pdf
* 🎬 **Video:** https://drive.google.com/file/d/1EiLVqhetlhspkLudKjix5NoWCJOMj6Dw/view?usp=sharing
