import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QHBoxLayout()
        self.textArea = QTextEdit("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pretium dui ut ultricies fermentum. Cras quis eleifend metus, a blandit ex. Integer id rutrum arcu. In laoreet cursus est. Phasellus ornare massa id lectus consequat, vel tincidunt enim aliquam. Nunc aliquet commodo hendrerit. Nullam posuere, justo id tincidunt aliquam, dolor ante bibendum nunc, vel ultricies urna turpis id nisi. Nullam bibendum eros ut nibh varius, a convallis erat accumsan. Etiam pretium vehicula arcu, mattis fringilla tortor efficitur nec. Morbi eget vulputate diam, in posuere dolor. Cras interdum facilisis luctus. Fusce volutpat sapien eget consequat tristique. In nec arcu velit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pretium dui ut ultricies fermentum. Cras quis eleifend metus, a blandit ex. Integer id rutrum arcu. In laoreet cursus est. Phasellus ornare massa id lectus consequat, vel tincidunt enim aliquam. Nunc aliquet commodo hendrerit. Nullam posuere, justo id tincidunt aliquam, dolor ante bibendum nunc, vel ultricies urna turpis id nisi. Nullam bibendum eros ut nibh varius, a convallis erat accumsan. Etiam pretium vehicula arcu, mattis fringilla tortor efficitur nec. Morbi eget vulputate diam, in posuere dolor. Cras interdum facilisis luctus. Fusce volutpat sapien eget consequat tristique. In nec arcu velit.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas pretium dui ut ultricies fermentum. Cras quis eleifend metus, a blandit ex. Integer id rutrum arcu. In laoreet cursus est. Phasellus ornare massa id lectus consequat, vel tincidunt enim aliquam. Nunc aliquet commodo hendrerit. Nullam posuere, justo id tincidunt aliquam, dolor ante bibendum nunc, vel ultricies urna turpis id nisi. Nullam bibendum eros ut nibh varius, a convallis erat accumsan. Etiam pretium vehicula arcu, mattis fringilla tortor efficitur nec. Morbi eget vulputate diam, in posuere dolor. Cras interdum facilisis luctus. Fusce volutpat sapien eget consequat tristique. In nec arcu velit.")

        self.layout.addWidget(self.textArea)
        self.textArea.setStyleSheet("QTextEdit {color:white;background-color:#212121;border-radius:16px;}")
        
        self.sans = QFont("Segoe UI",15)
        self.textArea.setFont(self.sans)
        
        self.btnLayout = QVBoxLayout()
        self.btnLayout.addWidget(QPushButton("Open"))
        self.btnLayout.addWidget(QPushButton("Setup"))
        self.btnLayout.addWidget(QPushButton("Find"))
        self.setStyleSheet("QPushButton {margin-bottom:8px;min-height:52px;max-width:160px;color:#4fc3f7;background-color:#424242;border:3px solid #4fc3f7;border-radius:16px;font-size:35px;font-weight:bold;}" + "QPushButton:hover {color:#212121;background-color:#4fc3f7;}" + "QPushButton:pressed {color:white;background-color:#212121;border-color:white;}")
        
        self.status = QTextEdit()
        self.status.insertPlainText("Successfully loaded" + "\nOpen a file...")
        self.status.setReadOnly(1)
        self.status.setStyleSheet("QTextEdit {color:#bdbdbd;background-color:#212121;border-radius:16px;font-size:14px;font-weight:bold;max-width:160px;max-height:100px;border-bottom:none;border-bottom-left-radius:0;border-bottom-right-radius:0;}")

        self.controlLayout = QVBoxLayout()
        self.controlLayout.addWidget(self.status)

        self.statusBtnLayout = QHBoxLayout()
        self.prevBtn = QPushButton("Previous")
        self.nextBtn = QPushButton("Next")
        self.cntrlBtnDesign = ("QPushButton {margin-bottom:0;min-height:26px;color:#757575;font-size:14px;background-color:#212121;border:3px solid #181818;border-top:3px solid gray;border-radius: 4px 10px 4px 4px;border-radius:0;border-bottom-left-radius:16px;border-bottom-right-radius:16px;}")
        self.prevBtn.setStyleSheet(self.cntrlBtnDesign + "QPushButton:hover {color:white;background-color:black;}" + "QPushButton:pressed {color:black;background-color:white;}" + "QPushButton {border-bottom-right-radius:0;border-right:1px solid gray;}")
        self.nextBtn.setStyleSheet(self.cntrlBtnDesign + "QPushButton:hover {color:white;background-color:black;}" + "QPushButton:pressed {color:black;background-color:white;}" + "QPushButton {color:#f5f5f5;border-bottom-left-radius:0;border-left:2px solid gray;}")
        self.statusBtnLayout.addWidget(self.prevBtn)
        self.statusBtnLayout.addWidget(self.nextBtn)
        self.controlLayout.setSpacing(0)
        self.controlLayout.addLayout(self.statusBtnLayout)
        self.btnLayout.addLayout(self.controlLayout)

        self.btnLayout.setAlignment(Qt.AlignTop)
        self.layout.addLayout(self.btnLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.layout)

        self.setLayout(self.mainLayout)
        self.setGeometry(100, 100, 695, 385)
        self.widgetMargin = 6
        self.btnLayout.setContentsMargins(self.widgetMargin,0,0,0)
        self.setContentsMargins(self.widgetMargin,self.widgetMargin,self.widgetMargin,self.widgetMargin)
        self.setWindowTitle("Wordfind")
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.png"))
    app.setStyleSheet("QWidget {background-color:#424242;}" + "QTextEdit {border: 3px solid #181818;}")
    app.setFont(QFont("Trebuchet MS"))
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())