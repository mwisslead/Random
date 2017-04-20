import sys
import time

from PyQt5 import QtWidgets as QtGui, QtCore

import gui_process.design as design


class ProcessThread(QtCore.QThread):
    update_signal = QtCore.pyqtSignal(str)
    done_signal = QtCore.pyqtSignal()

    def __init__(self, inputDir, outputDir):
        super(ProcessThread, self).__init__()
        self.inputDir = inputDir
        self.outputDir = outputDir
        self.paused = False


    def run(self):
        for i in range(10):
            while self.paused:
                time.sleep(0.1)
            self.update_signal.emit(str(i))
            time.sleep(0.2)
            if self.paused:
                self.update_signal.emit('Paused')
        self.done_signal.emit()


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Image processing gui example')
        self.process = None
        self.switchToolbarState(False)
        self.statusbar.showMessage('Ready')


    def selectInputDir(self):
        self.inputDir.setText(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))


    def selectOutputDir(self):
        self.outputDir.setText(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))


    def switchToolbarState(self, state):
        self.toolbarStart.setEnabled(not state)
        self.toolbarPause.setEnabled(state)
        self.toolbarStop.setEnabled(state)


    def startProcess(self):
        if self.process:
            self.pauseProcess()
            return
        self.switchToolbarState(True)
        self.process = ProcessThread(self.inputDir.text, self.outputDir.text)
        self.process.update_signal.connect(self.updateStatus)
        self.process.done_signal.connect(self.stopProcess)
        self.process.start()


    def pauseProcess(self):
        if self.process:
            self.process.paused = not self.process.paused
            self.toolbarStart.setEnabled(self.process.paused)
            self.toolbarPause.setEnabled(not self.process.paused)


    def stopProcess(self):
        if self.process and not self.process.isFinished():
            self.process.terminate()
        self.process = None
        self.switchToolbarState(False)
        self.statusbar.showMessage('Ready')


    def updateStatus(self, msg):
        self.statusbar.showMessage(msg)


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
