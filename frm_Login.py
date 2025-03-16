from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QWidget)
import icon_TelaLogin_rc

class Ui_frm_Login(object):
    def setupUi(self, frm_Login):
        if not frm_Login.objectName():
            frm_Login.setObjectName(u"frm_Login")
        frm_Login.resize(800, 658)
        frm_Login.setStyleSheet(u"QWidget {\n"
"    background-color: #2F4F4F;\n"
"}")
        self.centralwidget = QWidget(frm_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_usuario = QLabel(self.centralwidget)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(70, 250, 131, 31))
        font = QFont()
        font.setBold(True)
        self.lbl_usuario.setFont(font)
        self.lbl_usuario.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Usuario = QLineEdit(self.centralwidget)
        self.txt_Usuario.setObjectName(u"txt_Usuario")
        self.txt_Usuario.setGeometry(QRect(210, 240, 511, 51))
        font1 = QFont()
        self.txt_Usuario.setFont(font1)
        self.txt_Usuario.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"	color: #00000\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_senha = QLabel(self.centralwidget)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(90, 330, 111, 31))
        self.lbl_senha.setFont(font)
        self.lbl_senha.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_Senha = QLineEdit(self.centralwidget)
        self.txt_Senha.setObjectName(u"txt_Senha")
        self.txt_Senha.setGeometry(QRect(210, 320, 511, 51))
        self.txt_Senha.setFont(font1)
        self.txt_Senha.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"	color: #00000\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.txt_Senha.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 420, 81, 121))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background: url(:/icon_login/avsIconLogo.png);\n"
"	background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 550, 251, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 590, 201, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 60, 401, 81))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    font-size: 60px;\n"
"    font-weight: bold;\n"
"    color: #FFA500;\n"
"    padding: 10px;\n"
"    border-radius: 8px;\n"
"}")
        frm_Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_Login)

        QMetaObject.connectSlotsByName(frm_Login)
    # setupUi

    def retranslateUi(self, frm_Login):
        frm_Login.setWindowTitle(QCoreApplication.translate("frm_Login", u"MainWindow", None))
        self.lbl_usuario.setText(QCoreApplication.translate("frm_Login", u"Usu\u00e1rio:", None))
        self.lbl_senha.setText(QCoreApplication.translate("frm_Login", u"Senha:", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("frm_Login", u"AVS-SOFTWARES", None))
        self.label_4.setText(QCoreApplication.translate("frm_Login", u"SOFTWARE E TECNOLOGIA", None))
        self.label_2.setText(QCoreApplication.translate("frm_Login", u"BEM-VINDO!", None))
    # retranslateUi

