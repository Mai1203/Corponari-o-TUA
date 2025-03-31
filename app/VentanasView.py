# app/VentanasView.py
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QStackedWidget
from PyQt5.QtGui import QIcon
from app.view import (
    SidebarView,
    PersonalView,
)  # Asegúrate de importar correctamente SidebarView y PersonalView

class MainApp(QWidget):
    def __init__(self, parent=None):  # Recibe la referencia de MainWindow
        super(MainApp, self).__init__(parent)

        print("MainApp inicializada.")

        # Configuración de la ventana principal
        self.setWindowTitle("Corponariño")
        self.setWindowIcon(QIcon("assets/iconoTitulo.png"))
        self.resize(800, 600)
        self.setStyleSheet("background-color: white;")

        # Widget central que contiene el diseño principal
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        layout.setSpacing(0)

        # Crear el Sidebar (equivalente al Navbar)
        self.sidebar = SidebarView()
        layout.addWidget(self.sidebar)  # Sidebar a la izquierda
        print("Sidebar añadido a MainApp.")

        # Crear el QStackedWidget para el contenido
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)  # Agregar el QStackedWidget al lado derecho

        # Crear las vistas
        self.personal = PersonalView()
        print("Vista de PersonalView creada.")

        # Agregar las vistas al QStackedWidget
        self.stacked_widget.addWidget(self.personal)  # Índice 0 (Vista de Personal)
        print("Vista de PersonalView añadida al QStackedWidget.")

        # Conectar el botón BtnExpediente del Sidebar para cambiar la vista
        self.sidebar.BtnExpediente.clicked.connect(
            lambda: self.stacked_widget.setCurrentWidget(self.personal)
        )
