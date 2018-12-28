import sys
import untitled
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QDialog
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = untitled.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())