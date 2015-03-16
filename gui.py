#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
from genexpr import genExpr
from switch_menus import *
from add_grid import add_grid

class Gui(QtGui.QMainWindow):

    def __init__(self):
        super(Gui, self).__init__()

        self.initUI()

    def initUI(self):
        # Loading config file

        try:
            file = open("config", 'r')
        except IOError:
            file = open("config", 'w+')
            file.write('0\n9\n')
            file.close()
            file = open("config", 'r')

        self.first = int(file.readline().strip("\n"))
        self.second = int(file.readline().strip("\n"))

        file.close()

        # Init Window properties

        self.mainWidget = QtGui.QWidget(self)

        self.setCentralWidget(self.mainWidget)

        self.expression, self.answer = genExpr(self.first, self.second)

        self.grid = QtGui.QGridLayout(self.mainWidget)
        self.grid.setSpacing(40)

        # self.setFixedSize(300, 200)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Math Problems')
        self.setWindowIcon(QtGui.QIcon('icon.svg'))

        self.show()

        self.center()

        self.statusBar().showMessage("")


        # Start Widgets

        self.problem_field = QtGui.QLabel(self.expression, self)
        self.problem_field.setAlignment(QtCore.Qt.AlignCenter)

        self.answer_field = QtGui.QLabel(self)
        self.answer_field.setAlignment(QtCore.Qt.AlignCenter)

        self.show_answer = QtGui.QPushButton("Don't know", self)
        self.show_answer.clicked.connect(self.dont_know)

        self.submit = QtGui.QPushButton('Submit', self)
        self.submit.clicked.connect(self.check)

        self.start_menu = QtGui.QPushButton('Menu', self)
        self.start_menu.clicked.connect(self.menu)

        self.user_answer_field = QtGui.QLineEdit(self)

        self.user_answer_field.returnPressed.connect(self.check)

        self.user_answer_field.setMaximumWidth(200)
        self.start_menu.setMaximumWidth(200)
        self.submit.setMaximumWidth(200)
        self.show_answer.setMaximumWidth(200)
        self.answer_field.setMaximumWidth(200)
        self.problem_field.setMaximumWidth(200)


        # Main menu Widgets

        self.start = QtGui.QPushButton('Start', self)
        self.start.clicked.connect(self.game)

        self.options = QtGui.QPushButton('Options', self)
        self.options.clicked.connect(self.settings)

        self.quit = QtGui.QPushButton('Quit', self)
        self.quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.quit.setMaximumWidth(200)
        self.options.setMaximumWidth(200)
        self.start.setMaximumWidth(200)


        self.freespace = QtGui.QLabel(self)
        self.freespace1 = QtGui.QLabel(self)

        # Settings Widgets

        self.label = QtGui.QLabel('From', self)
        self.label1 = QtGui.QLabel('To', self)

        self.apply = QtGui.QPushButton('Apply', self)
        self.apply.clicked.connect(self.apply_settings)

        self.options_menu = QtGui.QPushButton('Menu', self)
        self.options_menu.clicked.connect(self.opt_menu)

        self.from_field = QtGui.QLineEdit(self)
        self.from_field.setText(str(self.first))
        self.to_field = QtGui.QLineEdit(self)
        self.to_field.setText(str(self.second))

        self.apply.setMaximumWidth(200)
        self.from_field.setMaximumWidth(200)
        self.to_field.setMaximumWidth(200)
        self.options_menu.setMaximumWidth(200)
        self.label.setMaximumWidth(200)
        self.label1.setMaximumWidth(200)

        add_grid(self)

        hide_options(self)
        hide_start(self)

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def opt_menu(self):
        show_menu(self)
        hide_options(self)

    def check(self):
        self.user_a = self.user_answer_field.text()
        self.answer_field.clear()

        if self.user_a == str(self.answer):
            self.statusBar().showMessage("Right")
            self.expression, self.answer = genExpr(self.first, self.second)
            self.problem_field.clear()
            self.problem_field.setText(self.expression)

        elif self.user_a != str(self.answer):
            self.statusBar().showMessage("Wrong")

        self.user_answer_field.clear()

    def game(self):
        hide_menu(self)
        show_start(self)

    def menu(self):
        self.statusBar().showMessage("")

        show_menu(self)
        hide_start(self)

    def dont_know(self):
        self.answer_field.clear()
        self.answer_field.setText(str(self.answer))

    def settings(self):
        show_options(self)
        hide_menu(self)

    def apply_settings(self):
        self.first = int(self.from_field.text())
        self.second = int(self.to_field.text())

        file = open("config", 'w')
        file.write(str(self.first) + "\n" + str(self.second))
        file.close()

        self.expression, self.answer = genExpr(self.first, self.second)

        self.problem_field.clear()
        self.problem_field.setText(self.expression)

        hide_options(self)
        show_menu(self)

def main():

    app = QtGui.QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
