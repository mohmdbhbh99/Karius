import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QTabWidget,QPushButton

x = QApplication(sys.argv)
window = QWidget()

window.setGeometry(100,200,500,500)


# ----------------------------------------------------------------------------
tab = QTabWidget(window)
tab.setGeometry(20,10,500,500)
t1 = QWidget()
t2 = QWidget()

tab.addTab(t1,'tab1')
tab.addTab(t2,'tab2')

# ----------------------------------------------------------------------------
button1 = QPushButton('hello tab1',t1)
button2 = QPushButton('hello tab2',t2)


window.show()
x.exec_()
