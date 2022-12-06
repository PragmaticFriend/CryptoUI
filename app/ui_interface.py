# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomStackedWidget

import QSS_Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 545)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget, #tableBtn, #mainBodyContent{\n"
"	background-color: #323232;\n"
"}\n"
"#header, #mainBody, #rightMenu{\n"
"	background-color: #1e1e1e;\n"
"}\n"
"\n"
"#pushButton{\n"
"	border: 1px solid #cc5bce;\n"
"    border-radius: 19px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"    padding: 5px 10px;\n"
"    border-top-left-radius: 5px;\n"
"    border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Inter")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(800, 397))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = QWidget(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(150, 0))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tableBtn = QPushButton(self.frame_3)
        self.tableBtn.setObjectName(u"tableBtn")
        font1 = QFont()
        font1.setFamily(u"Inter")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setWeight(50)
        self.tableBtn.setFont(font1)
        self.tableBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/Icons/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableBtn.setIcon(icon)

        self.verticalLayout_4.addWidget(self.tableBtn)

        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font1)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.settingsBtn)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.aboutBtn = QPushButton(self.frame_4)
        self.aboutBtn.setObjectName(u"aboutBtn")
        font2 = QFont()
        font2.setFamily(u"Inter")
        font2.setPointSize(8)
        self.aboutBtn.setFont(font2)
        self.aboutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.aboutBtn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.aboutBtn)


        self.verticalLayout_6.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.tablePage = QWidget()
        self.tablePage.setObjectName(u"tablePage")
        self.verticalLayout_7 = QVBoxLayout(self.tablePage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.tablePage)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget_3 = QWidget(self.splitter)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_9 = QVBoxLayout(self.widget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.frame_5 = QFrame(self.widget_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamily(u"Inter")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.splitter.addWidget(self.widget_3)
        self.rightMenu = QWidget(self.splitter)
        self.rightMenu.setObjectName(u"rightMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rightMenu.sizePolicy().hasHeightForWidth())
        self.rightMenu.setSizePolicy(sizePolicy1)
        self.rightMenu.setMinimumSize(QSize(200, 210))
        self.rightMenu.setMaximumSize(QSize(800, 16777215))
        self.rightMenu.setFont(font2)
        self.verticalLayout_8 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 60, 10, 20)
        self.frame_7 = QFrame(self.rightMenu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setSpacing(20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(10, 0, 0, 0)
        self.login_2 = QLineEdit(self.frame_7)
        self.login_2.setObjectName(u"login_2")
        self.login_2.setFont(font2)

        self.verticalLayout_14.addWidget(self.login_2)

        self.passLength_2 = QLineEdit(self.frame_7)
        self.passLength_2.setObjectName(u"passLength_2")
        self.passLength_2.setFont(font2)

        self.verticalLayout_14.addWidget(self.passLength_2)

        self.useNumeric_2 = QCheckBox(self.frame_7)
        self.useNumeric_2.setObjectName(u"useNumeric_2")
        self.useNumeric_2.setFont(font2)

        self.verticalLayout_14.addWidget(self.useNumeric_2)

        self.useUpperCase_2 = QCheckBox(self.frame_7)
        self.useUpperCase_2.setObjectName(u"useUpperCase_2")
        self.useUpperCase_2.setFont(font2)

        self.verticalLayout_14.addWidget(self.useUpperCase_2)

        self.useSpecCharacters_2 = QCheckBox(self.frame_7)
        self.useSpecCharacters_2.setObjectName(u"useSpecCharacters_2")
        self.useSpecCharacters_2.setFont(font2)

        self.verticalLayout_14.addWidget(self.useSpecCharacters_2)

        self.addPassBtn = QPushButton(self.frame_7)
        self.addPassBtn.setObjectName(u"addPassBtn")
        font4 = QFont()
        font4.setFamily(u"Inter")
        font4.setPointSize(8)
        font4.setBold(True)
        font4.setWeight(75)
        self.addPassBtn.setFont(font4)
        self.addPassBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addPassBtn.setIcon(icon3)
        self.addPassBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_14.addWidget(self.addPassBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_8.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.splitter.addWidget(self.rightMenu)

        self.horizontalLayout_7.addWidget(self.splitter)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.mainPages.addWidget(self.tablePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_12 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_5 = QWidget(self.settingsPage)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.widget_4 = QWidget(self.widget_5)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.verticalLayout_13 = QVBoxLayout(self.widget_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout_13.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.rootPassword = QLineEdit(self.widget_6)
        self.rootPassword.setObjectName(u"rootPassword")
        self.rootPassword.setFont(font2)

        self.horizontalLayout_3.addWidget(self.rootPassword)

        self.saveRootPasswordBtn = QPushButton(self.widget_6)
        self.saveRootPasswordBtn.setObjectName(u"saveRootPasswordBtn")
        self.saveRootPasswordBtn.setFont(font2)
        self.saveRootPasswordBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.saveRootPasswordBtn)


        self.verticalLayout_13.addWidget(self.widget_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.widget_5)

        self.mainPages.addWidget(self.settingsPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.verticalLayout_15 = QVBoxLayout(self.aboutPage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_7 = QWidget(self.aboutPage)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_16 = QVBoxLayout(self.widget_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.verticalLayout_16.addWidget(self.label_4)

        self.label_8 = QLabel(self.widget_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_8)

        self.label_7 = QLabel(self.widget_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_7)


        self.horizontalLayout_9.addWidget(self.widget_8)

        self.label_9 = QLabel(self.widget_7)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setPointSize(6)
        self.label_9.setFont(font5)
        self.label_9.setText(u"")
        self.label_9.setPixmap(QPixmap(u"data/img/me.jpg"))
        self.label_9.setScaledContents(False)

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_15.addWidget(self.widget_7)

        self.mainPages.addWidget(self.aboutPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainBodyContent)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        sizePolicy2.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy2)
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.footer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u041f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.tableBtn.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.aboutBtn.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0421\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None));
        self.login_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.passLength_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u041f\u0430\u0440\u043e\u043b\u044f", None))
        self.useNumeric_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0438\u0444\u0440\u044b", None))
        self.useUpperCase_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u043b\u0430\u0432\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b", None))
        self.useSpecCharacters_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446. \u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.addPassBtn.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0417\u0430\u043f\u0438\u0441\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0442\u0435\u0440-\u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.rootPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u043e\u0432\u044b\u0439 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.saveRootPasswordBtn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TG: https://t.me/rasim50", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440: \u041d\u0443\u0440\u0430\u043b\u0438\u0435\u0432 \u0420.\u0420.", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0443\u0440\u0430\u043b\u0438\u0435\u0432 \u0420.\u0420 \u041f\u041819-4", None))
    # retranslateUi

