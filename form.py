from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QFileDialog, QCheckBox, QScrollArea, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QFont, QDoubleValidator

import mainFile

app = QApplication([])
window = QMainWindow()
window.setWindowTitle("Intrusion Detection System")
window.setFixedSize(700, 750)
window.setStyleSheet('background-color: linear-gradient(90deg, rgba(25,25,27,1) 0%, rgba(81,81,88,1) 100%);')

icon = QIcon("logo_network.png")
window.setWindowIcon(icon)
pixmap = QPixmap("global-network.png")
label = QLabel(window)
label.setPixmap(pixmap)
label.setGeometry(100, 0, 600, 500)

label2 = QLabel("Created by: Abbas Ghasan Noury", window)
label2.setGeometry(140, 500, 600, 50)
label2.setStyleSheet('color: #0D3162; font-family: Georgia;')
label3 = QLabel("Supervised by: Prof. Dr. Iman Salih Alshamery ", window)
label3.setGeometry(70, 600, 600, 50)
label3.setStyleSheet('color: #0D3162; font-family:Georgia;')
font = QFont()
font.setPointSize(16)
font2 = QFont()
font2.setPointSize(12)
label2.setFont(font)
label3.setFont(font)
button = QPushButton("Start", window)
button.setGeometry(500, 670, 180, 50)
button.setStyleSheet('color: black; font-family: Georgia; background-color:darkgreen')
button.setFont(font)


#######################################################################################
def options_page():
    window2.show()
    window.hide()


button.clicked.connect(options_page)
window2 = QMainWindow()
window2.setWindowTitle("Intrusion Detection System")
window2.setFixedSize(550, 500)
window2.setStyleSheet('background-color: linear-gradient(90deg, rgba(25,25,27,1) 0%, rgba(81,81,88,1) 100%);')
window2.setWindowIcon(icon)

button2 = QPushButton("Evaluate the System", window2)
button2.setGeometry(100, 100, 350, 50)
button2.setStyleSheet('color: white; font-family: Trebuchet MS; background-color:#0a5ad6')
button2.setFont(font)

label4 = QLabel("* This option Allow you Evaluate the system accuracy\n    with your dataset to find best impurity "
                "measure ", window2)
label4.setGeometry(120, 170, 340, 50)
label4.setStyleSheet('color: red; font-family:Georgia;')

button3 = QPushButton("Test The System", window2)
button3.setGeometry(100, 300, 350, 50)
button3.setStyleSheet('color: white; font-family: Trebuchet MS; background-color:#0a5ad6')
button3.setFont(font)

label5 = QLabel("* This option Allow you Test real data & find Decisions", window2)
label5.setGeometry(120, 370, 340, 50)
label5.setStyleSheet('color: red; font-family:Georgia;')


######################################################################################
def evaluate():
    window3.show()


button2.clicked.connect(evaluate)

window3 = QMainWindow()
window3.setWindowTitle("Intrusion Detection System")
window3.setFixedSize(700, 700)
window3.setStyleSheet('background-color: linear-gradient(90deg, rgba(25,25,27,1) 0%, rgba(81,81,88,1) 100%);')
window3.setWindowIcon(icon)

label5 = QLabel("Path to the DATASET", window3)
label5.setGeometry(20, 50, 270, 50)
label5.setStyleSheet('color: #141496; font-family:Georgia;')
label5.setFont(font)


def open_file_dialog():
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(window, "Select File")
    pathText.setText(file_path)


pathText = QLineEdit(window3)
pathText.setGeometry(300, 50, 300, 40)
pathText.setStyleSheet('background-color:white;color:black')
pathText.setFont(font2)

uploadBTN = QPushButton("Upload", window3)
uploadBTN.setGeometry(600, 50, 50, 40)
uploadBTN.clicked.connect(open_file_dialog)

label5 = QLabel("Purity Measure", window3)
label5.setGeometry(20, 150, 225, 50)
label5.setStyleSheet('color: #141496; font-family:Georgia;')
label5.setFont(font)
criteriontypeText = QComboBox(window3)
criteriontypeText.setGeometry(300, 150, 150, 40)
criteriontypeText.setFont(font2)
criteriontypeText.addItem("entropy")
criteriontypeText.addItem("gini")

label6 = QLabel("Train split size", window3)
label6.setGeometry(20, 250, 270, 50)
label6.setStyleSheet('color: #141496; font-family:Georgia;')
label6.setFont(font)

trainText = QLineEdit(window3)
trainText.setGeometry(300, 250, 200, 40)
trainText.setStyleSheet('background-color:white;color:black')
trainText.setFont(font2)
trainText.setValidator(QDoubleValidator())

label7 = QLabel("Test split size", window3)
label7.setGeometry(20, 350, 270, 50)
label7.setStyleSheet('color: #141496; font-family:Georgia;')
label7.setFont(font)

testText = QLineEdit(window3)
testText.setGeometry(300, 350, 200, 40)
testText.setStyleSheet('background-color:white;color:black')
testText.setFont(font2)
testText.setValidator(QDoubleValidator())

printopt = QCheckBox("Do you want to print the tree ? ", window3)
printopt.setGeometry(20, 450, 500, 30)
printopt.setFont(font)
printopt.setStyleSheet('color: #141496; font-family:Georgia;')


def check_input():
    if pathText.text() == '' or criteriontypeText.currentText() == '' or float(trainText.text()) == 0 or float(
            trainText.text()) < 0 or float(trainText.text()) > 0.99 or float(testText.text()) == 0 or float(
        testText.text()) < 0 or float(testText.text()) > 0.99:
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Error")
        message_box.setText("Invalid Or Messing  Inputs!")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    else:
        acc, cv10, cv5, cv3 = mainFile.main_function(pathText.text(), criteriontypeText.currentText(),
                                                     float(trainText.text()), float(testText.text()),
                                                     printopt.checkState())
        label8 = QLabel('Accuracy:' + str(acc)[:4] + '%', window4)
        label8.setGeometry(150, 50, 480, 50)
        label8.setStyleSheet('color: red; font-family:Arial;')
        label8.setFont(font)

        label9 = QLabel('Cross Validation(10):' + str(cv10)[:4], window4)
        label9.setGeometry(100, 150, 480, 50)
        label9.setStyleSheet('color: red; font-family:Arial;')
        label9.setFont(font)

        label10 = QLabel('Cross Validation(5):' + str(cv5)[:4], window4)
        label10.setGeometry(100, 250, 480, 50)
        label10.setStyleSheet('color: red; font-family:Arial;')
        label10.setFont(font)

        label11 = QLabel('Cross Validation(3):' + str(cv3)[:4], window4)
        label11.setGeometry(100, 350, 480, 50)
        label11.setStyleSheet('color: red; font-family:Arial;')
        label11.setFont(font)
        window4.show()


runBTN = QPushButton("Run The System", window3)
runBTN.setGeometry(250, 500, 200, 40)
runBTN.setFont(font2)
runBTN.clicked.connect(check_input)
######################################################################################
window4 = QMainWindow()
window4.setWindowTitle("Intrusion Detection System")
window4.setFixedSize(500, 500)
window4.setStyleSheet('background-color: linear-gradient(90deg, rgba(25,25,27,1) 0%, rgba(81,81,88,1) 100%);')
window4.setWindowIcon(icon)


######################################################################################
def test():
    window6.show()


button3.clicked.connect(test)

window6 = QMainWindow()
window6.setWindowTitle("Intrusion Detection System")
window6.setFixedSize(700, 400)
window6.setStyleSheet('background-color: linear-gradient(90deg, rgba(25,25,27,1) 0%, rgba(81,81,88,1) 100%);')
window6.setWindowIcon(icon)

label12 = QLabel("Path to train DATASET", window6)
label12.setGeometry(20, 50, 300, 50)
label12.setStyleSheet('color: #141496; font-family:Georgia;')
label12.setFont(font)


def open_file_dialog2():
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(window, "Select File")
    pathText2.setText(file_path)


pathText2 = QLineEdit(window6)
pathText2.setGeometry(310, 50, 300, 40)
pathText2.setStyleSheet('background-color:white;color:black')
pathText2.setFont(font2)

uploadBTN2 = QPushButton("Upload", window6)
uploadBTN2.setGeometry(610, 50, 50, 40)
uploadBTN2.clicked.connect(open_file_dialog2)

label13 = QLabel("Purity Measure", window6)
label13.setGeometry(20, 150, 225, 50)
label13.setStyleSheet('color: #141496; font-family:Georgia;')
label13.setFont(font)
criteriontypeText2 = QComboBox(window6)
criteriontypeText2.setGeometry(300, 150, 150, 40)
criteriontypeText2.setFont(font2)
criteriontypeText2.addItem("entropy")
criteriontypeText2.addItem("gini")

label13 = QLabel("Path to test DATASET", window6)
label13.setGeometry(20, 250, 300, 50)
label13.setStyleSheet('color: #141496; font-family:Georgia;')
label13.setFont(font)


def open_file_dialog3():
    file_dialog = QFileDialog()
    file_path, _ = file_dialog.getOpenFileName(window, "Select File")
    path2Text.setText(file_path)


path2Text = QLineEdit(window6)
path2Text.setGeometry(310, 250, 300, 40)
path2Text.setStyleSheet('background-color:white;color:black')
path2Text.setFont(font2)

uploadBTN3 = QPushButton("Upload", window6)
uploadBTN3.setGeometry(610, 250, 50, 40)
uploadBTN3.clicked.connect(open_file_dialog3)


def check_input2():
    if pathText2.text() == '' or criteriontypeText2.currentText() == '' or path2Text.text() == '':
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Error")
        message_box.setText("Invalid Or Messing  Inputs!")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    else:
        predections = mainFile.indvisual_scan(pathText2.text(), criteriontypeText2.currentText(), path2Text.text())
        prediction = ""
        for c, i in zip(range(len(predections)), predections):
            prediction += str(c + 1) + "-" + i + "\n"

        label14 = QLabel('Decisions:\n' + prediction, window7)
        label14.setGeometry(20, 10, 500, 600)
        label14.setStyleSheet('color: red; font-family:Arial;')
        label14.setFont(font2)
        window7.show()


runBTN2 = QPushButton("Run The System", window6)
runBTN2.setGeometry(250, 350, 200, 40)
runBTN2.setFont(font2)
runBTN2.clicked.connect(check_input2)
#####################################################

window7 = QMainWindow()
window7.setWindowTitle("Intrusion Detection System")
window7.setFixedSize(700, 600)
window7.setStyleSheet('background-color: linear-gradient(90deg, rgba(25,25,27,1) 0%, rgba(81,81,88,1) 100%);')
window7.setWindowIcon(icon)

window.show()
app.exec_()

#####################################################
