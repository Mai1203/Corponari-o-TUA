# main.py
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)
from PyQt5.QtGui import QIcon
import sys
from app.view.LoginView import Login_View  # Importamos la clase Login_View
from app.VentanasView import MainApp  # Importamos la clase MainApp


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Corponariño")
        self.setWindowIcon(QIcon("assets/iconoTitulo.png"))
        self.resize(500, 600)
        self.setStyleSheet("background-color: white;")

        # Deshabilitar el redimensionamiento de la ventana
        # self.setFixedSize(self.size())  # Fijar el tamaño de la ventana y previene el cambio de tamaño

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Crear el diseño principal
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        layout.setSpacing(0)

        self.stacked_widget = QStackedWidget()  # Contenedor de vistas
        layout.addWidget(self.stacked_widget)

        # Instanciar las vistas
        self.Login = Login_View()  # Pasar la referencia de MainWindow a Login_View
        self.MainApp = MainApp()  # Pasar la referencia de MainWindow a MainApp

        # Agregar vistas al QStackedWidget
        
        self.stacked_widget.addWidget(self.Login)
        self.stacked_widget.addWidget(self.MainApp)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
