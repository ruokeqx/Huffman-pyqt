import sys
import ui
from PyQt5.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)
mainwindow = QMainWindow()
ui = ui.Ui_MainWindow()
# ui.pushButton.clicked.connect(loadfile)
ui.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())
