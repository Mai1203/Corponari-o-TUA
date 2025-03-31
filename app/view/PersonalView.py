# app/view/SidebarView.py
from PyQt5.QtWidgets import QWidget
from app.ui.Personal import Ui_Personal

class PersonalView(QWidget, Ui_Personal):
    def __init__( self, parent=None):
        super(PersonalView, self).__init__(parent)
        # Aquí tu implementación
        self.setWindowTitle("Informacion Personal")

