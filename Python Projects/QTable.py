import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QTableWidget,QTableWidgetItem

x = QApplication(sys.argv)
window = QWidget()
window.setGeometry(100,200,500,500)

table = QTableWidget(window)
table.setRowCount(2)
table.setColumnCount(3)
table.setGeometry(100,100,350,120)
table.setItem(0,0,QTableWidgetItem('Hi'))
table.setItem(0,1,QTableWidgetItem('Mr'))
table.setItem(0,2,QTableWidgetItem('Karious'))
table.setHorizontalHeaderLabels(str("num1:num2:num3").split(':'))
table.setVerticalHeaderLabels(str("num1:num2:num3").split(':'))

def func():
    for i in table.selectedItems() :
        print(i.row(),',',i.column(),',',i.text())

table.clicked.connect(func)




window.show()
x.exec_()
