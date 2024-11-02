import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtWebEngineWidgets import *


class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.navigateur = QWebEngineView()
        self.navigateur.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.navigateur)
        self.showMaximized()

        # Barre de navigation
        navbar = QToolBar()
        self.addToolBar(navbar)

        accueil_btn = QAction('Accueil', self)
        accueil_btn.triggered.connect(self.url_accueil)
        navbar.addAction(accueil_btn)

        retour_btn = QAction(QtGui.QIcon('back.png'), 'Retour', self)
        retour_btn.triggered.connect(self.navigateur.back)
        navbar.addAction(retour_btn)

        refresh_btn = QAction(QtGui.QIcon('refresh.png'), 'Actualiser', self)
        refresh_btn.triggered.connect(self.navigateur.reload)
        navbar.addAction(refresh_btn)

        avancer_btn = QAction(QtGui.QIcon('avancer.png'), 'Avancer', self)
        avancer_btn.triggered.connect(self.navigateur.forward)
        navbar.addAction(avancer_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)

        # Appliquer des styles CSS pour arrondir les bords de la barre d'URL
        self.url_bar.setStyleSheet("border-radius: 10px; padding: 5px;")

        navbar.addWidget(self.url_bar)

        recherche_btn = QPushButton()
        recherche_btn.setIcon(QtGui.QIcon('loupe.png'))
        recherche_btn.clicked.connect(self.navigation)
        navbar.addWidget(recherche_btn)

        self.navigateur.urlChanged.connect(self.update_url)

    def url_accueil(self):
        self.navigateur.setUrl(QUrl('http://google.com'))

    def navigation(self):
        url = self.url_bar.text()
        self.navigateur.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('SecureWeb Sentinel')
fenetre = FenPrincipale()
fenetre.show()
sys.exit(app.exec_())
