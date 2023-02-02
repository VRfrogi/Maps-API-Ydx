import PyQt5
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
        uic.loadUi('Interface.ui', self)
        self.getResult.clicked.connect(self.mapIt)
                
    def mapIt(self, getScale=True):
        self.fCord, self.sCord = float(self.firstCoord.text()), float(self.secondCoord.text())
        if getScale:
            self.scaler = float(self.scale.text())
        get_image((self.fCord, self.sCord), (self.scaler, self.scaler))
        map = QtGui.QPixmap('map.png')
        self.map.setPixmap(map)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mapper()
    ex.show()
    sys.exit(app.exec_())