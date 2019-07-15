import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QInputDialog,QLineEdit
x = QApplication(sys.argv)
window = QWidget()
window.setGeometry(100,200,500,500)

i = QInputDialog.getInt(window,'title','question',10,0,100,2)
print(i[0]) # print the written value


x = QInputDialog.getText(window,'title','question',QLineEdit.Normal)
print(x[0]) # print the written value


list = ['red','green','blue']
k = QInputDialog.getItem(window,'title','question',list,2,False)
print(k[0]) # print the written value




window.show()
x.exec_()
