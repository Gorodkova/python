import sys 
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 250)
    w.setWindowTitle("Hello, world")
    w.show()
    sys.exit(app.exec_())