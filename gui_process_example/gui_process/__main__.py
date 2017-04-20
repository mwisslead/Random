import sys

from PyQt5 import QtWidgets as QtGui

import gui_process.design as design

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Image processing gui example')


    def selectInputDir(self):
        self.inputDir.setText(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))


    def selectOutputDir(self):
        self.outputDir.setText(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))


    def startProcess(self):
        print('pressed start')


    def pauseProcess(self):
        print('pressed pause')


    def stopProcess(self):
        print('pressed stop')


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
