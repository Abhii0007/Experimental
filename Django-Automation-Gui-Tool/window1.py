# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form1yjYKJP.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QWidget)

class Ui_master(object):
    def setupUi(self, master):
        if not master.objectName():
            master.setObjectName(u"master")
        master.resize(720, 630)
        master.setStyleSheet(u"background-color: rgb(92, 180, 183);")
        master.setDocumentMode(False)
        self.centralwidget = QWidget(master)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 720, 556))
        self.label.setPixmap(QPixmap(u"back1.png"))
        self.label.setScaledContents(True)
        self.pushButton_runserver = QPushButton(self.centralwidget)
        self.pushButton_runserver.setObjectName(u"pushButton_runserver")
        self.pushButton_runserver.setGeometry(QRect(108, 157, 171, 41))
        font = QFont()
        font.setPointSize(16)
        self.pushButton_runserver.setFont(font)
        self.pushButton_runserver.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_runserver.setStyleSheet(u"background-color: rgb(152, 222, 218);\n"
"selection-background-color: rgb(214, 214, 214);")
        self.pushButton_show_databse = QPushButton(self.centralwidget)
        self.pushButton_show_databse.setObjectName(u"pushButton_show_databse")
        self.pushButton_show_databse.setGeometry(QRect(108, 237, 171, 41))
        self.pushButton_show_databse.setFont(font)
        self.pushButton_show_databse.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_admin = QPushButton(self.centralwidget)
        self.pushButton_admin.setObjectName(u"pushButton_admin")
        self.pushButton_admin.setGeometry(QRect(108, 317, 171, 41))
        self.pushButton_admin.setFont(font)
        self.pushButton_admin.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_open_shell = QPushButton(self.centralwidget)
        self.pushButton_open_shell.setObjectName(u"pushButton_open_shell")
        self.pushButton_open_shell.setGeometry(QRect(108, 397, 171, 41))
        self.pushButton_open_shell.setFont(font)
        self.pushButton_open_shell.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_check = QPushButton(self.centralwidget)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setGeometry(QRect(107, 473, 171, 41))
        self.pushButton_check.setFont(font)
        self.pushButton_check.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_flush_databse = QPushButton(self.centralwidget)
        self.pushButton_flush_databse.setObjectName(u"pushButton_flush_databse")
        self.pushButton_flush_databse.setGeometry(QRect(437, 473, 171, 41))
        self.pushButton_flush_databse.setFont(font)
        self.pushButton_flush_databse.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_make_migration = QPushButton(self.centralwidget)
        self.pushButton_make_migration.setObjectName(u"pushButton_make_migration")
        self.pushButton_make_migration.setGeometry(QRect(437, 237, 171, 41))
        self.pushButton_make_migration.setFont(font)
        self.pushButton_make_migration.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_create_new_app = QPushButton(self.centralwidget)
        self.pushButton_create_new_app.setObjectName(u"pushButton_create_new_app")
        self.pushButton_create_new_app.setGeometry(QRect(437, 157, 171, 41))
        self.pushButton_create_new_app.setFont(font)
        self.pushButton_create_new_app.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_apply_migration = QPushButton(self.centralwidget)
        self.pushButton_apply_migration.setObjectName(u"pushButton_apply_migration")
        self.pushButton_apply_migration.setGeometry(QRect(436, 317, 171, 41))
        self.pushButton_apply_migration.setFont(font)
        self.pushButton_apply_migration.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_show_migration = QPushButton(self.centralwidget)
        self.pushButton_show_migration.setObjectName(u"pushButton_show_migration")
        self.pushButton_show_migration.setGeometry(QRect(436, 397, 171, 41))
        self.pushButton_show_migration.setFont(font)
        self.pushButton_show_migration.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(560, 560, 151, 33))
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(6, 561, 451, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.lineEdit.setMaxLength(1000)
        self.pushButton_open_site = QPushButton(self.centralwidget)
        self.pushButton_open_site.setObjectName(u"pushButton_open_site")
        self.pushButton_open_site.setGeometry(QRect(461, 560, 71, 33))
        self.pushButton_open_site.setFont(font)
        self.pushButton_open_site.setStyleSheet(u"background-color: rgb(152, 222, 218);")
        master.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(master)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 33))
        self.menubar.setStyleSheet(u"background-color: rgb(92, 180, 183);\n"
"color: rgb(255, 255, 255);")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuForm = QMenu(self.menubar)
        self.menuForm.setObjectName(u"menuForm")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        master.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuForm.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(master)

        QMetaObject.connectSlotsByName(master)
    # setupUi

    def retranslateUi(self, master):
        master.setWindowTitle(QCoreApplication.translate("master", u"Django Master v1.0", None))
        self.label.setText("")
        self.pushButton_runserver.setText(QCoreApplication.translate("master", u"Run/Server", None))
        self.pushButton_show_databse.setText(QCoreApplication.translate("master", u"Show Databse", None))
        self.pushButton_admin.setText(QCoreApplication.translate("master", u"Admin", None))
        self.pushButton_open_shell.setText(QCoreApplication.translate("master", u"Open Shell", None))
        self.pushButton_check.setText(QCoreApplication.translate("master", u"Check", None))
        self.pushButton_flush_databse.setText(QCoreApplication.translate("master", u"Flush Databse", None))
        self.pushButton_make_migration.setText(QCoreApplication.translate("master", u"Make migration", None))
        self.pushButton_create_new_app.setText(QCoreApplication.translate("master", u"Create New App", None))
        self.pushButton_apply_migration.setText(QCoreApplication.translate("master", u"Apply Migration", None))
        self.pushButton_show_migration.setText(QCoreApplication.translate("master", u"Show Migrations", None))
        self.pushButton_clear.setText(QCoreApplication.translate("master", u"Clear Console", None))
        self.lineEdit.setText(QCoreApplication.translate("master", u"http://127.0.0.1:8000/", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("master", u"Default URL:-http://127.0.0.1:8000/", None))
        self.pushButton_open_site.setText(QCoreApplication.translate("master", u"Open", None))
        self.menuFile.setTitle(QCoreApplication.translate("master", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("master", u"Edit", None))
        self.menuForm.setTitle(QCoreApplication.translate("master", u"Form", None))
        self.menuAbout.setTitle(QCoreApplication.translate("master", u"About", None))
    # retranslateUi

