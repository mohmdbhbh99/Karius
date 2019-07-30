import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QPushButton,QLineEdit,QMessageBox,QLabel,QPlainTextEdit,QPlainTextDocumentLayout
import mysql.connector
from PyQt5.QtGui import QPixmap
from time import sleep


mydb = mysql.connector.connect(host="localhost",user="root",password="root@01060744077")
mycursor = mydb.cursor()

import pyttsx3
engine = pyttsx3.init()



x = QApplication(sys.argv)
window2 = QWidget()
window2.setFixedSize(820,600)
window2.setWindowTitle('Karius Artificial Intelligence Corp JR')

labelPicture = QLabel(window2)
Pic = QPixmap('girl.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

intro_label2 = QLabel('Karius AI Corporation',window2)
intro_label2.setGeometry(130, 10, 600, 130)
intro_label2.setStyleSheet("color:white;font-size:60px;font-weight:bold;font-family:'Times New Roman';")

labelQuestion = QLabel('Answer',window2)
labelAnswer = QLabel('Question',window2)
labelQuestion.setStyleSheet("color:white;font-size:25px;font-weight:bold;font-family:'Times New Roman';")
labelAnswer.setStyleSheet("color:white;font-size:25px;font-weight:bold;font-family:'Times New Roman';")
labelQuestion.setGeometry(90, 280, 400, 50)
labelAnswer.setGeometry(90, 220, 400, 50)

lineEdit2 = QLineEdit(window2)
lineEdit2.setGeometry(210, 280, 400, 50)
lineEdit2.setStyleSheet("border-radius:25px;font-size:20px;color:black;")
lineEdit3 = QLineEdit(window2)
lineEdit3.setGeometry(210, 220, 400, 50)
lineEdit3.setStyleSheet("border-radius:25px;font-size:20px;color:black;")

injectbutton2 = QPushButton('Inject', window2)
injectbutton2.setGeometry(260, 340, 300, 50)
injectbutton2.setStyleSheet("background-color:rgb(255, 112, 138);border-radius:25px;font-size:25px;color:black;font-weight:bold;font-family:'Times New Roman';")

def Inject():
    xA = lineEdit2.text()
    yQ = lineEdit3.text()
    mycursor.execute("use ai")
    mycursor.execute("select Question from ai where Question ='" + yQ + "'")
    for i in mycursor:
        if yQ in i:
            msg1 = QMessageBox.warning(window2, 'Error', 'This Question Already Exists ..')
            lineEdit2.setText(None)
            lineEdit3.setText(None)




    values = (lineEdit3.text(), lineEdit2.text())
    sql = "insert into ai(Question,Answer) values(%s,%s)"
    mycursor.execute(sql, values)
    mydb.commit()
    msg1 = QMessageBox.information(window2, 'Success', 'Injection Completed ')
    mycursor.execute("delete from ai where Question =''")
    lineEdit2.setText(None)
    lineEdit3.setText(None)



injectbutton2.clicked.connect(Inject)


def showWindow2():
    window2.show()
def Activate():
    typedText = lineEdit1.text()
    mycursor.execute("use ai")
    mycursor.execute("select Answer from ai where Question = '" + typedText + "'")
    for i in mycursor:
     lineAnalysis.setPlainText(i[0])
     engine.say(str(i[0]))
     engine.runAndWait()
     engine.stop()

# ------------------------------------------------------------------------------------ WINDOW ONE ----------------------------------------------------------

window1 = QWidget()
window1.setFixedSize(820,600)
window1.setWindowTitle('Karius Artificial Intelligence Corp JR')

labelPicture = QLabel(window1)
Pic = QPixmap('girl.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

intro_label = QLabel('Karius AI Corporation \n                ⚜',window1)
intro_label.setGeometry(130, 10, 600, 150)
intro_label.setStyleSheet("color:white;font-size:60px;font-weight:bold;font-family:'Times New Roman';")

lineEdit1 = QLineEdit(window1)
lineEdit1.setGeometry(215, 230, 400, 50)
lineEdit1.setStyleSheet("border-radius:25px;font-size:20px;color:black;")

lineAnalysis = QPlainTextEdit(window1)
lineAnalysis.setGeometry(215, 400, 400, 150)
lineAnalysis.setStyleSheet("border-radius:70px;"
                           "font-size:20px;"
                           "color:black;"
                           "font-family:'Times New Roman';"
                           "font-weight:bold;")

labelanalysis = QLabel('Analysis',window1)
labelanalysis.move(365, 360)
labelanalysis.setStyleSheet("font-size:30px;font-family:'Times New Roman';font-weight:bold;color:white;")


Excbutton = QPushButton('Activate', window1)
Excbutton.setGeometry(265, 175, 300, 50)
Excbutton.setStyleSheet("background-color:rgb(255, 112, 138);border-radius:25px;font-size:25px;color:black;font-weight:bold;font-family:'Times New Roman';")
Excbutton.clicked.connect(Activate)


injectbutton = QPushButton('Inject', window1)
injectbutton.setGeometry(265, 285, 300, 50)
injectbutton.setStyleSheet("background-color:rgb(255, 112, 138);border-radius:25px;font-size:25px;color:black;font-weight:bold;font-family:'Times New Roman';")


injectbutton.clicked.connect(showWindow2)

window1.show()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------




















































x.exec_()
















































