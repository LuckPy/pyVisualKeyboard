from PySide6 import QtWidgets, QtGui, QtCore

from keyboard import return_random_text


class Keyboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.add_layout()
        self.setup_ui()
        self.setFixedHeight(600)
        self.setup_connections()
        self.setStyleSheet("background-color: #2c2c2c")
        self.reload_text()

    def setup_ui(self):
        self.btns = {}

        def add_ligne(l1, l2, layout):
            for i, letter in enumerate(l1):
                if letter != r'\\':
                    self.btns[f"{letter} {l2[i]}"] = self.ButtonKey()
                    self.btns[f"{letter} {l2[i]}"].setText(f"{letter} {l2[i]}")
                    layout.addWidget(self.btns[f"{letter} {l2[i]}"])

        add_ligne("&é\"\'(-è_çà)=", "1234567890°+", self.first_ligne_layout)
        add_ligne("azertyuiop^$", "AZERTYUIOP¨£", self.second_ligne_layout)
        add_ligne("qsdfghjklmù*", "QSDFGHJKLM%µ", self.third_ligne_layout)
        add_ligne("<wxcvbn,;:!", ">WXCVBN?./§", self.fourth_ligne_layout)

        #  WIDGETS LEFT LAYOUT
        self.te_exemple_text = self.TextEdit("", readonly=True)
        self.vertical_left_layout.addWidget(self.te_exemple_text)
        self.te_write_text = self.TextEdit("")
        self.te_write_text.setPlaceholderText("Zone de saisie de texte")
        self.vertical_left_layout.addWidget(self.te_write_text)

        #  WIDGETS RIGHT LAYOUT
        self.btn_reload_text = QtWidgets.QPushButton()
        self.btn_reload_text.setStyleSheet("border: none")
        my_icon = QtGui.QPixmap("resources/reload.png")
        self.btn_reload_text.setIcon(QtGui.QIcon(my_icon))
        self.btn_reload_text.setIconSize(QtCore.QSize(60, 60))
        self.vertical_right_layout.addWidget(self.btn_reload_text)

    def add_layout(self):
        #  MAIN LAYOUT
        self.main_layout = QtWidgets.QGridLayout(self)

        #  LAYOUT LEFT
        self.vertical_left_layout = QtWidgets.QVBoxLayout()
        self.first_ligne_layout = QtWidgets.QHBoxLayout()
        self.second_ligne_layout = QtWidgets.QHBoxLayout()
        self.third_ligne_layout = QtWidgets.QHBoxLayout()
        self.fourth_ligne_layout = QtWidgets.QHBoxLayout()

        #  LAYOUT RIGHT
        self.vertical_right_layout = QtWidgets.QVBoxLayout()

        # ADD LAYOUT TO LAYOUT
        self.main_layout.addLayout(self.vertical_left_layout, 0, 0, 1, 1)
        self.main_layout.addLayout(self.vertical_right_layout, 0, 1, 1, 1)
        self.vertical_left_layout.addLayout(self.first_ligne_layout)
        self.vertical_left_layout.addLayout(self.second_ligne_layout)
        self.vertical_left_layout.addLayout(self.third_ligne_layout)
        self.vertical_left_layout.addLayout(self.fourth_ligne_layout)

    def setup_connections(self):
        self.te_write_text.textChanged.connect(self.selected_key_colored)
        self.btn_reload_text.clicked.connect(self.reload_text)

    def selected_key_colored(self):
        for i in self.btns.values():
            i.setStyleSheet("color: white; border : 2px solid black ; border-radius: 4px; background : #303030")
        text = self.te_write_text.toPlainText()
        for key, value in self.btns.items():
            separate_character = key.split(" ")
            if len(text) > 0 and text[-1] in separate_character:
                value.setStyleSheet("color: white; border : 2px solid black ; border-radius: 4px; background : red")
                break

    def reload_text(self):
        self.te_exemple_text.setText("\n".join(return_random_text(4)))

    class TextEdit(QtWidgets.QTextEdit):
        def __init__(self, text, readonly=False):
            super().__init__()
            self.setText(text)
            self.setReadOnly(readonly)
            self.zoomIn(2)
            self.setStyleSheet("color: white; font-weight: bold; border : 1px solid grey ; border-radius: 3px;")

    class ButtonKey(QtWidgets.QPushButton):
        def __init__(self):
            super().__init__()
            self.setFixedSize(60, 60)
            self.setStyleSheet("color: white; border : 2px solid black ; border-radius: 4px; background : #303030")


app = QtWidgets.QApplication([])
win = Keyboard()
win.show()

app.exec_()
