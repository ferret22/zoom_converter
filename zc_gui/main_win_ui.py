# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_win.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_zc_main(object):
    def setupUi(self, zc_main):
        if not zc_main.objectName():
            zc_main.setObjectName(u"zc_main")
        zc_main.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(zc_main.sizePolicy().hasHeightForWidth())
        zc_main.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        zc_main.setFont(font)
        self.centralwidget = QWidget(zc_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.text_ = QTextEdit(self.centralwidget)
        self.text_.setObjectName(u"text_")
        self.text_.setGeometry(QRect(10, 70, 781, 361))
        self.text_.setAutoFillBackground(False)
        self.text_.setReadOnly(True)
        self.button_convert = QPushButton(self.centralwidget)
        self.button_convert.setObjectName(u"button_convert")
        self.button_convert.setGeometry(QRect(610, 450, 171, 81))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 781, 51))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.path_line = QLineEdit(self.widget)
        self.path_line.setObjectName(u"path_line")

        self.horizontalLayout.addWidget(self.path_line)

        zc_main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(zc_main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        zc_main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(zc_main)
        self.statusbar.setObjectName(u"statusbar")
        zc_main.setStatusBar(self.statusbar)

        self.retranslateUi(zc_main)

        QMetaObject.connectSlotsByName(zc_main)
    # setupUi

    def retranslateUi(self, zc_main):
        zc_main.setWindowTitle(QCoreApplication.translate("zc_main", u"Zoom Converter", None))
        self.button_convert.setText(QCoreApplication.translate("zc_main", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0430\u0446\u0438\u044e", None))
        self.label.setText(QCoreApplication.translate("zc_main", u"\u041f\u0443\u0442\u044c \u0434\u043e \u043f\u0430\u043f\u043a\u0438 \u0441 \u0434\u0438\u0440\u0438\u043a\u0442\u043e\u0440\u0438\u044f\u043c\u0438 \u0437\u0430\u043f\u0438\u0441\u0435\u0439:", None))
    # retranslateUi

