# Калькулятор с формулами
from math import *
import numpy
from Eval_gui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QSettings
from Translate_menu import Object_menu

ORGANIZATION_NAME = "isva_company"
APPLICATION_NAME = "Eval_gui"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_functions()
        self.path = "Eval_gui.ini"
        self.menu_obj = Object_menu()
        self.textCalc.customContextMenuRequested.connect(self.menu_obj.show_menu_text)
        self.spin_precision.customContextMenuRequested.connect(self.menu_obj.show_menu_spinbox)
        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.window_section = "Window"  # Секция параметров окна
        self.values_section = "Values"  # Секция параметров переменных
        self.spin_precision.setValue(self.settings.value(self.values_section + "/Precision", 16, type=int))
        self.checkBSel.setChecked(self.settings.value(self.values_section + "/Select", True, type=bool))
        self.radioB_rad.setChecked(self.settings.value(self.values_section + "/Rad_Deg", True, type=bool))
        self.radioB_Deg.setChecked(not self.radioB_rad.isChecked())
        if self.settings.contains(self.window_section + "/geometry"):
            self.restoreGeometry(self.settings.value(self.window_section + "/geometry"))  # Восстановление размера окна
        if self.settings.contains(self.window_section + "/windowState"):
            self.restoreState(
                self.settings.value(self.window_section + "/windowState"))  # Восстановление состояния окна
        self.textCalc.setFocus()

    def add_functions(self):
        for button in self.findChildren(Qt.QPushButton):  # просматриваем все кнопки
            if button.objectName()[0:6] == "pushBf":  # если имя кнопки начинается с pushBf (это кнопки функций) ,
                button.clicked.connect(self.add_txt)  # то подключаем обработчик при нажатии (add_txt)

        for button in self.findChildren(Qt.QPushButton):  # просматриваем все кнопки
            if button.objectName()[
               0:10] == "pushB_cons":  # если имя кнопки начинается с pushB_cons (это кнопки констант) ,
                button.clicked.connect(self.add_txtc)  # то подключаем обработчик при нажатии (add_txtc)

        self.pushB_Exit.clicked.connect(self.run_exit)
        self.pushB_Clear.clicked.connect(self.Clear_Calc)
        self.pushB_Save.clicked.connect(self.Save_ini)
        self.pushB_Calc.clicked.connect(self.Calc)
        self.pushB_Exit.setShortcut("Alt+F4")
        self.pushB_Calc.setShortcut("Alt+E")
        self.pushB_Clear.setShortcut("Alt+C")
        self.pushB_Save.setShortcut("Alt+S")

    def closeEvent(self, event):
        # Ваше действие при закрытии окна
        self.settings.setValue(self.window_section + "/geometry", self.saveGeometry())  # Сохранение размера окна
        self.settings.setValue(self.window_section + "/windowState", self.saveState())  # Сохранение состояния окна
        event.accept()  # Закрываем окно

    def Save_ini(self):
        self.settings.setValue(self.values_section + "/Precision", self.spin_precision.value())
        self.settings.setValue(self.values_section + "/Select", str(self.checkBSel.isChecked()))
        self.settings.setValue(self.values_section + "/Rad_Deg", str(self.radioB_rad.isChecked()))

    def run_exit(self):
        self.close()

    def Clear_Calc(self):
        self.textCalc.clear()

    def add_txt(self):  # обработчик при нажатии кнопки функции
        txt = self.sender().text()  # получаем текст кнопки
        txtf = txt.split("(")[0] + (
            "()")  # из текста выделяем название функции, т.е. текст до открывающей скобки, к этому названию добавляем скобки
        selected_text = self.textCalc.textCursor().selectedText()  # и полученный текст добавлеям в позицию курсора
        # Если есть выделенный текст, заменяем его новым текстом
        if selected_text:
            self.textCalc.insertPlainText(txtf)
            # Удалаем выделенный текст
            self.textCalc.textCursor().removeSelectedText()
        else:
            self.textCalc.insertPlainText(txtf)  # и полученный текст добавлеям в позицию курсора
        cursor = self.textCalc.textCursor()
        # Перемещаем курсор на одну позицию влево
        cursor.movePosition(QTextCursor.Left)
        # Устанавливаем обновленный курсор в QPlainTextEdit
        self.textCalc.setTextCursor(cursor)
        self.textCalc.setFocus()

    def add_txtc(self):  # обработчик при нажатии кнопки констант
        txt = self.sender().text()  # получаем текст кнопки
        txtf = txt.split(" ")[0]  # из текста выделяем название константы, т.е. текст до пробела,
        # self.textCalc.setText(self.textCalc.toPlainText() + txtf)  # и полученный текст добавлеям в конец выражения
        selected_text = self.textCalc.textCursor().selectedText()
        if selected_text:
            self.textCalc.insertPlainText(txtf)
            # Удалаем выделенный текст
            self.textCalc.textCursor().removeSelectedText()
        else:
            # self.textCalc.setText(self.textCalc.toPlainText() + txtf)  # и полученный текст добавлеям в конец выражения
            self.textCalc.insertPlainText(txtf)
        self.textCalc.setFocus()

    def Calc(self):
        lst_tgp = ("cos", "sin", "tan", "coshа", "sinh")
        lst_tgo = ("acos", "asin", "atan", "acosh", "asinh", "atanh")
        lst_tgo2 = ("atan2", "{{{{{{{{")
        expression = self.textCalc.toPlainText()
        expression = expression.replace("\n", "")
        if self.radioB_Deg.isChecked():
            for fn in lst_tgo:
                expression = expression.replace(fn + "(",
                                                "tgo(" + fn + ",")  # заменяем типа asin( на типа tgo~(asin, т.к. м.б. типа sin
            for fn in lst_tgp:
                expression = expression.replace(fn + "(", "tgp(" + fn + ",")  # заменяем типа sin( на типа tgp~(sin,
            for fn in lst_tgo2:
                expression = expression.replace(fn + "(", "tgo2(" + fn + ",")
        try:
            result = eval(expression)
            lnlenint = self.spin_precision.value() - len(str(int(result)))
            rnd = 0 if lnlenint < 0 else lnlenint
            result = round(result, rnd)
            values = numpy.format_float_positional(result, trim='-')
            self.txtRez.setText(values)
        except:
            self.txtRez.setText("Ошибка в выражении и/или аргументах")
        if self.checkBSel.isChecked():
            self.textCalc.selectAll()
        self.textCalc.setFocus()


def tgp(fn, x):  # Для прямых тригонаметрических функций с одним аргументом
    return (fn(radians(x)))  # переводим градусы в радианы и вычисляем тригонаметрическую функцию fn в радинах


def tgo(fn, x):  # Для обратных тригонаметрических функций с одним аргументом
    return degrees(fn(x))  # вычисляем тригонаметрическую функцию fn в радинах и переводим радианы в градусы


def tgo2(fn, x, y):  # Для обратных тригонаметрических функций с двумя аргументами
    return degrees(fn(x, y))  # вычисляем тригонаметрическую функцию fn в радинах и переводим радианы в градусы


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
