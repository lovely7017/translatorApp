# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translate.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import sys
import googletrans
import textblob
import pyttsx3



class Ui_MainWindow(object):
    def  translate1(self):
        for key,value in self.languages.items():
                if(value == self.comboBox.currentText()):
                    from_language_key = key 
        for key,value in self.languages.items():
                if(value == self.comboBox_2.currentText()):
                    to_language_key = key 

        #self.textEdit.setText(from_language_key)
        #self.textEdit_2.setText(to_language_key)

            #turn origional text into textblob
        words = textblob.TextBlob(self.textEdit.toPlainText())
        words = words.translate(from_lang = from_language_key,to=to_language_key)
        self.textEdit_2.setText(str(words))

        #intialize the search engine
        engine = pyttsx3.init()

        #pass words to speak
        engine.say(words)

        #run engine
        engine.runAndWait()
        
       




       # except Exception as e:
        #    QMessageBox.about(self,"Translate",str(e))
        
    def clear1(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.comboBox.setCurrentText("english")
        self.comboBox.setCurrentText("german")


        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        #add language to combo box
        self.languages = googletrans.LANGUAGES
        #convert to list
        self.language_list = list(self.languages.values())
        #add item to comobo




        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(23, 26, 271, 301))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(483, 26, 271, 301))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.translate1())
        self.pushButton.setGeometry(QtCore.QRect(310, 110, 151, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        #add languages to combo box
        self.comboBox.addItems(self.language_list)
        self.comboBox.setCurrentText("english")
        self.comboBox.setGeometry(QtCore.QRect(22, 372, 271, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        #add languages to combo box
        self.comboBox_2.addItems(self.language_list)
        self.comboBox_2.setCurrentText("german")

        self.comboBox_2.setGeometry(QtCore.QRect(480, 370, 271, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda : self.clear1())
        self.pushButton_2.setGeometry(QtCore.QRect(340, 260, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Translate"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
