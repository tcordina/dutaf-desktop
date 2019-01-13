from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from src.Controllers import ArticleController, FournisseurController
from src.Repositories import ArticleRepository, FournisseurRepository
import sqlite3


class Ui_MainWindow(object):

    def setup_ui(self, MainWindow):
        self.create_tables()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidgetArticles = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetArticles.setGeometry(QtCore.QRect(0, 0, 750, 531))
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

        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 450, 71, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.doubleSpinBoxArticlePrix = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxArticlePrix.setGeometry(QtCore.QRect(140, 450, 171, 22))
        self.doubleSpinBoxArticlePrix.setObjectName("doubleSpinBoxArticlePrix")

        self.spinBoxArticleQuant = QtWidgets.QSpinBox(self.tab)
        self.spinBoxArticleQuant.setGeometry(QtCore.QRect(423, 409, 171, 22))
        self.spinBoxArticleQuant.setObjectName("spinBoxArticleQuant")

        self.pushButtonArticle = QtWidgets.QPushButton(self.tab)
        self.pushButtonArticle.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButtonArticle.setObjectName("pushButtonArticle")

        self.pushButtonArticleEdit = QtWidgets.QPushButton(self.tab)
        self.pushButtonArticleEdit.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButtonArticleEdit.setObjectName("pushButtonArticleEdit")
        self.pushButtonArticleEdit.hide()

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

        self.pushButtonFourEdit = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonFourEdit.setGeometry(QtCore.QRect(320, 480, 75, 23))
        self.pushButtonFourEdit.setObjectName("pushButtonFourEdit")
        self.pushButtonFourEdit.hide()

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
        self.tableWidgetFours.setColumnCount(5)
        self.tableWidgetFours.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFours.setHorizontalHeaderItem(4, item)
        self.tabWidgetArticles.addTab(self.tab_2, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        self.tabWidgetArticles.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonArticle.clicked.connect(self.add_article)
        self.pushButtonFour.clicked.connect(self.add_fournisseur)
        self.load_articles()
        self.load_fournisseurs()
        self.load_articles_combobox()

    def add_article(self):
        ArticleController.new_article(self)
        self.load_articles()

    def add_fournisseur(self):
        FournisseurController.new_fournisseur(self)
        self.load_fournisseurs()
        self.load_articles_combobox()

    def load_articles_combobox(self):
        self.comboBoxArticleFournisseur.clear()
        fournisseurs = FournisseurRepository.find_all()
        for four in fournisseurs:
            self.comboBoxArticleFournisseur.addItem(four[1], int(four[0]))

    def load_articles(self):
        articles = ArticleRepository.find_all()
        self.tableWidgetArticles.setRowCount(len(articles))
        key = 0
        for article in articles:
            btnEditArticle = QtWidgets.QPushButton(self.tableWidgetArticles)
            btnEditArticle.setText('Editer')
            btnEditArticle.clicked.connect(lambda state, data=article[0]: self.edit_article(data))
            btnDelArticle = QtWidgets.QPushButton(self.tableWidgetArticles)
            btnDelArticle.setText('Supprimer')
            btnDelArticle.clicked.connect(lambda state, data=article[0]: self.del_article(data))
            self.tableWidgetArticles.setCellWidget(key, 6, btnDelArticle)
            self.tableWidgetArticles.setCellWidget(key, 5, btnEditArticle)
            for i in range(0, 5):
                item = QTableWidgetItem(str(article[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetArticles.setItem(key, i, item)
            key += 1

    def load_fournisseurs(self):
        fours = FournisseurRepository.find_all()
        self.tableWidgetFours.setRowCount(len(fours))
        key = 0;
        for four in fours:
            btnEditFour = QtWidgets.QPushButton(self.tableWidgetArticles)
            btnEditFour.setText('Editer')
            btnEditFour.clicked.connect(lambda state, data=four[0]: self.edit_four(data))
            btnDelFour = QtWidgets.QPushButton(self.tableWidgetArticles)
            btnDelFour.setText('Supprimer')
            btnDelFour.clicked.connect(lambda state, data=four[0]: self.del_four(data))
            self.tableWidgetFours.setCellWidget(key, 4, btnDelFour)
            self.tableWidgetFours.setCellWidget(key, 3, btnEditFour)
            for i in range(0, 3):
                item = QTableWidgetItem(str(four[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidgetFours.setItem(key, i, item)
            key += 1

    def edit_article(self, data):
        print(data)
        article = ArticleRepository.find(data)
        print(article)
        self.lineEditArticleName.setText(article[1])
        self.doubleSpinBoxArticlePrix.setValue(float(article[2].replace(',', '.')))
        self.spinBoxArticleQuant.setValue(int(article[3]))
        if article[5]:
            self.comboBoxArticleFournisseur.setCurrentIndex(int(article[5]-1))
        else:
            self.comboBoxArticleFournisseur.setCurrentIndex(0)
        self.pushButtonArticleEdit.clicked.connect(lambda state, id=article[0]: self.update_article(id))
        self.pushButtonArticle.hide()
        self.pushButtonArticleEdit.show()

    def edit_four(self, data):
        print(data)
        four = FournisseurRepository.find(data)
        print(four)
        self.lineEditFourName.setText(four[1])
        self.lineEditFourVille.setText(four[2])
        self.pushButtonFourEdit.clicked.connect(lambda state, id=four[0]: self.update_four(id))
        self.pushButtonFour.hide()
        self.pushButtonFourEdit.show()

    def update_article(self, id):
        ArticleController.update_article(self, id)
        self.load_articles()
        self.pushButtonArticleEdit.hide()
        self.pushButtonArticleEdit.disconnect()
        self.pushButtonArticle.show()
        self.lineEditArticleName.setText('')
        self.doubleSpinBoxArticlePrix.setValue(0)
        self.spinBoxArticleQuant.setValue(0)
        self.comboBoxArticleFournisseur.setCurrentIndex(0)

    def update_four(self, id):
        FournisseurController.update_fournisseur(self, id)
        self.load_fournisseurs()
        self.pushButtonFourEdit.hide()
        self.pushButtonFourEdit.disconnect()
        self.pushButtonFour.show()
        self.lineEditFourName.setText('')
        self.lineEditFourVille.setText('')
        self.load_articles_combobox()

    def del_article(self, id):
        print(id)
        article = ArticleRepository.find(id)
        print(article)
        ArticleController.delete_article(id)
        self.load_articles()

    def del_four(self, id):
        print(id)
        four = FournisseurRepository.find(id)
        print(four)
        FournisseurController.delete_fournisseur(id)
        self.load_fournisseurs()
        self.load_articles()
        self.load_articles_combobox()

    @staticmethod
    def create_tables():
        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fournisseur(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name VARCHAR(100),
                city VARCHAR(100)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS article(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name VARCHAR(100),
                price FLOAT,
                quant INTEGER,
                fournisseur_id INTEGER,
                CONSTRAINT fk_founisseur
                    FOREIGN KEY (fournisseur_id)
                    REFERENCES fournisseur(id)
                    ON DELETE SET NULL
            );
        """)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dutaf"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Prix"))
        self.label_3.setText(_translate("MainWindow", "Quantité"))
        self.pushButtonArticle.setText(_translate("MainWindow", "Ajouter"))
        self.pushButtonArticleEdit.setText(_translate("MainWindow", "Editer"))
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
        self.pushButtonFourEdit.setText(_translate("MainWindow", "Editer"))
        self.label_6.setText(_translate("MainWindow", "Nom"))
        self.label_7.setText(_translate("MainWindow", "Ville"))
        item = self.tableWidgetFours.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "#"))
        item = self.tableWidgetFours.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidgetFours.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ville"))
        item = self.tableWidgetFours.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Editer"))
        item = self.tableWidgetFours.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Supprimer"))
        self.tabWidgetArticles.setTabText(self.tabWidgetArticles.indexOf(self.tab_2), _translate("MainWindow", "Fournisseurs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

