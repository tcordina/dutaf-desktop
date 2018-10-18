# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from src.Controllers import ArticleController
from src.Repositories import FournisseurRepository


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidgetArticles = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetArticles.setGeometry(QtCore.QRect(0, 0, 711, 531))
        self.tabWidgetArticles.setObjectName("tabWidgetArticles")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEditArticleName = QtWidgets.QLineEdit(self.tab)
        self.lineEditArticleName.setGeometry(QtCore.QRect(140, 410, 171, 20))
        self.lineEditArticleName.setObjectName("lineEditArticleName")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(80, 414, 47, 13))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 454, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(363, 413, 47, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.doubleSpinBoxArticlePrix = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxArticlePrix.setGeometry(QtCore.QRect(140, 450, 171, 22))
        self.doubleSpinBoxArticlePrix.setObjectName("doubleSpinBoxArticlePrix")
        self.spinBoxArticleQuant = QtWidgets.QSpinBox(self.tab)
        self.spinBoxArticleQuant.setGeometry(QtCore.QRect(423, 409, 171, 22))
        self.spinBoxArticleQuant.setObjectName("spinBoxArticleQuant")
        self.pushButtonArticle = QtWidgets.QPushButton(self.tab)
        self.pushButtonArticle.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButtonArticle.setObjectName("pushButtonArticle")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 450, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.comboBoxArticleFournisseur = QtWidgets.QComboBox(self.tab)
        self.comboBoxArticleFournisseur.setGeometry(QtCore.QRect(423, 449, 171, 22))
        self.comboBoxArticleFournisseur.setObjectName("comboBoxArticleFournisseur")
        fournisseurs = FournisseurRepository.find_all()
        for four in fournisseurs:
            self.comboBoxArticleFournisseur.addItem(four[1], int(four[0]))
        self.tableViewArticles = QtWidgets.QTableView(self.tab)
        self.tableViewArticles.setGeometry(QtCore.QRect(20, 10, 661, 381))
        self.tableViewArticles.setObjectName("tableViewArticles")
        self.tabWidgetArticles.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButtonFour = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonFour.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButtonFour.setObjectName("pushButtonFour")
        self.tableViewFours = QtWidgets.QTableView(self.tab_2)
        self.tableViewFours.setGeometry(QtCore.QRect(20, 10, 661, 421))
        self.tableViewFours.setObjectName("tableViewFours")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(110, 450, 47, 13))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.lineEditFourName = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditFourName.setGeometry(QtCore.QRect(170, 446, 171, 20))
        self.lineEditFourName.setObjectName("lineEditFourName")
        self.lineEditFourVille = QtWidgets.QLineEdit(self.tab_2)
        self.lineEditFourVille.setGeometry(QtCore.QRect(420, 446, 171, 20))
        self.lineEditFourVille.setObjectName("lineEditFourVille")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(360, 450, 47, 13))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.tabWidgetArticles.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidgetArticles.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''
        self.tableViewArticles.setItem(0, 0, "ID")
        self.tableViewArticles.setItem(0, 1, "Nom")
        self.tableViewArticles.setItem(0, 2, "Prix")
        self.tableViewArticles.setItem(0, 3, "Quantité")
        self.tableViewArticles.setItem(0, 4, "fournisseur")
        '''

        self.pushButtonArticle.clicked.connect(self.addArticle)

    def addArticle(self):
        ArticleController.new_article(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Allo"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Prix"))
        self.label_3.setText(_translate("MainWindow", "Quantité"))
        self.pushButtonArticle.setText(_translate("MainWindow", "Ajouter"))
        self.label_4.setText(_translate("MainWindow", "Fournisseur"))
        self.tabWidgetArticles.setTabText(self.tabWidgetArticles.indexOf(self.tab),
                                          _translate("MainWindow", "Articles"))
        self.pushButtonFour.setText(_translate("MainWindow", "Ajouter"))
        self.label_6.setText(_translate("MainWindow", "Nom"))
        self.label_7.setText(_translate("MainWindow", "Ville"))
        self.tabWidgetArticles.setTabText(self.tabWidgetArticles.indexOf(self.tab_2),
                                          _translate("MainWindow", "Fournisseurs"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
