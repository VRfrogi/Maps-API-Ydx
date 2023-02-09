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
        self.scaler = float()
        self.layer = 'skl'
        self.place = str()
        self.point = list()
        self.Hybride.value = 'sat,skl'
        self.Hybride.toggled.connect(self.changeType)
        self.Scheme.value = 'skl'
        self.Scheme.toggled.connect(self.changeType)
        self.Satellite.value = 'sat'
        self.Satellite.toggled.connect(self.changeType)
        self.getResult.clicked.connect(self.decorator)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        koef = 0.25 * self.scaler
        print(event.key())
        if event.key() == 57 and self.scaler < 90 - koef:
            self.scaler += koef
            self.mapIt(getNew=False)
        elif event.key() == 51 and self.scaler > koef:
            self.scaler -= koef
            self.mapIt(getNew=False)
        elif event.key() == 1062:
            self.sCord += koef
            self.mapIt(getNew=False)
        elif event.key() == 1067:
            self.sCord -= koef
            self.mapIt(getNew=False)
        elif event.key() == 1042:
            self.fCord += koef
            self.mapIt(getNew=False)
        elif event.key() == 1060:
            self.fCord -= koef
            self.mapIt(getNew=False)
        

    def decorator(self):
        self.mapIt(getNew=True)

    def changeType(self):
        self.layer = self.sender().value
        self.mapIt(getNew=False)
                
    def mapIt(self, getNew=True):
        if getNew and self.getPlace.toPlainText() == 'Введите название объекта' or self.getPlace.toPlainText() == '':
            self.point = list()
            if getNew or not self.sCord:
                self.fCord, self.sCord = float(self.firstCoord.text()), float(self.secondCoord.text())
            if getNew or not self.scaler:
                self.scaler = float(self.scale.text())
        elif getNew:
            info = get_coords(self.getPlace.toPlainText())
            self.fCord, self.sCord = info['coords']
            self.point = list(info['coords'])
            self.scaler = max(info['del_dolg'], info['del_shir'])
        get_image((self.fCord, self.sCord), (self.scaler, self.scaler), self.layer, self.point)
        map = QtGui.QPixmap('map.png')
        self.map.setPixmap(map)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mapper()
    ex.show()
    sys.exit(app.exec_())