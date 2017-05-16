# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

transitions = {}
inString = []
resultString = []

pp = pprint.PrettyPrinter(indent=4)


#first line-states
line = sys.stdin.readline()
line = line.strip()
states=line.split(",")

#second line-input alphabet
line = sys.stdin.readline()
line = line.strip()
inputAlph=line.split(",")
    
#third line-line alphabet
line = sys.stdin.readline()
line = line.strip()
lineAlph=line.split(",")

#fourth line-empty place sign
line = sys.stdin.readline()
line = line.strip()
emptySign=line
    
#fifth line-input string
line = sys.stdin.readline()
line = line.strip()
inputString=line

#sixth line-accStates
line = sys.stdin.readline()
line = line.strip()
accStates=line.split(",")

#seventh line-initState
line = sys.stdin.readline()
line = line.strip()
initState=line

#eight line-TS inital position
line = sys.stdin.readline()
line = line.strip()
initPosition=line

#rest of input-transitions
for line in sys.stdin.readlines():
    line = line.strip()
    trans = line.split("->")
    stateLetter = trans[0].split(",")
    fromState = stateLetter[0]
    letter = stateLetter[1]
    newStateSignDirection = trans[1].split(",")
    toState = newStateSignDirection[0]
    newSign = newStateSignDirection[1]
    direction = newStateSignDirection[2]
    transitions[(fromState,letter)] = (toState, newSign, direction)

for i in inputString:
    inString.append(i)

i = int(initPosition)
state = initState
letter = inString[i]
flag = 2
while flag == 2:
    if (state, letter) in transitions.keys():
        initPrijelaz = transitions[(state, letter)]
        state = initPrijelaz[0]
        inString[i] = initPrijelaz[1]
        if initPrijelaz[2] == 'R'and i == 69:
            if state in accStates:
                flag = 1
            else:
                flag = 0
            break
        elif initPrijelaz[2] == 'R':
            i = (i+1)
        elif initPrijelaz[2] == 'L'and i == 0:
            if state in accStates:
                flag = 1
            else:
                flag = 0
            break
        elif initPrijelaz[2] == 'L':
            i = (i-1)
        letter = inString[i]
        if state in accStates and inString[i] in emptySign:
            flag = 1
            break
    else:
        if state in accStates:
            flag = 1
        else:
            flag = 0
        break

resultString.append(state)
resultString.append(str(i))
inString = ''.join(inString)
resultString.append(inString)
if flag == 1:
    resultString.append("1")
    print "|".join(resultString)
else:
    resultString.append("0")
    print "|".join(resultString)

