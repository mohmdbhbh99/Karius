import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QPushButton,QLineEdit,QMessageBox,QLabel

def printMsg():
    print("hello fuck")

x = QApplication(sys.argv)
window = QWidget()

# ----------------------------------------------------------------------------
def printMsg():
    msg = lineEdit.text()
    print("Hello " + msg)
lineEdit = QLineEdit(window)
lineEdit.setGeometry(150,200,140,20)
# ----------------------------------------------------------------------------
button = QPushButton('click me',window)
button.move(180,250)
button.clicked.connect(printMsg)
# ----------------------------------------------------------------------------
window.setGeometry(100,200,500,500)
window.show()
# ----------------------------------------------------------------------------
label = QLabel('This is label',window)
label.move(80,200)
label.show()
# ----------------------------------------------------------------------------
msgBox = QMessageBox.question(window,'title','text',QMessageBox.Yes|QMessageBox.Close)
if msgBox == QMessageBox.Yes :
    print("Yes Accepted")
else :
    window.close()
# ----------------------------------------------------------------------------

x.exec_()
