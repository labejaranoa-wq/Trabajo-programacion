import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QTextEdit, QComboBox
)
from PyQt5.QtCore import Qt
import analisis
import csv

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DataLab — Equipo de Análisis de Sonido")
        self.setMinimumSize(1000, 700)
        self.df = analisis.cargar_datos("spotify_completo.csv")
        self.ultimos_resultados = []
        self.setup_ui()

    def setup_ui(self):
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        # ENCABEZADO
        encabezado = QLabel("🎵 DataLab — Equipo de Análisis de Sonido")
        encabezado.setAlignment(Qt.AlignCenter)
        encabezado.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px;")
        layout_principal.addWidget(encabezado)

        subtitulo = QLabel("Predicción de popularidad de canciones en Spotify")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setStyleSheet("font-size: 14px; color: gray; padding-bottom: 10px;")
        layout_principal.addWidget(subtitulo)

        # PANEL BÚSQUEDA
        label_busqueda = QLabel("🔍 Buscar canción o artista:")
        label_busqueda.setStyleSheet("font-size: 14px; font-weight: bold; padding-top: 15px;")
        layout_principal.addWidget(label_busqueda)

        self.campo_busqueda = QLineEdit()
        self.campo_busqueda.setPlaceholderText("Escribe un nombre de canción, artista o género...")
        self.campo_busqueda.setStyleSheet("padding: 6px; font-size: 13px;")
        layout_principal.addWidget(self.campo_busqueda)

        boton_buscar = QPushButton("Buscar")
        boton_buscar.setStyleSheet("background-color: #2ecc71; color: white; padding: 8px; font-size: 13px;")
        boton_buscar.clicked.connect(self.ejecutar_busqueda)
        layout_principal.addWidget(boton_buscar)

        # PANEL FILTRADO
        label_filtro = QLabel("🎚️ Filtrar por valor numérico:")
        label_filtro.setStyleSheet("font-size: 14px; font-weight: bold; padding-top: 15px;")
        layout_principal.addWidget(label_filtro)

        self.selector_campo = QComboBox()
        self.selector_campo.addItems(["popularity", "energy", "tempo", "valence", "duration_ms"])
        self.selector_campo.setStyleSheet("padding: 6px; font-size: 13px;")
        layout_principal.addWidget(self.selector_campo)

        self.campo_umbral = QLineEdit()
        self.campo_umbral.setPlaceholderText("Escribe el valor mínimo (ej: 80)")
        self.campo_umbral.setStyleSheet("padding: 6px; font-size: 13px;")
        layout_principal.addWidget(self.campo_umbral)

        boton_filtrar = QPushButton("Filtrar")
        boton_filtrar.setStyleSheet("background-color: #3498db; color: white; padding: 8px; font-size: 13px;")
        boton_filtrar.clicked.connect(self.ejecutar_filtro)
        layout_principal.addWidget(boton_filtrar)

        # RESULTADOS
        label_resultados = QLabel("Resultados:")
        label_resultados.setStyleSheet("font-size: 13px; font-weight: bold; padding-top: 10px;")
        layout_principal.addWidget(label_resultados)

        self.area_resultados = QTextEdit()
        self.area_resultados.setReadOnly(True)
        self.area_resultados.setStyleSheet("font-size: 12px; padding: 5px;")
        self.area_resultados.setMinimumHeight(200)
        layout_principal.addWidget(self.area_resultados)

        boton_guardar = QPushButton("💾 Guardar resultados en CSV")
        boton_guardar.setStyleSheet("background-color: #f39c12; color: white; padding: 8px; font-size: 13px;")
        boton_guardar.clicked.connect(self.guardar_resultados)
        layout_principal.addWidget(boton_guardar)

        # ESTADISTICAS
        boton_estadisticas = QPushButton("📊 Ver estadísticas")
        boton_estadisticas.clicked.connect(self.ver_estadisticas)
        layout_principal.addWidget(boton_estadisticas)

# CATEGORIAS
       boton_categorias = QPushButton("🎼 Distribución por género")
       boton_categorias.clicked.connect(self.ver_categorias)
       layout_principal.addWidget(boton_categorias)

# METRICAS
       boton_metricas = QPushButton("📈 Métricas numéricas")
       boton_metricas.clicked.connect(self.ver_metricas)
       layout_principal.addWidget(boton_metricas)

        # BOTÓN SALIR
        boton_salir = QPushButton("Salir")
        boton_salir.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-size: 13px;")
        boton_salir.clicked.connect(self.close)
        layout_principal.addWidget(boton_salir)

    def ejecutar_busqueda(self):
        termino = self.campo_busqueda.text()
        if not termino:
            self.area_resultados.setText("Escribe un término para buscar.")
            return
        canciones = self.df.to_dict("records")
        resultados = analisis.buscar_por_termino(canciones, termino)
        self.ultimos_resultados = resultados
        if not resultados:
            self.area_resultados.setText("No se encontraron resultados.")
            return
        texto = f"Se encontraron {len(resultados)} canciones:\n\n"
        for c in resultados[:20]:
            texto += str(c) + "\n\n"
        self.area_resultados.setText(texto)

    def ejecutar_filtro(self):
        campo = self.selector_campo.currentText()
        try:
            umbral = float(self.campo_umbral.text())
        except ValueError:
            self.area_resultados.setText("Escribe un número válido en el valor mínimo.")
            return
        canciones = self.df.to_dict("records")
        resultados = analisis.filtrar_por_valor(canciones, campo, umbral)
        self.ultimos_resultados = resultados
        if not resultados:
            self.area_resultados.setText("No se encontraron canciones con ese filtro.")
            return
        texto = f"Se encontraron {len(resultados)} canciones con {campo} mayor a {umbral}:\n\n"
        for c in resultados[:20]:
            texto += str(c) + "\n\n"
        self.area_resultados.setText(texto)

        def guardar_resultados(self):
        if not self.ultimos_resultados:
            self.area_resultados.setText("Primero haz una búsqueda o filtrado.")
            return

        nombre = "resultados_guardados.csv"

        with open(nombre, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=self.ultimos_resultados[0].keys()
            )
            writer.writeheader()
            writer.writerows(self.ultimos_resultados)

        self.area_resultados.append(
            f"\n✅ Guardado en {nombre}"
        )

    def ver_estadisticas(self):
        canciones = self.df.to_dict("records")

        stats = analisis.estadisticas_campo(
            canciones,
            "popularity"
        )

        if not stats:
            self.area_resultados.setText(
                "No se pudieron calcular estadísticas."
            )
            return

        texto = (
            f"ESTADÍSTICAS DE POPULARIDAD\n\n"
            f"Máximo: {stats['maximo']}\n"
            f"Mínimo: {stats['minimo']}\n"
            f"Promedio: {stats['promedio']:.2f}\n"
            f"Total registros: {stats['total']}"
        )

        self.area_resultados.setText(texto)

    def ver_categorias(self):
        canciones = self.df.to_dict("records")

        categorias = analisis.agrupar_por_categoria(
            canciones,
            "track_genre"
        )

        texto = "DISTRIBUCIÓN POR GÉNERO\n\n"

        for genero, cantidad in categorias[:20]:
            texto += f"{genero}: {cantidad}\n"

        self.area_resultados.setText(texto)

    def ver_metricas(self):
        canciones = self.df.to_dict("records")

        campos = analisis.listar_campos_numericos(
            canciones
        )

        texto = "MÉTRICAS NUMÉRICAS\n\n"

        for campo in campos:
            stats = analisis.estadisticas_campo(
                canciones,
                campo
            )

            if stats:
                texto += (
                    f"{campo}\n"
                    f"Promedio: {stats['promedio']:.2f}\n"
                    f"Máximo: {stats['maximo']}\n"
                    f"Mínimo: {stats['minimo']}\n\n"
                )

        self.area_resultados.setText(texto)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
