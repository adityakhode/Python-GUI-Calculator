from PyQt5 import QtCore, QtWidgets
from playsound import playsound

class Ui_Calculator(object):
    def __init__(self) -> None:
        self.stack = []
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(269, 502)
        Calculator.setStyleSheet("QWidget{\n"
                                 "background-color: rgb(0, 0, 0);\n"
                                 "border-radius: 20px;\n"
                                 "}\n"
                                 "")
        self.display = QtWidgets.QLabel(Calculator)
        self.display.setGeometry(QtCore.QRect(0, 0, 271, 171))
        self.display.setStyleSheet("QLabel{\n"
                                   "background-color: rgb(46, 52, 54);\n"
                                   "border-radius: 20px;\n"
                                   "}")
        self.display.setObjectName("display")
        self.AC = QtWidgets.QPushButton(Calculator)
        self.AC.setGeometry(QtCore.QRect(10, 200, 111, 51))
        self.AC.setStyleSheet("QPushButton {\n"
                              "    background-color: rgb(57, 67, 78);\n"
                              "    border-radius: 24px;                   \n"
                              "    color: rgb(0, 230, 255);   }\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                              "}")
        self.AC.setObjectName("AC")
        self.but7 = QtWidgets.QPushButton(Calculator)
        self.but7.setGeometry(QtCore.QRect(10, 260, 51, 51))
        self.but7.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255);   }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but7.setObjectName("but7")
        self.but0 = QtWidgets.QPushButton(Calculator)
        self.but0.setGeometry(QtCore.QRect(10, 440, 111, 51))
        self.but0.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "   color: rgb(0, 230, 255);    }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but0.setObjectName("but0")
        self.but5 = QtWidgets.QPushButton(Calculator)
        self.but5.setGeometry(QtCore.QRect(70, 320, 51, 51))
        self.but5.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255);    }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but5.setObjectName("but5")
        self.but6 = QtWidgets.QPushButton(Calculator)
        self.but6.setGeometry(QtCore.QRect(130, 320, 51, 51))
        self.but6.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255);    }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but6.setObjectName("but6")
        self.but1 = QtWidgets.QPushButton(Calculator)
        self.but1.setGeometry(QtCore.QRect(10, 380, 51, 51))
        self.but1.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255);  }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but1.setObjectName("but1")
        self.but4 = QtWidgets.QPushButton(Calculator)
        self.but4.setGeometry(QtCore.QRect(10, 320, 51, 51))
        self.but4.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "   color: rgb(0, 230, 255);    }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but4.setObjectName("but4")
        self.but2 = QtWidgets.QPushButton(Calculator)
        self.but2.setGeometry(QtCore.QRect(70, 380, 51, 51))
        self.but2.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "   color: rgb(0, 230, 255);     }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but2.setObjectName("but2")
        self.but8 = QtWidgets.QPushButton(Calculator)
        self.but8.setGeometry(QtCore.QRect(70, 260, 51, 51))
        self.but8.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255);  }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but8.setObjectName("but8")
        self.but3 = QtWidgets.QPushButton(Calculator)
        self.but3.setGeometry(QtCore.QRect(130, 380, 51, 51))
        self.but3.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255);    }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but3.setObjectName("but3")
        self.but9 = QtWidgets.QPushButton(Calculator)
        self.but9.setGeometry(QtCore.QRect(130, 260, 51, 51))
        self.but9.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);\n"
                                "    border-radius: 24px;                   \n"
                                "    color: rgb(0, 230, 255); }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.but9.setObjectName("but9")
        self.butdot = QtWidgets.QPushButton(Calculator)
        self.butdot.setGeometry(QtCore.QRect(130, 440, 51, 51))
        self.butdot.setStyleSheet("QPushButton {\n"
                                  "    background-color: rgb(57, 67, 78);\n"
                                  "    border-radius: 24px;                   \n"
                                  "    color: rgb(0, 230, 255);   }\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                  "}")
        self.butdot.setObjectName("butdot")
        self.percent = QtWidgets.QPushButton(Calculator)
        self.percent.setGeometry(QtCore.QRect(130, 200, 51, 51))
        self.percent.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(57, 67, 78);\n"
                                   "    border-radius: 24px;                   \n"
                                   "    color: rgb(0, 230, 255);   }\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                   "}")
        self.percent.setObjectName("percent")
        self.divide = QtWidgets.QPushButton(Calculator)
        self.divide.setGeometry(QtCore.QRect(200, 200, 61, 51))
        self.divide.setStyleSheet("QPushButton {\n"
                                  "    background-color: rgb(57, 67, 78);             \n"
                                  "    color: rgb(0, 230, 255);   }\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    background: rgb(46, 52, 54);  \n"
                                  "}")
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(Calculator)
        self.multiply.setGeometry(QtCore.QRect(200, 260, 61, 51))
        self.multiply.setStyleSheet("QPushButton {\n"
                                    "    background-color: rgb(57, 67, 78);            \n"
                                    "    color: rgb(0, 230, 255);   }\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                    "}")
        self.multiply.setObjectName("multiply")
        self.minus = QtWidgets.QPushButton(Calculator)
        self.minus.setGeometry(QtCore.QRect(200, 320, 61, 51))
        self.minus.setStyleSheet("QPushButton {\n"
                                 "    background-color: rgb(57, 67, 78);                 \n"
                                 "    color: rgb(0, 230, 255);   }\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                 "}")
        self.minus.setObjectName("minus")
        self.plus = QtWidgets.QPushButton(Calculator)
        self.plus.setGeometry(QtCore.QRect(200, 380, 61, 51))
        self.plus.setStyleSheet("QPushButton {\n"
                                "    background-color: rgb(57, 67, 78);           \n"
                                "    color: rgb(0, 230, 255);   }\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                "}")
        self.plus.setObjectName("plus")
        self.equals = QtWidgets.QPushButton(Calculator)
        self.equals.setGeometry(QtCore.QRect(200, 440, 61, 51))
        self.equals.setStyleSheet("QPushButton {\n"
                                  "    background-color: rgb(57, 67, 78);                \n"
                                  "    color: rgb(0, 230, 255);   }\n"
                                  "\n"
                                  "QPushButton:hover {\n"
                                  "    background: rgb(46, 52, 54);           /* Hover background color */\n"
                                  "}")
        self.equals.setObjectName("equals")
        self.label = QtWidgets.QLabel(Calculator)
        self.label.setGeometry(QtCore.QRect(0, 40, 271, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.output = QtWidgets.QLabel(Calculator)
        self.output.setGeometry(QtCore.QRect(150, 116, 111, 41))
        self.output.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.output.setObjectName("outpt")
        self.line = QtWidgets.QFrame(Calculator)
        self.line.setGeometry(QtCore.QRect(0, 180, 271, 2))
        self.line.setStyleSheet("background-color:rgb(0, 230, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        self._translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(self._translate("Calculator", "Form"))
        self.display.setText(self._translate("Calculator", "<html><head/><body><p><br/></p></body></html>"))
        self.AC.setText(self._translate("Calculator", "AC"))
        self.but7.setText(self._translate("Calculator", "7"))
        self.but0.setText(self._translate("Calculator", "0"))
        self.but5.setText(self._translate("Calculator", "5"))
        self.but6.setText(self._translate("Calculator", "6"))
        self.but1.setText(self._translate("Calculator", "1"))
        self.but4.setText(self._translate("Calculator", "4"))
        self.but2.setText(self._translate("Calculator", "2"))
        self.but8.setText(self._translate("Calculator", "8"))
        self.but3.setText(self._translate("Calculator", "3"))
        self.but9.setText(self._translate("Calculator", "9"))
        self.butdot.setText(self._translate("Calculator", "."))
        self.percent.setText(self._translate("Calculator", "<--"))
        self.divide.setText(self._translate("Calculator", "/"))
        self.multiply.setText(self._translate("Calculator", "X"))
        self.minus.setText(self._translate("Calculator", "-"))
        self.plus.setText(self._translate("Calculator", "+"))
        self.equals.setText(self._translate("Calculator", "="))
        

    def buttoninit(self):
        self.AC.clicked.connect(lambda: self.action("AC"))
        self.percent.clicked.connect(lambda: self.action("%"))
        self.divide.clicked.connect(lambda: self.action("/"))
        self.but9.clicked.connect(lambda: self.action("9"))
        self.but8.clicked.connect(lambda: self.action("8"))
        self.but7.clicked.connect(lambda: self.action("7"))
        self.but6.clicked.connect(lambda: self.action("6"))
        self.but5.clicked.connect(lambda: self.action("5"))
        self.but4.clicked.connect(lambda: self.action("4"))
        self.but3.clicked.connect(lambda: self.action("3"))
        self.but2.clicked.connect(lambda: self.action("2"))
        self.but1.clicked.connect(lambda: self.action("1"))
        self.but0.clicked.connect(lambda: self.action("0"))
        self.multiply.clicked.connect(lambda: self.action("*"))
        self.minus.clicked.connect(lambda: self.action("-"))
        self.plus.clicked.connect(lambda: self.action("+"))
        self.equals.clicked.connect(lambda: self.action("="))
        self.butdot.clicked.connect(lambda: self.action("."))

    def action(self,button_name):
        name = "assets/click.wav"
        playsound(name)
        if button_name == "AC":
            self.stack = []
            self.operation = []
            self.display = []
            result = self.calculate(button_name)
            self.output.setText(self._translate("Calculator", "<html><head/><body><p align=\"right\"><span style=\" font-size:30pt; font-weight:600; color:#00e6ff;\"></span></p></body></html>"))

        else:
            result = self.calculate(button_name)
            if result!=None:
                print(result)

            if button_name == '=':
                self.output.setText(self._translate("Calculator", f"<html><head/><body><p align=\"right\"><span style=\" font-size:30pt; font-weight:600; color:#00e6ff;\">{result}</span></p></body></html>"))


    def calculate(self,input):
        if input != "=":
            if input != "AC":
                self.stack.append(input)
                if input == "%":
                    self.stack.pop()
                    self.stack.pop()
                display=''
                for i in range (0,len(self.stack)):
                    display = display+self.stack[i]
                self.label.setText(self._translate("Calculator", f"<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; color:#00e6ff;\">{display}</span></p></body></html>"))
            else:
                self.label.setText(self._translate("Calculator", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; color:#00e6ff;\"></span></p></body></html>"))
        else:
            self.operation = (self.combine_numbers(self.stack))
            while len(self.operation) != 1:
                if '/' in self.operation :
                    self.manipulate('/')
                if '*' in self.operation:
                    self.manipulate('*')
                if '+' in self.operation:
                    self.manipulate('+')
                if '-' in self.operation:
                    self.manipulate('-')
                if len(self.operation) ==1:
                    return self.operation[0]
            return self.operation[0]

    def combine_numbers(self,stack):
        combined_stack = []
        current_number = ""

        for item in stack:
            if item in ['+', '-', '*', '/']:
                if "." in stack:        
                    combined_stack.append(float(current_number))
                else:
                    combined_stack.append(int(current_number))

                current_number = ""
                combined_stack.append(item)
            else:
                current_number += str(item)

        if "." in stack:        
            combined_stack.append(float(current_number))
        else:
            combined_stack.append(int(current_number))
        current_number = ""

        return combined_stack

    def manipulate(self,operator):
        temp = self.operation.index(operator)
        if operator == "+":
            self.operation[temp-1] = self.operation[temp-1]+self.operation[temp+1] 
            self.operation.pop(temp)
            self.operation.pop(temp)
        elif operator == "-":
            self.operation[temp-1] = self.operation[temp-1]-self.operation[temp+1]
            self.operation.pop(temp)
            self.operation.pop(temp)
        elif operator == "*":
            self.operation[temp-1] = self.operation[temp-1]*self.operation[temp+1]
            self.operation.pop(temp)
            self.operation.pop(temp)
        elif operator == "/":
            if self.operation[temp+1] == 0:
                raise ZeroDivisionError("ERROR")
            self.operation[temp-1] = self.operation[temp-1]/self.operation[temp+1]
            self.operation.pop(temp)
            self.operation.pop(temp)
        elif operator == '%':
            self.operation[temp-1] = self.operation[temp-1]/100
            self.operation.pop(temp)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    ui.buttoninit()
    sys.exit(app.exec_())
