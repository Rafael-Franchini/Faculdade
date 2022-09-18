"""Importando bibliotecas"""
from PyQt5.QtWidgets import*
import sys
from PyQt5.QtWebEngineWidgets import*
from PyQt5.QtCore import*

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser= QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
App = QApplication(sys.argv)
QApplication.setApplicationName('Meu_browser')
windows=MainWindow()

"""Executando app"""
App.exec()