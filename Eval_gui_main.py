from math import *
import numpy
import re
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QTextCursor
from PyQt5.QtCore import QSettings, Qt
from functools import wraps
from PyQt5.QtCore import QTranslator, QLibraryInfo
from Eval_gui import Ui_MainWindow

ORGANIZATION_NAME = "isva_company"
APPLICATION_NAME = "Eval_gui"
f_degrees = False  # признак расчета тригонометрических функции в градусах


def decorator_direct_tg_function(func):
    """
    Декоратор для выполнения прямой тригонометрической функции
    @param func: название функции
    @return: результат
    """

    @wraps(func)
    def wrapper(x):
        if f_degrees:  # Если заданы градусы
            res = func(radians(x))  # то градусы преобразовываем в радианы и вызываем функцию
        else:
            res = func(x)  # вызываем функцию без преобразования
        return res

    return wrapper


def decorator_inverse_tg_function(func):
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


@decorator_direct_tg_function
def ctg(x):
    """
    Функция для расчета котангенса
    """
    return 1.0 / tan(x)


@decorator_inverse_tg_function
def arcctg(x):
    """
    Функция для расчета арктангенса
    """
    return pi / 2.0 - atan(x)


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


# прямая тригонометрическая функция
# @func_decorator_tgo
def arcth(x):
    """
    Функция для расчета гиперболического арккотангенса
    """
    return ln((x + 1) / (x - 1)) / 2


sin = decorator_direct_tg_function(sin)
cos = decorator_direct_tg_function(cos)
tg = decorator_direct_tg_function(tan)
# sh = func_decorator_tgp(sinh)
# ch = func_decorator_tgp(cosh)
# th = func_decorator_tgp(tanh)

arcsin = decorator_inverse_tg_function(asin)
arccos = decorator_inverse_tg_function(acos)
arctg = decorator_inverse_tg_function(atan)
atan2 = decorator_inverse_tg_function(atan2)
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
        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.window_section = "Window"  # Секция параметров окна
        self.values_section = "Values"  # Секция параметров переменных
        self.precision_spinbox.setValue(self.settings.value(self.values_section + "/Precision", 16, type=int))
        self.select_checkbox.setChecked(self.settings.value(self.values_section + "/Select", True, type=bool))
        self.radian_radio.setChecked(self.settings.value(self.values_section + "/Rad_Deg", True, type=bool))
        self.degree_radio.setChecked(not self.radian_radio.isChecked())
        if self.settings.contains(self.window_section + "/geometry"):
            self.restoreGeometry(self.settings.value(self.window_section + "/geometry"))  # Восстановление размера окна
        if self.settings.contains(self.window_section + "/windowState"):
            self.restoreState(
                self.settings.value(self.window_section + "/windowState"))  # Восстановление состояния окна
        self.calc_text.setFocus()

    def add_functions(self):
        for button in self.findChildren(QtWidgets.QPushButton):
            if button.objectName().startswith(
                    "function_button_"):  # если имя кнопки начинается с function_button_ (это кнопки функций),
                button.clicked.connect(self.add_function)  # то подключаем обработчик при нажатии (add_txt)

        for button in self.findChildren(QtWidgets.QPushButton):
            if button.objectName().startswith(
                    "const_button_"):  # если имя кнопки начинается с const_button (это кнопки констант),
                button.clicked.connect(self.add_constant)  # то подключаем обработчик при нажатии (add_txtc)

        self.exit_button.clicked.connect(self.close)
        self.clear_button.clicked.connect(self.Clear_Calc)
        self.save_button.clicked.connect(self.Save_ini)
        self.calculate_button.clicked.connect(self.Calc)

    def closeEvent(self, event):
        # Ваше действие при закрытии окна
        self.settings.setValue(self.window_section + "/geometry", self.saveGeometry())  # Сохранение размера окна
        self.settings.setValue(self.window_section + "/windowState", self.saveState())  # Сохранение состояния окна
        event.accept()  # Закрываем окно

    def Save_ini(self):
        # сохранение настроек
        self.settings.setValue(self.values_section + "/Precision", self.precision_spinbox.value())
        self.settings.setValue(self.values_section + "/Select", str(self.select_checkbox.isChecked()))
        self.settings.setValue(self.values_section + "/Rad_Deg", str(self.radian_radio.isChecked()))

    def Clear_Calc(self):
        # очистка текста выражения
        self.calc_text.clear()

    def add_function(self):  # обработчик при нажатии кнопки функции
        txt = self.sender().text()  # type: ignore # получаем текст кнопки
        txt_f = txt.split("(")[0] + (
            "()")  # из текста выделяем название функции, т.е. текст до открывающей скобки, к этому названию
        # добавляем скобки
        selected_text = self.calc_text.textCursor().selectedText()  # и полученный текст добавляем в позицию курсора
        # Если есть выделенный текст, заменяем его новым текстом
        if selected_text:
            self.calc_text.insertPlainText(txt_f)
            # Удаляем выделенный текст
            self.calc_text.textCursor().removeSelectedText()
        else:
            self.calc_text.insertPlainText(txt_f)  # и полученный текст добавляем в позицию курсора
        cursor = self.calc_text.textCursor()
        # Перемещаем курсор на одну позицию влево
        cursor.movePosition(QTextCursor.Left)
        # Устанавливаем обновленный курсор в QPlainTextEdit
        self.calc_text.setTextCursor(cursor)
        self.calc_text.setFocus()

    def add_constant(self):  # обработчик при нажатии кнопки констант
        txt = self.sender().text()  # type: ignore # получаем текст кнопки
        txt_f = txt.split(" ")[0]  # из текста выделяем название константы, т.е. текст до пробела,
        selected_text = self.calc_text.textCursor().selectedText()
        if selected_text:
            self.calc_text.insertPlainText(txt_f)
            # Удаляем выделенный текст
            self.calc_text.textCursor().removeSelectedText()
        else:
            self.calc_text.insertPlainText(txt_f)
        self.calc_text.setFocus()

    def Calc(self):
        # вычисление выражения
        expression = self.calc_text.toPlainText()
        # удаление перевода строки, пробелов.
        # Замена пробельных символов на пустой и "^" на "**" (возведение в степень)
        expression = re.sub(r'\s', '', expression).replace("^", "**")
        expression = re.sub(r'[|#~&]', '$', expression)
        # Замена дубликатов функций на недопустимое выражение '$'
        pstr = r'\b(' + "|".join(lst_nofun) + r')\b'
        # print(pstr)
        expression = re.sub(pstr, '$', expression)
        global f_degrees
        f_degrees = self.degree_radio.isChecked()  # Признак расчета в градусах
        # print(expression)
        try:
            result = eval(expression)
            lenient = self.precision_spinbox.value() - len(str(int(result)))
            rnd = 0 if lenient < 0 else lenient
            result = round(result, rnd)
            values = numpy.format_float_positional(result, trim='-')
            self.result_label_value.setText(values)
        except(Exception,):
            self.result_label_value.setText("Ошибка в выражении и/или аргументах")
        if self.select_checkbox.isChecked():
            self.calc_text.selectAll()
        self.calc_text.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_translator = QTranslator()
    qt_translator.load("qtbase_ru", QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(qt_translator)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())
