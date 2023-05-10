import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap
import sqlite3


class loginscreen(QDialog):
    def __init__(self):
        super(loginscreen,self).__init__()
        loadUi("Loginpaage.ui",self)
        self.pushButton_2.clicked.connect(self.gotoregistration)
        self.pushButton.clicked.connect(self.loginfunction)



    def loginfunction(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if len(username)==0 or len(password)==0:
            self.label_2.setText("Please input all fields.")
        elif username == "admin" and password == "admin":
            self.label_2.setText("")
            
        else:
            conn = sqlite3.connect("shop_data.db")
            cur = conn.cursor()
            query = 'SELECT password FROM login_info WHERE username =\''+username+"\'"
            cur.execute(query)
            result = cur.fetchone()
            if result is not None and result[0] == password:
                print("Successfully logged in.")
                self.label_2.setText("")           
                
            else:
                self.label_2.setText("Invalid username or password.") 

                                                                    
    
      

    def gotoregistration(self):
        registration = registrationscreen()
        Widget.addWidget(registration)
        Widget.setCurrentIndex(Widget.currentIndex()+1)

    


  


class registrationscreen(QDialog):
    def __init__(self):
        super(registrationscreen, self).__init__()
        loadUi("registration.ui", self)
        self.pushButton_2.clicked.connect(self.gotologin)
        self.pushButton.clicked.connect(self.registrationfunction)



    def registrationfunction(self):
            username = self.lineEdit_2.text()
            email =  self.lineEdit.text()
            pass1 = self.lineEdit_4.text()
            pass2 = self.lineEdit_3.text()

            if len(username)==0 or len(pass1)==0 or len(pass2)==0 or len(email)==0 :
                self.label_2.setText("Please fill in all inputs.")

            elif pass1 != pass2:
                self.label_2.setText("Passwords do not match.")

            elif len(pass1) < 8:
                self.label_2.setText("Password should have at least 8 characters.")
            
            elif not any(char in '!@#$%^&*()-+' for char in pass1):
                self.label_2.setText("Password should have at least one special character.")

            elif email.endswith("@gmail.com") == False:
                self.label_2.setText("Invalid email address.")

            else:
                conn = sqlite3.connect("shop_data.db")
                cur = conn.cursor()
                user_info = [username , pass1 , email]
                cur.execute('INSERT INTO login_info (username,password,email) VALUES(?,?,?)',user_info)
                self.label_2.setText("")
                self.gotoSearch()
                conn.commit()
                conn.close()
                self.gotoproduct()
                
              


    def gotologin(self):
        login = loginscreen()
        Widget.addWidget(login)
        Widget.setCurrentIndex(Widget.currentIndex()-1)


 







#main
app = QApplication(sys.argv)
log=loginscreen()
Widget = QtWidgets.QStackedWidget()
Widget.addWidget(log)
Widget.setFixedSize(1200,900)
Widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")




