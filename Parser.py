# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

pp = pprint.PrettyPrinter(indent=4)

signs = []

#first line-string
line = sys.stdin.readline()
line = line.strip()
input=line

#first sub-S
def S():
    global input
    signs.append("S")
    if len(input) == 0:
        return 0
    elif input[0] == 'a':
        input = input[1:]
        A()
        B()
    elif input[0] == 'b':
        input = input[1:]
        B()
        A()
    else:
        print "".join(signs)
        print "NE"
        sys.exit()


#second sub-A
def A():
    global input
    signs.append("A")
    if len(input) == 0:
        print "".join(signs)
        print "NE"
        sys.exit()
    elif input[0] == 'b':
        input = input[1:]
        C()
    elif input[0] =='a':
        input = input[1:]
        return 1
    else:
        print "".join(signs)
        print "NE"
        sys.exit()


#third sub-B
def B():
    global input
    signs.append("B")
    if len(input) == 0:
        return 1
    elif input[0] == 'c':
        input = input[1:]
        if input[0] == 'c':
            input = input[1:]
            S()
            if input[0] == 'b':
                input = input[1:]
                if input[0] == 'c':
                    input = input[1:]
                else:
                        print "".join(signs)
                        print "NE"
                        sys.exit()
            else:
                print "".join(signs)
                print "NE"
                sys.exit()
        else:
            print "".join(signs)
            print "NE"
            sys.exit()


#fourth sub-C
def C():
    global input
    signs.append("C")
    A()
    A()

#main program
if S()==0 or len(input)>0:
    print "".join(signs)
    print "NE"
else:
    print "".join(signs)
    print "DA"

