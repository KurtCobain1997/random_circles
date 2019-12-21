import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(150, 150, 400, 400)
        self.setWindowTitle('Git и случайные окружности')
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Круг")
        self.pushButton.move(self.width() - 100, self.height() - 30)
        self.pushButton.clicked.connect(self.run)

    def drawCircle(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setPen(QColor(r, g, b))
        if self.width() > self.height():
            dm = self.height()
        else:
            dm = self.width()
        dm = random.randint(10, dm)
        qp.drawEllipse(0, 0, dm, dm)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def run(self, event):
        self.update()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())