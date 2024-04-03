# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from qt_material import apply_stylesheet

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.v = 0
        self.s = 1
        self.stopped = False

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionaha.triggered.connect(self.menu_bar)
        self.ui.pushButton.released.connect(self.stop_button)


        gauge = self.ui.widget

        gauge.value_min = 0
        gauge.value_max = 200
        gauge.update_value(100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(50)  # Update data every 0.05 second

    def update_data(self):
        self.v += self.s
        if self.v >= 200:
            self.s = -1
        elif self.v < 0:
            self.s = 1
        self.ui.widget.update_value(self.v)

    def menu_bar(self):
        print("it works my man")

    def stop_button(self):
        self.stopped = not self.stopped
        if self.stopped:
            self.ui.pushButton.setText("arranca pendejo")
            self.s = 0
            self.v = 0
        else:
            self.ui.pushButton.setText("pará pará")
            self.s = 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
