# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.true_btn = QPushButton(self.centralwidget)
        self.true_btn.setObjectName(u"true_btn")
        self.true_btn.setGeometry(QRect(110, 130, 81, 26))
        self.false_btn = QPushButton(self.centralwidget)
        self.false_btn.setObjectName(u"false_btn")
        self.false_btn.setGeometry(QRect(220, 130, 81, 26))
        self.and_btn = QPushButton(self.centralwidget)
        self.and_btn.setObjectName(u"and_btn")
        self.and_btn.setGeometry(QRect(330, 130, 81, 26))
        self.or_btn = QPushButton(self.centralwidget)
        self.or_btn.setObjectName(u"or_btn")
        self.or_btn.setGeometry(QRect(450, 130, 81, 26))
        self.eql_btn = QPushButton(self.centralwidget)
        self.eql_btn.setObjectName(u"eql_btn")
        self.eql_btn.setGeometry(QRect(560, 130, 81, 26))
        self.input_label = QLabel(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setGeometry(QRect(110, 80, 49, 16))
        self.output_label = QLabel(self.centralwidget)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setGeometry(QRect(110, 200, 49, 16))
        self.input_text = QLineEdit(self.centralwidget)
        self.input_text.setObjectName(u"input_text")
        self.input_text.setGeometry(QRect(160, 80, 211, 26))
        self.prefix_text = QLineEdit(self.centralwidget)
        self.prefix_text.setObjectName(u"prefix_text")
        self.prefix_text.setGeometry(QRect(220, 260, 201, 26))
        self.prefix_label = QLabel(self.centralwidget)
        self.prefix_label.setObjectName(u"prefix_label")
        self.prefix_label.setGeometry(QRect(110, 260, 81, 16))
        self.output_text = QLineEdit(self.centralwidget)
        self.output_text.setObjectName(u"output_text")
        self.output_text.setGeometry(QRect(170, 200, 71, 26))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.true_btn.setText(QCoreApplication.translate("MainWindow", u"t", None))
        self.false_btn.setText(QCoreApplication.translate("MainWindow", u"f", None))
        self.and_btn.setText(QCoreApplication.translate("MainWindow", u"\u2227", None))
        self.or_btn.setText(QCoreApplication.translate("MainWindow", u"\u2228", None))
        self.eql_btn.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.input_label.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
        self.prefix_label.setText(QCoreApplication.translate("MainWindow", u"Prefix Notation:", None))
    # retranslateUi

