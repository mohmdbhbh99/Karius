import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QPushButton,QLineEdit,QMessageBox,QLabel,QTabWidget,QPlainTextEdit
import mysql.connector
from PyQt5.QtGui import QPixmap


mydb = mysql.connector.connect(host="localhost",user="root",password="root@01060744077")
mycursor = mydb.cursor()

x = QApplication(sys.argv)

window1 = QWidget()
window1.setFixedSize(820,600)
window1.setWindowTitle('Work Management')
labelPicture = QLabel(window1)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)
labelPicture.autoFillBackground()

window2 = QWidget()
window2.setFixedSize(820,600)
window2.setWindowTitle('Work Management')
labelPicture = QLabel(window2)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)
labelPicture.autoFillBackground()

windownew = QWidget() # ---------------------------- New member window
windownew.setFixedSize(820,600)
windownew.setWindowTitle('Sports Club Management')
labelPicture = QLabel(windownew)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)
labelPicture.autoFillBackground()

window_search = QWidget() # ---------------------------- Search window
window_search.setFixedSize(820,600)
window_search.setWindowTitle('Sports Club Management')
labelPicture = QLabel(window_search)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)
labelPicture.autoFillBackground()

windowdelete = QWidget() # ------------------------- Delete member window
windowdelete.setFixedSize(820,600)
windowdelete.setWindowTitle('Sports Club Management')
labelPicture = QLabel(windowdelete)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)
labelPicture.autoFillBackground()

windowedit = QWidget() # --------------------------- Edit member window
windowedit.setFixedSize(820,600)
windowedit.setWindowTitle('Sports Club Management')
labelPicture = QLabel(windowedit)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)
labelPicture.autoFillBackground()

lineEdit1 = QLineEdit(window1) # ------------------- user name
lineEdit1.setGeometry(290,150,280,50)
lineEdit1.setStyleSheet("border-radius:25px;font-size:20px;color:black;")
lineEdit2 = QLineEdit(window1) # ------------------- password
lineEdit2.setGeometry(290,210,280,50)
lineEdit2.setStyleSheet("border-radius:25px;font-size:20px;color:black;")
# ......................................................................................................................

label1 = QLabel('User Name',window1)
label1.setGeometry(180,130,100,100)
label1.show()
label1.setStyleSheet("color:white;font-size:20px;")


label2 = QLabel('Password',window1)
label2.setGeometry(180,185,100,100)
label2.setStyleSheet("color:white;font-size:20px;")
label2.show()
def lineEditLogin():
    line1msg = lineEdit1.text()
    line2msg = lineEdit2.text()
    if line1msg == str('') and line2msg == str(''): # ---------------------- username and password
        window1.close()
        window2.show()
    else:
        msgboxinf = QMessageBox.information(window1,'Work Database','Access Denied , Incorrect Username or Password')
class Login_Button():

 Logbutton = QPushButton('Login',window1)
 Logbutton.setGeometry(315,270,230,50)
 Logbutton.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
 Logbutton.clicked.connect(lineEditLogin)

def NewMember():
    windownew.show()
def EditMember():
    windowedit.show()
def DeleteMember():
    windowdelete.show()
def WindowSearch():
    window_search.show()

button_new1 = QPushButton('New Member',window2) # new member of tab1
button_new1.setGeometry(300,310,200,50)
button_new1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
button_new1.clicked.connect(NewMember)
button_edit1 = QPushButton('Update Member',window2) # edit of of tab1
button_edit1.setGeometry(300,250,200,50)
button_edit1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
button_edit1.clicked.connect(EditMember)
button_del1 = QPushButton('Delete Member',window2) # delete member of tab1 ---------------------------------- TAB 1-----------------------
button_del1.setGeometry(300,190,200,50)
button_del1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
button_del1.clicked.connect(DeleteMember)
search_button1 = QPushButton('Search',window2)
search_button1.setGeometry(300,80,200,50)
search_button1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
search_button1.clicked.connect(WindowSearch)

def Search():
 searchText = linesearchID.text()
 mycursor.execute("use management")
 mycursor.execute("select * from management where ID = '" + searchText + "'")
 for i in mycursor:
  searchResult.setPlainText("     ID = "+str(i[0]) +"\n      Name = "+str(i[1])+"\n      Date = "+str(i[2])+"\n      Phone = "+str(i[3])+"\n      Address = "+str(i[4]))
def Update():
    val_update_name = lineupdate1.text()
    val_update_date = lineupdate2.text()
    val_update_phone = lineupdate3.text()
    val_update_address = lineupdate4.text()
    id_update = lineID.text()

    mycursor.execute("use management")
    sqlx = "update management set Name=%s,Date=%s,Phone=%s,Address=%s where ID = "+id_update
    valuesx = (val_update_name,val_update_date,val_update_phone,val_update_address)
    mycursor.execute(sqlx,valuesx)
    mydb.commit()
def createNew():
    name = lineNewName1.text()
    date = lineNewDate1.text()
    phone = lineNewPhone1.text()
    address = lineNewAddress1.text()
    mycursor.execute("use management")
    sql = "insert into management(Name,Date,Phone,Address) values(%s,%s,%s,%s)"
    values = (name,date,phone,address)
    mycursor.execute(sql,values)
    mydb.commit()
def Delete():
 DeletedID = lineeditDelete.text()
 mycursor.execute("use management")
 mycursor.execute("delete from management where ID = '" + DeletedID + "'")
 mydb.commit()


linesearchID = QLineEdit(window_search) # ----------------------------- Name value
linesearchID.setGeometry(310,140,200,30)
linesearchID.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
button_GoSearch = QPushButton('Search',window_search)
button_GoSearch.setGeometry(310,190,200,50)
button_GoSearch.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
button_GoSearch.clicked.connect(Search)
searchLabel = QLabel('Type the ID',window_search)
searchLabel.setGeometry(380,155,240,50)
searchLabel.setStyleSheet("color:white")
searchResult = QPlainTextEdit(window_search)
searchResult.setGeometry(275,320,270,200)
searchResult.setStyleSheet("border-radius:25px;font-size:20px;color:black;")
searchLabel = QLabel('Results',window_search)
searchLabel.setGeometry(375,275,240,50)
searchLabel.setStyleSheet("color:white;font-size:25px")



buttonDelete = QPushButton('Delete',windowdelete)
buttonDelete.clicked.connect(Delete)
buttonDelete.setGeometry(310,200,200,50)
buttonDelete.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")
lineeditDelete = QLineEdit(windowdelete)
lineeditDelete.setGeometry(310,150,200,30)
lineeditDelete.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
label = QLabel('Delete ID', windowdelete)
label.move(390, 130)
label.setStyleSheet("color:white")

lineNewName1 = QLineEdit(windownew) # ----------------------------- Name value
lineNewName1.setGeometry(310,150,190,30)
lineNewName1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineNewDate1 = QLineEdit(windownew) # ----------------------------- Date value
lineNewDate1.setGeometry(310,200,190,30)
lineNewDate1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineNewPhone1 = QLineEdit(windownew) # ----------------------------- Phone Number value
lineNewPhone1.setGeometry(310,250,190,30)
lineNewPhone1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineNewAddress1 = QLineEdit(windownew) # ----------------------------- Address value
lineNewAddress1.setGeometry(310,300,190,30)
lineNewAddress1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
label1 = QLabel('Name',windownew)
label1.move(200,160)
label1.setStyleSheet("color:white;font-size:15px;")
label1.show()
label2 = QLabel('Date',windownew)
label2.move(200,210)
label2.setStyleSheet("color:white;font-size:15px;")
label2.show()
label2 = QLabel('Phone Number',windownew)
label2.move(200,260)
label2.setStyleSheet("color:white;font-size:15px;")
label2.show()
label2 = QLabel('Address',windownew)
label2.move(200,310)
label2.setStyleSheet("color:white;font-size:15px;")
label2.show()
buttonCreateMember = QPushButton('Create', windownew)
buttonCreateMember.setGeometry(280, 360, 240, 50)
buttonCreateMember.clicked.connect(createNew)
buttonCreateMember.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:20px;font-size:20px;color:black;")

# -------------------------------------------------------------------------------------------------------------------------------
button_update = QPushButton('Update',windowedit)
button_update.setGeometry(330,350,200,50)
button_update.clicked.connect(Update)
button_update.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:25px;font-size:20px;color:black;")

lineupdate1 = QLineEdit(windowedit) # -----------------------------New  Name value
lineupdate1.setGeometry(330,150,200,35)
lineupdate1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineupdate2 = QLineEdit(windowedit) # -----------------------------New Date value ------------------- UPDATE --------------------
lineupdate2.setGeometry(330,200,200,35)
lineupdate2.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineupdate3 = QLineEdit(windowedit) # -----------------------------New Phone Number value
lineupdate3.setGeometry(330,250,200,35)
lineupdate3.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineupdate4 = QLineEdit(windowedit) # -----------------------------New address value
lineupdate4.setGeometry(330,300,200,35)
lineupdate4.setStyleSheet("border-radius:15px;font-size:20px;color:black;")

lineID = QLineEdit(windowedit)
lineID.setGeometry(330,100,200,35)
lineID.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
label1 = QLabel('Enter ID ',windowedit)
label1.move(220,110)
label1.setStyleSheet("color:white")

label1 = QLabel('New Name',windowedit)
label1.move(220,160)
label1.setStyleSheet("color:white")
label1.show()
label2 = QLabel('New Date',windowedit)
label2.move(220,210)
label2.setStyleSheet("color:white")
label2.show()
label2 = QLabel('New PhoneNumber',windowedit)
label2.move(220,260)
label2.setStyleSheet("color:white")
label2.show()
label2 = QLabel('New Address',windowedit)
label2.move(220,310)
label2.setStyleSheet("color:white")
label2.show()






























window1.show()
x.exec_()
