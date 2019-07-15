import sys
from PyQt5.QtWidgets  import QApplication,QMainWindow,QMenuBar,QAction
from PyQt5.QtGui import QIcon
x = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(100,200,500,500)

def f():
    print("hello menu")
menu = window.menuBar()
f1 = menu.addMenu('File')
f2 = menu.addMenu('Edit')
item = QAction(QIcon('d.png'),'New',window)
item.setShortcut('ctrl+a')
item.triggered.connect(f)
f1.addAction(item)

window.show()
x.exec_()
