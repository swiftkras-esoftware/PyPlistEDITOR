from PyQt5 import QtWidgets

from pyplisteditor.interface.assets import mainwindow_QtUI


class EditorWinodwGUI(QtWidgets.QMainWindow, mainwindow_QtUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()  # Load design sourcecode from mainwindow_QtUI.py
        self.connect_callbacks()

    def connect_callbacks(self):
        """Connect UI elements with actions (WITH IT's HANDLERS CHECKER)"""
