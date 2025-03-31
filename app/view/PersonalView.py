# app/view/SidebarView.py
from PyQt5.QtWidgets import QWidget


class PersonalView(QWidget):
    def __init__(self, parent=None):
        super(PersonalView, self).__init__(parent)
        # Aquí tu implementación
        self.setWindowTitle("Expedientes")
