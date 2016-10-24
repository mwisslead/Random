import sys
import math
import traceback
import operator

import numpy as np

from PyQt5 import QtWidgets as QtGui

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import antlr4

import matplotlib_example.design as design
import matplotlib_example.testmodal as testmodal
from matplotlib_example.exprLexer import exprLexer
from matplotlib_example.exprParser import exprParser
from matplotlib_example.exprVisitor import exprVisitor

matplotlib.use('Qt5Agg')

FUNCS = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'arcsin': np.arcsin,
    'arccos': np.arccos,
    'arctan': np.arctan,
    'arctan2': np.arctan2,
    'asin': np.arcsin,
    'acos': np.arccos,
    'atan': np.arctan,
    'atan2': np.arctan2,
    'degrees': np.degrees,
    'radians': np.radians,
    'sinh': np.sinh,
    'cosh': np.cosh,
    'tanh': np.tanh,
    'arcsinh': np.arcsinh,
    'arccosh': np.arccosh,
    'arctanh': np.arctanh,
    'asinh': np.arcsinh,
    'acosh': np.arccosh,
    'atanh': np.arctanh,
    'round': np.round_,
    'floor': np.floor,
    'ceil': np.ceil,
    'exp': np.exp,
    'expm1': np.expm1,
    'exp2': np.exp2,
    'log': np.log,
    'log10': np.log10,
    'log2': np.log2,
    'log1p': np.log1p,
    'sqrt': np.sqrt,
    'abs': np.absolute,
    'sign': np.sign,
    'cumsum': np.cumsum
    }

class ExprEvalVisitor(exprVisitor):
    def __init__(self):
        super(ExprEvalVisitor, self).__init__()

    def _visit_op(self, ctx, operation):
        func1 = self.visit(ctx.expr()[0])
        func2 = self.visit(ctx.expr()[1])
        return lambda x: operation(func1(x), func2(x))

    def visitSub(self, ctx):
        return self.visit(ctx.expr())

    def visitMuldiv(self, ctx):
        return self._visit_op(ctx, operator.mul if ctx.MUL else operator.truediv)

    def visitAddsub(self, ctx):
        return self._visit_op(ctx, operator.add if ctx.ADD else operator.sub)

    def visitExpo(self, ctx):
        return self._visit_op(ctx, operator.pow)

    def visitMod(self, ctx):
        return self._visit_op(ctx, operator.mod)

    def visitNegate(self, ctx):
        func = self.visit(ctx.expr())
        return lambda x: -func(x)

    def visitFunc(self, ctx):
        funcname = ctx.ID().getText()
        if funcname not in FUNCS:
            raise NameError('{} is not a valid function name'.format(repr(funcname)))
        args = [self.visit(expr) for expr in ctx.expr()]
        return lambda x: FUNCS[funcname](*[f(x) for f in args])

    def visitNum(self, ctx):
        constant = float(ctx.NUM().getText())
        return lambda x: constant

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name == 'x':
            return lambda x: x
        elif name == 'pi':
            return lambda x: math.pi
        else:
            raise ValueError('only variable allowed is \'x\' or \'pi\'')

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Matplotlib Graph Example')
        self.figure = Figure(figsize=(320, 240), dpi=72, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.plothl.addWidget(self.canvas)
        self.actionStart.triggered.connect(self.OpenModal)
        self.InputBox.setText('arctan2(x, sin(2*pi*x)/x)')
        self.XMin.setText('-5')
        self.XMax.setText('5')
        self.Points.setText('200')
        self.InputChanged()

    def InputChanged(self):
        try:
            function = process_expr(self.InputBox.text())
            mnx = float(self.XMin.text())
            mxx = float(self.XMax.text())
            if mnx == mxx:
                mnx -= 0.5
                mxx += 0.5
            x = np.linspace(mnx, mxx, int(self.Points.text()))
            y = function(x)
            self.axes.clear()
            self.axes.plot(x, y)
            self.axes.set_xlim((mnx, mxx))
            if min(y) == max(y):
                self.axes.set_ylim((min(y)-0.5, max(y)+0.5))
            else:
                self.axes.set_ylim((min(y), max(y)))
            self.canvas.draw()
        except:
            traceback.print_exc()


    def OpenModal(self):
        testDialog = QtGui.QDialog(self)
        testUi = testmodal.Ui_Dialog()
        testUi.setupUi(testDialog)
        testDialog.show()

def process_expr(data):
    input_stream = antlr4.InputStream(data)
    lexer = exprLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = exprParser(stream)
    tree = parser.expr()
    visitor = ExprEvalVisitor()
    return visitor.visit(tree)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app

if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
