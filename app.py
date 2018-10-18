# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabs.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from src.Controllers import ArticleController, FournisseurController
from src.Repositories import ArticleRepository, FournisseurRepository


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidgetArticles = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetArticles.setGeometry(QtCore.QRect(0, 0, 800, 531))
        self.tabWidgetArticles.setObjectName("tabWidgetArticles")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEditArticleName = QtWidgets.QLineEdit(self.tab)
        self.lineEditArticleName.setGeometry(QtCore.QRect(140, 410, 171, 20))
        self.lineEditArticleName.setObjectName("lineEditArticleName")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(80, 414, 47, 13))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(80, 454, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(363, 413, 47, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.comboBoxArticleFournisseur = QtWidgets.QComboBox(self.tab)
        self.comboBoxArticleFournisseur.setGeometry(QtCore.QRect(423, 449, 171, 22))
        self.comboBoxArticleFournisseur.setObjectName("comboBoxArticleFournisseur")
        self.tableWidgetArticles = QtWidgets.QTableWidget(self.tab)
        self.tableWidgetArticles.setGeometry(QtCore.QRect(7, 10, 800, 371))
        self.tableWidgetArticles.setColumnCount(7)
        self.tableWidgetArticles.setObjectName("tableWidgetArticles")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetArticles.setHorizontalHeaderItem(6, item)
        self.tabWidgetArticles.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButtonFour = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonFour.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButtonFour.setObjectName("pushButtonFour")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(110, 450, 47, 13))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.tableWidgetFours = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidgetFours.setGeometry(QtCore.QRect(7, 10, 800, 411))
        self.tableWidgetFours.setObjectName("tableWidgetFours")
        self.tableWidgetFours.setColumnCount(3)
        self.tableWidgetFours.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(2, item)
        self.tabWidgetArticles.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidgetArticles.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonArticle.clicked.connect(self.addArticle)
        self.pushButtonFour.clicked.connect(self.addFournisseur)
        self.loadArticles()
        self.loadFournisseurs()
        self.loadArticlesComboBox()

    def addArticle(self):
        ArticleController.new_article(self)
        self.loadArticles()

    def addFournisseur(self):
        FournisseurController.new_fournisseur(self)
        self.loadFournisseurs()
        self.loadArticlesComboBox()

    def loadArticlesComboBox(self):
        self.comboBoxArticleFournisseur.clear()
        fournisseurs = FournisseurRepository.find_all()
        for four in fournisseurs:
            self.comboBoxArticleFournisseur.addItem(four[1], int(four[0]))

    def loadArticles(self):
        articles = ArticleRepository.find_all()
        self.tableWidgetArticles.setRowCount(len(articles))
        key = 0
        for article in articles:
            btnEditArticle = QtWidgets.QPushButton(self.tableWidgetArticles)
            btnEditArticle.setText('Editer')
            btnEditArticle.clicked.connect(lambda state, data=article[0]: self.editArticle(data))
            btnDelArticle = QtWidgets.QPushButton(self.tableWidgetArticles)
            btnDelArticle.setText('Supprimer')
            btnDelArticle.clicked.connect(lambda state, data=article[0]: self.delArticle(data))
            self.tableWidgetArticles.setCellWidget(key, 6, btnDelArticle)
            self.tableWidgetArticles.setCellWidget(key, 5, btnEditArticle)
            for i in range(0, 5):
                item = QTableWidgetItem(str(article[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetArticles.setItem(key, i, item)
            key += 1

    def loadFournisseurs(self):
        fours = FournisseurRepository.find_all()
        self.tableWidgetFours.setRowCount(len(fours))
        key = 0;
        for four in fours:
            for i in range(0, 3):
                item = QTableWidgetItem(str(four[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetFours.setItem(key, i, item)
            key += 1

    def editArticle(self, data):
        print(data)
        # Article edition here

    def delArticle(self, data):
        print(data)
        # Article deletion here

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Prix"))
        self.label_3.setText(_translate("MainWindow", "Quantité"))
        self.pushButtonArticle.setText(_translate("MainWindow", "Ajouter"))
        self.label_4.setText(_translate("MainWindow", "Fournisseur"))
        self.tableWidgetArticles.setSortingEnabled(True)
        item = self.tableWidgetArticles.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tableWidgetArticles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidgetArticles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prix (€)"))
        item = self.tableWidgetArticles.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantité"))
        item = self.tableWidgetArticles.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fournisseur"))
        item = self.tableWidgetArticles.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Editer"))
        item = self.tableWidgetArticles.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Supprimer"))
        self.tabWidgetArticles.setTabText(self.tabWidgetArticles.indexOf(self.tab), _translate("MainWindow", "Articles"))
        self.pushButtonFour.setText(_translate("MainWindow", "Ajouter"))
        self.label_6.setText(_translate("MainWindow", "Nom"))
        self.label_7.setText(_translate("MainWindow", "Ville"))
        item = self.tableWidgetFours.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tableWidgetFours.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidgetFours.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ville"))
        self.tabWidgetArticles.setTabText(self.tabWidgetArticles.indexOf(self.tab_2), _translate("MainWindow", "Fournisseurs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

