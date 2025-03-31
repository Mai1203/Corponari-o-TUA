# app/view/SidebarView.
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from app.ui.Sidebar import Ui_sidebar


class SidebarView(QWidget, Ui_sidebar):
    def __init__(self, parent=None):  # Recibimos la referencia de MainWindow
        super(SidebarView, self).__init__(parent)
        self.setupUi(self)  # Configura los widgets generados por Qt Designer
        self.setWindowTitle("Sidebar")
