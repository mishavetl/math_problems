#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    Created by Michael Vietluzhskih
    Copyright (c) 2015

    last edited: 15.03.15
'''

from __future__ import division
import os
from genexpr import genExpr
import random
import readline

def cls():
    os.system(['clear', 'cls'][os.name == 'nt'])

def main():
    print "\n*** Welcome to The Math Problems ***"
    print "\n\n"

    while True:
        expression, answer = genExpr()
        print "\n_____"

        while True:
            print expression

            user_a = raw_input("> ")

            if user_a == "dont know":
                print answer
                break

            elif user_a == "clear":
                cls()

            elif user_a == "exit":
                print "\n*** Goodbye Michael ***\n"
                exit(0)

            elif user_a == str(answer):
                print "Right"
                break

            elif user_a != str(answer):
                print "Wrong\n"

if __name__ == '__main__':
    main()
