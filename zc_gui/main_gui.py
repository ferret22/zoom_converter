from PySide2.QtWidgets import *
from main_win_ui import Ui_zc_main
from converter import ZoomConverter
import sys
import os


class MainWin(QMainWindow):

    def __init__(self, width: int, height: int, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_zc_main()
        self.ui.setupUi(self)

        self.error = QErrorMessage(self)
        self.msg_info = QMessageBox(self)

        self.ui.button_convert.clicked.connect(self.start_convert)

    def show_msg_info(self, msg: str, title: str):
        self.msg_info.setWindowTitle(title)
        self.msg_info.setText(msg)
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.show()

    def ms_error(self, title: str, message: str, type_error: str):  # Создание окна ошибки
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def get_path(self):
        path = self.ui.path_line.text()
        return path

    def start_convert(self):
        main_path = self.get_path()

        if os.path.exists(main_path):
            paths = os.listdir(main_path)
            convert = ZoomConverter(main_path, paths)
            convert.search_dot_zoom()

            if convert.dot_zoom_files:
                self.show_msg_info('Записи были найдены!', 'Search Zoom Files')
            else:
                self.ms_error('Search Zoom Files', 'Записи не найдены!', 'Search Zoom Files')


def start_program():
    app = QApplication(sys.argv)
    screen_rect = app.primaryScreen().availableGeometry()
    window = MainWin(screen_rect.width(), screen_rect.height())
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_program()
