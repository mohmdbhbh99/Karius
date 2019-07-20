import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QPushButton,QLineEdit,QMessageBox,QLabel,QTabWidget
import mysql.connector
from PyQt5.QtGui import QPixmap


mydb = mysql.connector.connect(host="localhost",user="root",password="root@01060744077")
mycursor = mydb.cursor()

x = QApplication(sys.argv)


window1 = QWidget()
window1.setFixedSize(820,600)
window1.setWindowTitle('Sports Club Management')
labelPicture = QLabel(window1)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)


window2 = QWidget()
window2.setFixedSize(820,600)
window2.setWindowTitle('Sports Club Management')
labelPicture = QLabel(window2)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

windownew = QWidget() # ---------------------------- New member window
windownew.setFixedSize(820,600)
windownew.setWindowTitle('Sports Club Management')
labelPicture = QLabel(windownew)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

window_search = QWidget() # ---------------------------- Search window
window_search.setFixedSize(820,600)
window_search.setWindowTitle('Sports Club Management')
labelPicture = QLabel(window_search)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

windowdelete = QWidget() # ------------------------- Delete member window
windowdelete.setFixedSize(820,600)
windowdelete.setWindowTitle('Sports Club Management')
labelPicture = QLabel(windowdelete)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

windowedit = QWidget() # --------------------------- Edit member window
windowedit.setFixedSize(820,600)
windowedit.setWindowTitle('Sports Club Management')
labelPicture = QLabel(windowedit)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(1,1,2000,800)

lineEdit1 = QLineEdit(window1) # ------------------- user name
lineEdit1.setGeometry(310,150,190,30)
lineEdit1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineEdit2 = QLineEdit(window1) # ------------------- password
lineEdit2.setGeometry(310,200,190,30)
lineEdit2.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
# ......................................................................................................................

label1 = QLabel('UserName',window1)
label1.move(250,160)
label1.show()
label1.setStyleSheet("color:white;")


label2 = QLabel('Password',window1)
label2.move(250,210)
label2.setStyleSheet("color:white;")
label2.show()
# ......................................................................................................................

def lineEditLogin():
    line1msg = lineEdit1.text()
    line2msg = lineEdit2.text()
    if line1msg == str('') and line2msg == str(''): # ---------------------- username and password
        window1.close()
        window2.show()
    else:
        msgboxinf = QMessageBox.information(window1,'Sports','Access Denied , Incorrect Username or Password')
def NewMember():
    windownew.show()
def EditMember():
    windowedit.show()
def DeleteMember():
    windowdelete.show()
def createNew():
    name = lineNewName1.text()
    date = lineNewDate1.text()
    phone = lineNewPhone1.text()
    mycursor.execute("use Sports")
    sql = "insert into sports(Name,Date,PhoneNumber) values(%s,%s,%s)"
    values = (name,date,phone)
    mycursor.execute(sql,values)
    mydb.commit()
def Delete():
 DeletedID = lineeditDelete.text()
 mycursor.execute("use Sports")
 mycursor.execute("delete from sports where ID = '" + DeletedID + "'")
 mydb.commit()
def WindowSearch():
 window_search.show()
def Search():
 searchText = linesearchID.text()
 mycursor.execute("use Sports")
 mycursor.execute("select * from sports where ID = '" + searchText + "'")
 for i in mycursor:

  msgboxinf2 = QMessageBox.information(window_search, 'Sports', "ID = "+str(i[0]) +"\nName = "+str(i[1])+"\nDate = "+str(i[2])+"\nPhoneNumber = "+str(i[3]))
def Update():
    val_update_name = lineupdate1.text()
    val_update_date = lineupdate2.text()
    val_update_phone = lineupdate3.text()
    id_update = lineID.text()

    mycursor.execute("use Sports")
    sqlx = "update sports set Name=%s,Date=%s,PhoneNumber=%s where ID = "+id_update
    valuesx = (val_update_name,val_update_date,val_update_phone)
    mycursor.execute(sqlx,valuesx)
    mydb.commit()

class Login_Button():

 Logbutton = QPushButton('Login',window1)
 Logbutton.move(210,250)
 Logbutton.setGeometry(330,250,150,30)
 Logbutton.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
 Logbutton.clicked.connect(lineEditLogin)



tab = QTabWidget(window2)
tab.setGeometry(0, 0, 1500, 1500)
t1 = QWidget()
labelPicture = QLabel(t1)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(0,0,2000,800)

t2 = QWidget()
labelPicture = QLabel(t2)
Pic = QPixmap('Fabric.jpg')
labelPicture.setPixmap(Pic)
labelPicture.setGeometry(0,0,2000,800)
tab.addTab(t1, 'Swimming')  # Tab of Swimming sport
tab.addTab(t2, 'Football')  # Tab of Football sport

# --------------------------------------------------------------------------------------------

button_new1 = QPushButton('New Member',t1) # new member of tab1
button_new1.setGeometry(300,280,200,50)
button_new1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_new1.clicked.connect(NewMember)
button_edit1 = QPushButton('Update Member',t1) # edit of of tab1
button_edit1.setGeometry(300,220,200,50)
button_edit1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_edit1.clicked.connect(EditMember)
button_del1 = QPushButton('Delete Member',t1) # delete member of tab1 ---------------------------------- TAB 1-----------------------
button_del1.setGeometry(300,160,200,50)
button_del1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_del1.clicked.connect(DeleteMember)
search_button1 = QPushButton('Search',t1)
search_button1.setGeometry(300,50,200,50)
search_button1.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
search_button1.clicked.connect(WindowSearch)

button_new2 = QPushButton('New Member',t2) # new member of tab1
button_new2.setGeometry(300,280,200,50)
button_new2.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_new2.clicked.connect(NewMember)
button_edit2 = QPushButton('Update Member',t2) # edit of of tab1
button_edit2.setGeometry(300,220,200,50)
button_edit2.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_edit2.clicked.connect(EditMember)
button_del2 = QPushButton('Delete Member',t2) # delete member of tab1 ---------------------------------- TAB 2 --------------------
button_del2.setGeometry(300,160,200,50)
button_del2.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_del2.clicked.connect(DeleteMember)
search_button2 = QPushButton('Search',t2)
search_button2.setGeometry(300,50,200,50)
search_button2.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
search_button2.clicked.connect(WindowSearch)





# --------------------------------------------------------------------------------------------


linesearchID = QLineEdit(window_search) # ----------------------------- Name value
linesearchID.setGeometry(310,140,200,30)
linesearchID.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
button_GoSearch = QPushButton('Search',window_search)
button_GoSearch.setGeometry(310,190,200,50)
button_GoSearch.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
button_GoSearch.clicked.connect(Search)

searchLabel = QLabel('Type the ID',window_search)
searchLabel.setGeometry(380,155,240,50)
searchLabel.setStyleSheet("color:white")


buttonDelete = QPushButton('Delete',windowdelete)
buttonDelete.clicked.connect(Delete)
buttonDelete.setGeometry(310,200,200,50)
buttonDelete.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")
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
label1 = QLabel('Name',windownew)
label1.move(220,160)
label1.setStyleSheet("color:white")
label1.show()
label2 = QLabel('Date',windownew)
label2.move(220,210)
label2.setStyleSheet("color:white")
label2.show()
label2 = QLabel('Phone Number',windownew)
label2.move(220,260)
label2.setStyleSheet("color:white")
label2.show()
buttonCreateMember = QPushButton('Create', windownew)
buttonCreateMember.setGeometry(330, 300, 150, 30)
buttonCreateMember.clicked.connect(createNew)
buttonCreateMember.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")

# -------------------------------------------------------------------------------------------------------------------------------
button_update = QPushButton('Update',windowedit)
button_update.setGeometry(300,300,200,50)
button_update.clicked.connect(Update)
button_update.setStyleSheet("background-color:rgb(136, 252, 165);border-radius:15px;font-size:20px;color:black;")

lineupdate1 = QLineEdit(windowedit) # -----------------------------New  Name value
lineupdate1.setGeometry(330,150,190,30)
lineupdate1.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineupdate2 = QLineEdit(windowedit) # -----------------------------New Date value ------------------- UPDATE --------------------
lineupdate2.setGeometry(330,200,190,30)
lineupdate2.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
lineupdate3 = QLineEdit(windowedit) # -----------------------------New Phone Number value
lineupdate3.setGeometry(330,250,190,30)
lineupdate3.setStyleSheet("border-radius:15px;font-size:20px;color:black;")
# -------------------------------------------------------------------------------------------------------------------------------

lineID = QLineEdit(windowedit)
lineID.setGeometry(330,100,190,30)
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



























window1.show()
x.exec_()
