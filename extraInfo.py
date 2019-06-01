# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExtraInfo_Text.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1185, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabTrois = QtWidgets.QTabWidget(self.centralwidget)
        self.tabTrois.setGeometry(QtCore.QRect(0, 0, 1181, 751))
        self.tabTrois.setObjectName("tabTrois")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.text_Accueil = QtWidgets.QTextBrowser(self.tab)
        self.text_Accueil.setGeometry(QtCore.QRect(90, 10, 1001, 361))
        self.text_Accueil.setObjectName("text_Accueil")
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(90, 670, 991, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(90, 680, 231, 16))
        self.label_3.setObjectName("label_3")
        self.calendarWidget_accueil = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget_accueil.setGeometry(QtCore.QRect(640, 20, 448, 331))
        self.calendarWidget_accueil.setObjectName("calendarWidget_accueil")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 380, 1001, 291))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        
        
        self.labelImage = QtWidgets.QLabel(self.tab)
        self.labelImage.setObjectName("labelImage")
        
        self.imageLayout_analyse = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.imageLayout_analyse.setContentsMargins(0, 0, 0, 0)
        self.imageLayout_analyse.setObjectName("imageLayout_analyse")
        self.imageLayout_analyse.addWidget(self.labelImage)
        
        
        
        self.tabTrois.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.progressBar_analyse = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_analyse.setGeometry(QtCore.QRect(90, 120, 989, 27))
        self.progressBar_analyse.setMouseTracking(True)
        self.progressBar_analyse.setProperty("value", 0)
        self.progressBar_analyse.setObjectName("progressBar_analyse")
        self.line_analyse = QtWidgets.QFrame(self.tab_2)
        self.line_analyse.setGeometry(QtCore.QRect(90, 40, 991, 20))
        self.line_analyse.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_analyse.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_analyse.setObjectName("line_analyse")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(90, 70, 789, 41))
        self.textEdit.setObjectName("textEdit")
        self.line_2 = QtWidgets.QFrame(self.tab_2)
        self.line_2.setGeometry(QtCore.QRect(90, 670, 991, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea.setGeometry(QtCore.QRect(90, 150, 990, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 989, 479))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.LabelResult_analyse = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.LabelResult_analyse.setGeometry(QtCore.QRect(10, 10, 971, 461))
        self.LabelResult_analyse.setObjectName("LabelResult_analyse")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.goB_analyse = QtWidgets.QPushButton(self.tab_2)
        self.goB_analyse.setGeometry(QtCore.QRect(890, 70, 140, 41))
        self.goB_analyse.setObjectName("goB_analyse")
        self.monNom_analyse = QtWidgets.QLabel(self.tab_2)
        self.monNom_analyse.setGeometry(QtCore.QRect(90, 680, 231, 16))
        self.monNom_analyse.setObjectName("monNom_analyse")
        self.delB_analyse = QtWidgets.QPushButton(self.tab_2)
        
        #boutton suppresion si plein
        #self.delB_analyse.setEnabled(False)
        
        self.delB_analyse.setGeometry(QtCore.QRect(1040, 70, 40, 41))
        self.delB_analyse.setObjectName("delB_analyse")
        self.exportB_analyse = QtWidgets.QPushButton(self.tab_2)
        self.exportB_analyse.setGeometry(QtCore.QRect(628, 640, 451, 34))
        self.exportB_analyse.setObjectName("exportB_analyse")
        self.Import_analyse = QtWidgets.QPushButton(self.tab_2)
        self.Import_analyse.setGeometry(QtCore.QRect(100, 640, 451, 34))
        self.Import_analyse.setObjectName("Import_analyse")
        self.tabTrois.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(70, 40, 1031, 611))
        self.label.setObjectName("label")
        self.tabTrois.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabTrois.setCurrentIndex(1)
        self.delB_analyse.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExtraInfo"))
        self.text_Accueil.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">Bonjour,</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">&gt; Bienvenue dans cette application qui va vous </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">permettre d\'analyser les données d\'un </span><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#0000ff;\">site </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#0000ff;\">internet</span><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-style:italic; color:#0000ff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">&gt; Veuillez passer à l\'onglet (Analyse) afin de </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">saisir votre lien.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-style:italic; color:#0000ff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">&gt; Les informations peuvent être </span><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#0000ff;\">exportées</span><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\"> dans </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; color:#0000ff;\">un fichier (.csv).</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-style:italic; color:#0000ff;\"><br /></p></body></html>"))
        
        self.labelImage.setPixmap(QtGui.QPixmap(_translate("MainWindow", 'acc.png')))
            
        self.label_3.setText(_translate("MainWindow", "Créee par : Idriss EL MESBAHI "))
        self.tabTrois.setTabText(self.tabTrois.indexOf(self.tab), _translate("MainWindow", "Accueil"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.LabelResult_analyse.setText(_translate("MainWindow", "test"))
        self.goB_analyse.setText(_translate("MainWindow", "Go"))
        self.monNom_analyse.setText(_translate("MainWindow", "Créee par : Idriss EL MESBAHI "))
        self.delB_analyse.setText(_translate("MainWindow", "Del"))
        self.exportB_analyse.setText(_translate("MainWindow", "Exporter les résultats"))
        self.Import_analyse.setText(_translate("MainWindow", "Importer un fichier Html"))
        self.tabTrois.setTabText(self.tabTrois.indexOf(self.tab_2), _translate("MainWindow", "Analyse"))
        self.label.setText(_translate("MainWindow", "apropos emm"))
        self.tabTrois.setTabText(self.tabTrois.indexOf(self.tab_3), _translate("MainWindow", "A propos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.setGeometry(400,400,400,400)
    MainWindow.show()
    #MainWindow.destroy()
    sys.exit(app.exec_())
  #  os.close(Python 3.6)
    #sys.exit(0)
