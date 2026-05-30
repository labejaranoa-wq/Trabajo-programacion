import sys
import pandas as pd
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QPushButton
)
from PyQt5.QtCore import Qt
import analisis

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DataLab — Equipo de Análisis de Sonido")
        self.setMinimumSize(1000, 700)
        self.df = analisis.cargar_datos("spotify_completo.csv")
        self.setup_ui()

    def setup_ui(self):
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout_principal = QVBoxLayout()
        widget_central.setLayout(layout_principal)

        encabezado = QLabel("🎵 DataLab — Equipo de Análisis de Sonido")
        encabezado.setAlignment(Qt.AlignCenter)
        encabezado.setStyleSheet("font-size: 24px; font-weight: bold; padding: 20px;")
        layout_principal.addWidget(encabezado)

        subtitulo = QLabel("Predicción de popularidad de canciones en Spotify")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setStyleSheet("font-size: 14px; color: gray; padding-bottom: 10px;")
        layout_principal.addWidget(subtitulo)

        self.area_contenido = QVBoxLayout()
        layout_principal.addLayout(self.area_contenido)

        boton_salir = QPushButton("Salir")
        boton_salir.setStyleSheet("background-color: #e74c3c; color: white; padding: 8px; font-size: 13px;")
        boton_salir.clicked.connect(self.close)
        layout_principal.addWidget(boton_salir)