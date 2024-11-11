from math import *
import numpy
import re
from Eval_gui import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QSettings
from Translate_menu import Object_menu
from functools import wraps

ORGANIZATION_NAME = "isva_company"
APPLICATION_NAME = "Eval_gui"
f_degrees = False  # признак расчета тригонометрических функции в градусах


def func_decorator_tgp(func):
    """
    Декоратор для выполнения прямой тригонометрической функции
    @param func: название функции
    @return: результат
    """

    @wraps(func)
    def wrapper(*args):
        if f_degrees:  # Если заданы градусы
            res = func(radians(*args))  # то градусы преобразовываем в радианы и вызываем функцию
        else:
            res = func(*args)  # вызываем функцию без преобразования
        return res

    return wrapper


def func_decorator_tgo(func):
    """
    Декоратор для выполнения обратной тригонометрической функции
    @param func: название функции
    @return: результат
    """

    @wraps(func)
    def wrapper(*args):
        if f_degrees:  # Если заданы градусы
            res = degrees(func(*args))  # то вызываем функцию и радианы преобразовываем в градусы
        else:
            res = func(*args)  # вызываем функцию без преобразования
        return res

    return wrapper


@func_decorator_tgp
def ctg(x):
    """
    Функция для расчета котангенса
    """
    return 1.0 / tan(x)


@func_decorator_tgo
def arcctg(x):
    """
    Функция для расчета арктангенса
    """
    return pi / 2.0 - atan(x)


# @func_decorator_tgp
def cth(x):
    """
    Функция для расчета гиперболического котангенса
    """
    return 1 / tanh(x)


def ln(x):
    """
    Функция для расчета натурального логарифма
    """
    return log(x, e)


# @func_decorator_tgo
def arcth(x):
    """
    Функция для расчета гиперболического арккотангенса
    """
    return ln((x + 1) / (x - 1)) / 2


sin = func_decorator_tgp(sin)
cos = func_decorator_tgp(cos)
tg = func_decorator_tgp(tan)
# sh = func_decorator_tgp(sinh)
# ch = func_decorator_tgp(cosh)
# th = func_decorator_tgp(tanh)

arcsin = func_decorator_tgo(asin)
arccos = func_decorator_tgo(acos)
arctg = func_decorator_tgo(atan)
atan2 = func_decorator_tgo(atan2)
# arsh = func_decorator_tgo(asinh)
# arch = func_decorator_tgo(acosh)
# arth = func_decorator_tgo(atanh)

abs = fabs
lgb = log2
sh = sinh
ch = cosh
th = tanh
arsh = asinh
arch = acosh
arth = atanh

# lst_nofun = ('fabs', 'tan', 'cosh', 'sinh', 'tanh', 'acos', 'asin', 'atan', 'log2', 'asinh', 'acosh', 'atanh', '|', '&', '^')

lst_nofun = (
    'fabs', 'tan', 'cosh', 'sinh', 'tanh', 'acos', 'asin', 'atan', 'log2', 'asinh', 'acosh', 'atanh')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_functions()
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
        # сохранение настроек
        self.settings.setValue(self.values_section + "/Precision", self.spin_precision.value())
        self.settings.setValue(self.values_section + "/Select", str(self.checkBSel.isChecked()))
        self.settings.setValue(self.values_section + "/Rad_Deg", str(self.radioB_rad.isChecked()))

    def run_exit(self):
        # закрыие окна
        self.close()

    def Clear_Calc(self):
        # очистка текста выражения
        self.textCalc.clear()

    def add_txt(self):  # обработчик при нажатии кнопки функции
        txt = self.sender().text()  # получаем текст кнопки
        txtf = txt.split("(")[0] + (
            "()")  # из текста выделяем название функции, т.е. текст до открывающей скобки, к этому названию
        # добавляем скобки
        selected_text = self.textCalc.textCursor().selectedText()  # и полученный текст добавляем в позицию курсора
        # Если есть выделенный текст, заменяем его новым текстом
        if selected_text:
            self.textCalc.insertPlainText(txtf)
            # Удаляем выделенный текст
            self.textCalc.textCursor().removeSelectedText()
        else:
            self.textCalc.insertPlainText(txtf)  # и полученный текст добавляем в позицию курсораа
        cursor = self.textCalc.textCursor()
        # Перемещаем курсор на одну позицию влево
        cursor.movePosition(QTextCursor.Left)
        # Устанавливаем обновленный курсор в QPlainTextEdit
        self.textCalc.setTextCursor(cursor)
        self.textCalc.setFocus()

    def add_txtc(self):  # обработчик при нажатии кнопки констант
        txt = self.sender().text()  # получаем текст кнопки
        txtf = txt.split(" ")[0]  # из текста выделяем название константы, т.е. текст до пробела,
        selected_text = self.textCalc.textCursor().selectedText()
        if selected_text:
            self.textCalc.insertPlainText(txtf)
            # Удаляем выделенный текст
            self.textCalc.textCursor().removeSelectedText()
        else:
            self.textCalc.insertPlainText(txtf)
        self.textCalc.setFocus()

    def Calc(self):
        # вичисление выражения
        expression = self.textCalc.toPlainText()
        # удаление перевода строки, пробелов.
        # Замена пробельных символов на пустой и "^" на "**" (возведение в степень)
        expression = re.sub(r'\s', '', expression).replace("^", "**")
        expression = re.sub(r'[|#~&]', '$', expression)
        # Замена дубликатов функций на недопустимое выражение '$'
        pstr = r'\b(' + "|".join(lst_nofun) + r')\b'
        # print(pstr)
        expression = re.sub(pstr, '$', expression)
        global f_degrees
        f_degrees = self.radioB_Deg.isChecked()  # Признак расчета в градусах
        # print(expression)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
