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
* **Nombre Estudiante** - [Usuario GitHub]

---

## 🎯 Objetivo del proyecto
El objetivo es construir un DataLab: herramienta de análisis de datos que permite consultar, explorar y visualizar un dataset. El objeto de estudio es un dataset sobre el **potencial de éxito en canciones de Spotify** que usa mediciones de audio para clasificar canciones de la platafroma de musica respecto a la popularidad que pueden alcanzar y asimismo obtener las mejores opciones de inversión en producción, campañas y marketing en la industria musical.
### Preguntas de Investigación
Con el apoyo de esta herramienta se busca dar respuesta a las siguientes preguntas:
1.  ¿Cuántas canciones superan los 4 minutos de duración?
2.  ¿Cuántas canciones del dataset pertenecen a un artista específico ingresado por el usuario?
3.  ¿Cuál es el nivel mínimo y máximo de danceability registrado en las 50 canciones de prueba?
4.  ¿Cuántas canciones en total contienen contenido explícito?

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
   ** Aseguúrese de tener instalado Python 3.x.
   ** Descargue los archivos main.py y spotify_pequeno.csv, estos deben estar en la misma carpeta.
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
---

### 🪁 Producto creativo:
Rutas de acceso al material complementario de la entrega:
* 📑 **Póster creativo:** https://canva.link/xieo0rkkoeokdvs
* 🎬 **Video:** https://drive.google.com/file/d/1OK9nVW5C-IDDBrkKvGPu1FU2IEyhUKyI/view?usp=sharing
* 📄**Documento de contribucones por integrante:** https://docs.google.com/document/d/1LSCMckuBDdb3TX0yAz6pGdlRR296shXOC53y-VRI0Z0/edit?usp=sharing
