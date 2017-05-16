# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

transitions = {}
inputStrings = []
stackString = []

pp = pprint.PrettyPrinter(indent=4)


#first line-strings
line = sys.stdin.readline()
line = line.strip()
for string in line.split("|"):
    inputStrings.append(string.split(","))

#second line-states
line = sys.stdin.readline()
line = line.strip()
states=line.split(",")
    
#third line-input alphabet
line = sys.stdin.readline()
line = line.strip()
inAlphabet=line.split(",")

#fourth line-stack alphabet
line = sys.stdin.readline()
line = line.strip()
stAlphabet=line.split(",")
    
#fifth line-accStates
line = sys.stdin.readline()
line = line.strip()
accStates=line.split(",")
    
#sixth line-initState
line = sys.stdin.readline()
line = line.strip()
initState=line

#seventh line-initStack
line = sys.stdin.readline()
line = line.strip()
initStack=line

#rest of input-transitions
for line in sys.stdin.readlines():
    line = line.strip()
    trans = line.split("->")
    stateLetterStack = trans[0].split(",")
    fromState = stateLetterStack[0]
    letter = stateLetterStack[1]
    stackSymbol = stateLetterStack[2]
    newStatesStackString = trans[1].split(",")
    toState = newStatesStackString[0]
    stackString = newStatesStackString[1]
    transitions[(fromState,letter,stackSymbol)] = (toState, stackString)

#pp.pprint(transitions)

def clean(stackContent):
    return stackContent.replace('$', '')


for string in inputStrings:
    resultString = []
    resultString.append(initState+"#"+initStack)
    cState = initState
    cStack = initStack
    doEpsilon = True
    while doEpsilon:
        doEpsilon = False
        if len(cStack) < 1:
            break
        if (cState, "$", cStack[0]) in transitions.keys():
            initPrijelaz = transitions[(cState, "$", cStack[0])]
            cState = initPrijelaz[0]
            cStack = clean(initPrijelaz[1]) + cStack[1:]
            if len(cStack) < 1:
                resultString.append(cState+"#$")
            else:
                resultString.append(cState+"#"+cStack)
            doEpsilon = True
    for i in range(len(string)):
        letter = string[i]
        #print letter + "%" + cState + "%" + cStack
        if len(cStack) < 1:
            resultString.append("fail")
            break
        if (cState, letter, cStack[0]) not in transitions.keys():
            #print "Nemam"
            if (cState, "$", cStack[0]) not in transitions.keys():
                resultString.append("fail")
                break
            else:
                if not (i == len(string)-1 and cState in accStates):
                    epsPrijelaz = transitions[(cState, "$", cStack[0])]
                    cState = epsPrijelaz[0]
                    cStack = clean(epsPrijelaz[1]) + cStack[1:]
                    if len(cStack) < 1:
                        resultString.append(cState+"#$")
                    else:
                        resultString.append(cState+"#"+cStack)
        else:
            #print cState, cStack, letter
            prijelaz = transitions[(cState, letter, cStack[0])]
            #print transitions
            #print prijelaz 
            cState = prijelaz[0]
            cStack = clean(prijelaz[1]) + cStack[1:]
            #print cState + "||" + cStack
            if len(cStack) < 1:
                resultString.append(cState+"#$")
            else:
                resultString.append(cState+"#"+cStack)
            doEpsilon = True
            while (doEpsilon and len(cStack) > 0 and not (i == len(string)-1 and cState in accStates)):
                #print "ja sam epsilon"
                doEpsilon = False
                if (cState, "$", cStack[0]) in transitions.keys():
                    initPrijelaz = transitions[(cState, "$", cStack[0])]
                    cState = initPrijelaz[0]
                    cStack = clean(initPrijelaz[1]) + cStack[1:]
                    if len(cStack) < 1:
                        resultString.append(cState+"#$")
                    else:
                        resultString.append(cState+"#"+cStack)
                    doEpsilon = True
    if cState in accStates and "fail" not in resultString:
        resultString.append("1")
    else:
        resultString.append("0")
    while resultString.count("fail") > 1:
        resultString.remove("fail")
    print "|".join(resultString)


