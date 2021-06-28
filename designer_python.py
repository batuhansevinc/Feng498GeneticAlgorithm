from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 864)
        MainWindow.setStyleSheet("background: \"#3c3f41\"")
        myFont = QtGui.QFont()
        myFont.setBold(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 460, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(myFont)
        self.label_4.setStyleSheet("color: \"#afb1b3\"")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 500, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(myFont)
        self.label_5.setStyleSheet("color: \"#afb1b3\"")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 460, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(myFont)
        self.label_6.setStyleSheet("color: \"#afb1b3\"")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 500, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(myFont)
        self.label_7.setStyleSheet("color: \"#afb1b3\"")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(125, 460, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background: \"#afb1b3\"")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(125, 500, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setStyleSheet("background: \"#afb1b3\"")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 460, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setStyleSheet("background: \"#afb1b3\"")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(315, 500, 86, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setStyleSheet("background: \"#afb1b3\"")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 450, 160, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(myFont)
        self.pushButton.setStyleSheet("background: \"#afb1b3\"")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(670, 30, 131, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.frame.setStyleSheet("color: \"#afb1b3\"")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(myFont)
        self.label_2.setObjectName("label_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 70, 83, 18))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 40, 110, 18))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 100, 83, 18))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 130, 83, 18))
        self.radioButton_7.setObjectName("radioButton_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(679, 200, 131, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setStyleSheet("color: \"#afb1b3\"")
        self.frame_2.setObjectName("frame_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 90, 83, 18))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 60, 83, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 30, 101, 18))
        self.radioButton.setObjectName("radioButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 450, 160, 71))
        self.pushButton_2.setObjectName("pushButton_3")
        self.pushButton_2.setFont(myFont)
        self.pushButton_2.setStyleSheet("background: \"#afb1b3\"")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 0, 20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(myFont)
        self.pushButton_3.setStyleSheet("background: \"#afb1b3\"")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(104, 0, 20, 20))
        self.pushButton_5.setObjectName("pushButton_3")
        self.pushButton_5.setFont(myFont)
        self.pushButton_5.setStyleSheet("background: \"#afb1b3\"")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(314, 459, 25, 22))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(myFont)
        self.pushButton_4.setStyleSheet("background: \"#afb1b3\"")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(458, 520, 330, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color: \"#afb1b3\"")
        self.textBrowser_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 580, 801, 231))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 550, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("color: \"#afb1b3\"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAdvanced = QtWidgets.QMenu(self.menubar)
        self.menuAdvanced.setObjectName("menuAdvanced")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuAdvanced.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.setStyleSheet("background: \"#afb1b3\"")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 651, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tab.setStyleSheet("background: \"#afb1b3\"")
        self.tabWidget.setStyleSheet("background: \"#afb1b3\"")
        self.lineEdit_5 = QtWidgets.QPlainTextEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 0, 645, 395))
        self.lineEdit_5.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setStyleSheet("background: \"#afb1b3\"")
        self.lineEdit_9 = QtWidgets.QPlainTextEdit(self.tab_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(0, 0, 645, 395))
        self.lineEdit_9.setObjectName("plainTextEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget.setCurrentIndex(0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.radioButton_6)
        MainWindow.setTabOrder(self.radioButton_6, self.radioButton_7)
        MainWindow.setTabOrder(self.radioButton_7, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GeNetic Algorithm Wizard -> GNAW"))
        self.label_4.setText(_translate("MainWindow", "Population Limit :"))
        self.label_5.setText(_translate("MainWindow", "Generation Limit : "))
        self.label_6.setText(_translate("MainWindow", "Fitness Score :"))
        self.label_7.setText(_translate("MainWindow", "Mutation % :"))
        self.pushButton.setText(_translate("MainWindow", "Save Code"))
        self.label_2.setText(_translate("MainWindow", "Selection Type"))
        self.radioButton_4.setText(_translate("MainWindow", "Tournament"))
        self.radioButton_5.setText(_translate("MainWindow", "Random"))
        self.radioButton_6.setText(_translate("MainWindow", "Rank"))
        self.radioButton_7.setText(_translate("MainWindow", "Roulette"))
        self.radioButton_3.setText(_translate("MainWindow", "Uniform"))
        self.radioButton_2.setText(_translate("MainWindow", "Multi Point"))
        self.label.setText(_translate("MainWindow", "CrossOver Type"))
        self.radioButton.setText(_translate("MainWindow", "Single Point"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_3.setText(_translate("MainWindow", "⟳"))
        self.pushButton_5.setText(_translate("MainWindow", "⟳"))
        self.pushButton_4.setText(_translate("MainWindow", ">"))
        self.label_9.setText(_translate("MainWindow", "You must save your code before you START"))
        self.label_10.setText(_translate("MainWindow", "Output:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAdvanced.setTitle(_translate("MainWindow", "Advanced"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Fitness Code"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Generate Ind"))
