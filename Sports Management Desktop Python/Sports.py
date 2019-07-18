import sys
from PyQt5.QtWidgets  import QApplication,QWidget,QPushButton,QLineEdit,QMessageBox,QLabel,QTabWidget
import mysql.connector
from time import sleep

mydb = mysql.connector.connect(host="localhost",user="root",password="root@01060744077")
mycursor = mydb.cursor()

x = QApplication(sys.argv)

window1 = QWidget()
window1.setGeometry(100,200,500,500)
window1.setWindowTitle('Sports Club Management')

window2 = QWidget()
window2.setGeometry(100,200,500,500)
window2.setWindowTitle('Sports Club Management')

windownew = QWidget() # ---------------------------- New member window
windownew.setGeometry(100,200,500,500)
windownew.setWindowTitle('Sports Club Management')

window_search = QWidget() # ---------------------------- Search window
window_search.setGeometry(100,200,500,500)
window_search.setWindowTitle('Sports Club Management')

windowdelete = QWidget() # ------------------------- Delete member window
windowdelete.setGeometry(100,200,500,500)
windowdelete.setWindowTitle('Sports Club Management')
windowedit = QWidget() # --------------------------- Edit member window
windowedit.setGeometry(100,200,500,500)
windowedit.setWindowTitle('Sports Club Management')

lineEdit1 = QLineEdit(window1) # ------------------- user name
lineEdit1.setGeometry(160,150,190,30)
lineEdit2 = QLineEdit(window1) # ------------------- password
lineEdit2.setGeometry(160,200,190,30)
# ......................................................................................................................

label1 = QLabel('UserName',window1)
label1.move(100,160)
label1.show()

label2 = QLabel('Password',window1)
label2.move(100,210)
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
 Logbutton.setGeometry(180,250,150,30)
 Logbutton.clicked.connect(lineEditLogin)



tab = QTabWidget(window2)
tab.setGeometry(1, 1, 1500, 1500)
t1 = QWidget()
t2 = QWidget()
tab.addTab(t1, 'Swimming')  # Tab of Swimming sport
tab.addTab(t2, 'Football')  # Tab of Football sport

button_new1 = QPushButton('New Member',t1) # new member of tab1
button_new1.setGeometry(150,280,200,50)
button_new1.clicked.connect(NewMember)
button_edit1 = QPushButton('Update Member',t1) # edit of of tab1
button_edit1.setGeometry(150,220,200,50)
button_edit1.clicked.connect(EditMember)
button_del1 = QPushButton('Delete Member',t1) # delete member of tab1
button_del1.setGeometry(150,160,200,50)
button_del1.clicked.connect(DeleteMember)
button_new2 = QPushButton('New Member',t2)
button_new2.setGeometry(150,280,200,50)
button_new2.clicked.connect(NewMember)
button_edit2 = QPushButton('Update Member',t2)
button_edit2.setGeometry(150,220,200,50)
button_edit2.clicked.connect(EditMember)
button_del2 = QPushButton('Delete Member',t2)
button_del2.setGeometry(150,160,200,50)
button_del2.clicked.connect(DeleteMember)

search_button1 = QPushButton('Search',t1)
search_button1.setGeometry(150,50,200,50)
search_button1.clicked.connect(WindowSearch)
search_button2 = QPushButton('Search',t2)
search_button2.setGeometry(150,50,200,50)
search_button2.clicked.connect(WindowSearch)
linesearchID = QLineEdit(window_search) # ----------------------------- Name value
linesearchID.setGeometry(160,140,200,30)
button_GoSearch = QPushButton('Search',window_search)
button_GoSearch.setGeometry(160,190,200,50)
button_GoSearch.clicked.connect(Search)

searchLabel = QLabel('Type the ID',window_search)
searchLabel.setGeometry(230,155,240,50)


buttonDelete = QPushButton('Delete',windowdelete)
buttonDelete.clicked.connect(Delete)
buttonDelete.setGeometry(160,200,200,50)
lineeditDelete = QLineEdit(windowdelete)
lineeditDelete.setGeometry(160,150,200,30)
label = QLabel('Delete ID', windowdelete)
label.move(240, 130)

lineNewName1 = QLineEdit(windownew) # ----------------------------- Name value
lineNewName1.setGeometry(160,150,190,30)
lineNewDate1 = QLineEdit(windownew) # ----------------------------- Date value
lineNewDate1.setGeometry(160,200,190,30)
lineNewPhone1 = QLineEdit(windownew) # ----------------------------- Phone Number value
lineNewPhone1.setGeometry(160,250,190,30)
label1 = QLabel('Name',windownew)
label1.move(70,160)
label1.show()
label2 = QLabel('Date',windownew)
label2.move(70,210)
label2.show()
label2 = QLabel('Phone Number',windownew)
label2.move(70,260)
label2.show()
buttonCreateMember = QPushButton('Create', windownew)
buttonCreateMember.setGeometry(180, 300, 150, 30)
buttonCreateMember.clicked.connect(createNew)

# -------------------------------------------------------------------------------------------------------------------------------
button_update = QPushButton('Update',windowedit)
button_update.setGeometry(150,300,200,50)
button_update.clicked.connect(Update)
lineupdate1 = QLineEdit(windowedit) # -----------------------------New  Name value
lineupdate1.setGeometry(180,150,190,30)
lineupdate2 = QLineEdit(windowedit) # -----------------------------New Date value ------------------- UPDATE --------------------
lineupdate2.setGeometry(180,200,190,30)
lineupdate3 = QLineEdit(windowedit) # -----------------------------New Phone Number value
lineupdate3.setGeometry(180,250,190,30)
# -------------------------------------------------------------------------------------------------------------------------------

lineID = QLineEdit(windowedit)
lineID.setGeometry(180,100,190,30)
label1 = QLabel('Enter ID ',windowedit)
label1.move(70,110)

label1 = QLabel('New Name',windowedit)
label1.move(70,160)
label1.show()
label2 = QLabel('New Date',windowedit)
label2.move(70,210)
label2.show()
label2 = QLabel('New PhoneNumber',windowedit)
label2.move(70,260)
label2.show()





























window1.show()
x.exec_()
