from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTextEdit, QMainWindow


class MyTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_w = self.get_main_window()

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter) and (event.modifiers() & Qt.ShiftModifier):
            self.insertPlainText('\n')  # Вставляем разрыв строки
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.main_w.Calc()
        else:
            super().keyPressEvent(event)

    def get_main_window(self):
        parent = self.parent()
        while parent and not isinstance(parent, QMainWindow):
            parent = parent.parent()
        return parent
