# app/view/LoginView.py
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from app.ui.Login import (
    Ui_Login,
)  # Asegúrate de importar correctamente la interfaz generada por Qt Designer


class Login_View(QWidget, Ui_Login):  # Heredamos de QWidget y de la interfaz Ui_Login
    def __init__(self, main, parent=None):  # Recibimos la referencia de MainWindow
        super(Login_View, self).__init__(parent)
        self.setupUi(self)  # Configura los widgets generados por Qt Designer

        # Configuración inicial de la interfaz
        QTimer.singleShot(
            0, self.lineEditUsuario.setFocus
        )  # Pone el foco en el campo de usuario
        self.lineEditPassword.setEchoMode(
            QLineEdit.Password
        )  # Establece el campo de contraseña como oculto
        self.BtnIngresar.clicked.connect(
            self.iniciar_sesion
        )  # Conectamos el botón BtnIngresar

    def iniciar_sesion(self):
        """
        Este método maneja el evento de clic en el botón de 'Ingresar'.
        Solo imprime la salida en consola dependiendo de las credenciales.
        """
        usuario = self.lineEditUsuario.text()  # Obtener el texto del usuario
        contrasena = self.lineEditPassword.text()  # Obtener el texto de la contraseña

        print(f"Usuario ingresado: {usuario}")
        print(f"Contraseña ingresada: {contrasena}")

        # Verificación (aquí puedes conectar a tu base de datos si lo deseas)
        if usuario == "admin" and contrasena == "1234":
            print("Inicio de sesión exitoso")

        else:
            print("Credenciales incorrectas")
            # Aquí puedes mostrar algún mensaje de error visual (si lo deseas)
