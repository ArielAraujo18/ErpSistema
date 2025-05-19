from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import icon_TelaLogin

class Ui_frm_Cadastrar(object):
    def setupUi(self, frm_Cadastrar):
        if not frm_Cadastrar.objectName():
            frm_Cadastrar.setObjectName(u"frm_Cadastrar")
        frm_Cadastrar.setFixedSize(1133, 724)
        frm_Cadastrar.setStyleSheet(u"QWidget {\n"
"    background-color: #2F4F4F;\n"
"}")
        self.centralwidget = QWidget(frm_Cadastrar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_usuario = QLabel(self.centralwidget)
        self.lbl_usuario.setObjectName(u"lbl_usuario")
        self.lbl_usuario.setGeometry(QRect(580, 150, 111, 31))
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
        self.txt_email = QLineEdit(self.centralwidget)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(700, 140, 411, 51))
        font1 = QFont()
        self.txt_email.setFont(font1)
        self.txt_email.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"	color: #00000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_senha = QLabel(self.centralwidget)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setGeometry(QRect(20, 230, 111, 31))
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
        self.txt_Senha.setGeometry(QRect(140, 220, 421, 51))
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
        self.label_3.setGeometry(QRect(530, 510, 81, 121))
        self.label_3.setStyleSheet(u"QLabel{\n"
"	background: url(:/icon_login/avsIconLogo.png);\n"
"	background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 640, 251, 31))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 680, 201, 20))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-size: 16px;\n"
"    color: #FFFFFF;\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 10, 321, 81))
        self.label_2.setStyleSheet(u"QLabel{\n"
"    font-size: 60px;\n"
"    font-weight: bold;\n"
"    color: #FFA500;\n"
"    padding: 10px;\n"
"    border-radius: 8px;\n"
"}")
        self.btn_voltar = QPushButton(self.centralwidget)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setGeometry(QRect(110, 360, 441, 91))
        self.btn_voltar.setStyleSheet(u"QPushButton {\n"
"    background-color: #6c757d; \n"
"    color: white; \n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5a6268; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #495057; \n"
"}")
        self.btn_cadastrar = QPushButton(self.centralwidget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setGeometry(QRect(570, 360, 481, 91))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    background-color: #8FBC8F; \n"
"    color: #000000;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #00FF7F; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #004085;\n"
"}")
        self.lbl_usuario_2 = QLabel(self.centralwidget)
        self.lbl_usuario_2.setObjectName(u"lbl_usuario_2")
        self.lbl_usuario_2.setGeometry(QRect(20, 150, 111, 31))
        self.lbl_usuario_2.setFont(font)
        self.lbl_usuario_2.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.txt_nome = QLineEdit(self.centralwidget)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(140, 140, 421, 51))
        self.txt_nome.setFont(font1)
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #cccccc; \n"
"    border-radius: 5px; \n"
"    padding: 6px; \n"
"    font-size: 30px; \n"
"    background-color: #ffffff;\n"
"    transition: all 0.3s ease;\n"
"	color: #00000;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid #3f51b5; \n"
"    background-color: #f5f5f5; \n"
"}\n"
"")
        self.lbl_usuario_3 = QLabel(self.centralwidget)
        self.lbl_usuario_3.setObjectName(u"lbl_usuario_3")
        self.lbl_usuario_3.setGeometry(QRect(570, 230, 171, 31))
        self.lbl_usuario_3.setFont(font)
        self.lbl_usuario_3.setStyleSheet(u"QLabel {\n"
"    font-size: 32px;\n"
"    color: #FFFFFF;\n"
"    font-weight: bold;\n"
"    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.4);\n"
"}\n"
"")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(760, 230, 221, 41))
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #2c3e50;\n"
"    color: #ecf0f1;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-size: 24px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: center right;\n"
"    width: 30px;\n"
"    border-left: 1px solid #34495e;\n"
"    background-color: #34495e;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border-left: 6px solid transparent;\n"
"    border-right: 6px solid transparent;\n"
"    border-top: 8px solid #ecf0f1;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #34495e;\n"
"    color: #ecf0f1;\n"
"    selection-background-color: #1abc9c;\n"
"    selection-color: #ffffff;\n"
"    border: 1px solid #34495e;\n"
"    border-radius: 5px;\n"
"    outline: none;\n"
"    min-width: 100px;\n"
""
                        "}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #1abc9c;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #16a085;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #2c3e50;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #1abc9c;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #2c3e50;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::han"
                        "dle:horizontal {\n"
"    background: #1abc9c;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #16a085;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"")
        frm_Cadastrar.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_Cadastrar)

        QMetaObject.connectSlotsByName(frm_Cadastrar)
    # setupUi

    def retranslateUi(self, frm_Cadastrar):
        frm_Cadastrar.setWindowTitle(QCoreApplication.translate("frm_Cadastrar", u"CADASTRE-SE", None))
        self.lbl_usuario.setText(QCoreApplication.translate("frm_Cadastrar", u"E-mail:", None))
        self.lbl_senha.setText(QCoreApplication.translate("frm_Cadastrar", u"Senha:", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("frm_Cadastrar", u"AVS-SOFTWARES", None))
        self.label_4.setText(QCoreApplication.translate("frm_Cadastrar", u"SOFTWARE E TECNOLOGIA", None))
        self.label_2.setText(QCoreApplication.translate("frm_Cadastrar", u"Cadastrar", None))
        self.btn_voltar.setText(QCoreApplication.translate("frm_Cadastrar", u"VOLTAR", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("frm_Cadastrar", u"Cadastre-se", None))
        self.lbl_usuario_2.setText(QCoreApplication.translate("frm_Cadastrar", u"Nome:", None))
        self.lbl_usuario_3.setText(QCoreApplication.translate("frm_Cadastrar", u"Permiss\u00e3o:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("frm_Cadastrar", u"Nenhum", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("frm_Cadastrar", u"Administrador", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("frm_Cadastrar", u"Usu\u00e1rio", None))

    # retranslateUi

if __name__ == "__main__":
        app = QApplication([])
        frm_Cadastrar = QMainWindow()
        ui = Ui_frm_Cadastrar()
        ui.setupUi(frm_Cadastrar)
        frm_Cadastrar.show()
        app.exec()