import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt 
from  PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from get_shots import get_coords, get_image

class Mapper(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Yandex Maps API')
        uic.loadUi('Maps-API-Ydx\Interface.ui', self)
        self.scaler = float()
        self.getResult.clicked.connect(self.decorator)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        print(event.key())
        koef = 0.25
        if event.key() == Qt.Key_PageUp and self.scaler < 90 - koef:
            self.scaler += koef
            print(self.scaler)
            self.mapIt(getScale=False, getCenter=False)
        elif event.key() == Qt.Key_PageDown and self.scaler > koef:
            self.scaler -= koef
            print(self.scaler)
            self.mapIt(getScale=False, getCenter=False)
        elif event.key() == Qt.Key_W:
            self.sCord += koef
            self.mapIt(getScale=False, getCenter=False)
        elif event.key() == Qt.Key_S:
            self.sCord -= koef
            self.mapIt(getScale=False, getCenter=False)
        elif event.key() == Qt.Key_D:
            self.fCord += koef
            self.mapIt(getScale=False, getCenter=False)
        elif event.key() == Qt.Key_A:
            self.fCord -= koef
            self.mapIt(getScale=False, getCenter=False)

    def decorator(self):
        self.mapIt(getScale=True, getCenter=True)
                
    def mapIt(self, getScale=True, getCenter=True):
        if getCenter or not self.sCord:
            self.fCord, self.sCord = float(self.firstCoord.text()), float(self.secondCoord.text())
        if getScale or not self.scaler:
            self.scaler = float(self.scale.text())
        get_image((self.fCord, self.sCord), (self.scaler, self.scaler))
        map = QtGui.QPixmap('map.png')
        self.map.setPixmap(map)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mapper()
    ex.show()
    sys.exit(app.exec_())