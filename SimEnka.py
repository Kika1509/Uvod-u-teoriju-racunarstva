# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

data = []
inputStrings = []
transitions = {}

pp = pprint.PrettyPrinter(indent=4)

#provjera #, idi po prijelazu
def getNextStates(state, letter):
    nextStates = transitions[state][letter]
    if nextStates[0] == "#":
        return []
    else:
        return nextStates

#sva stanja iz epsilon prijelaza
def getAllEpsilon(states):
    for state in states:
        rStates = transitions[state]["$"]
        if rStates[0] != "#":
            for r in rStates:
                if r not in states:
                    states.append(r)
    return states


#first line-strings
line = sys.stdin.readline()
line = line.strip()
for string in line.split("|"):
    inputStrings.append(string.split(","))

#second line-states
line = sys.stdin.readline()
line = line.strip()
states=line.split(",")
    
#third line-alphabet
line = sys.stdin.readline()
line = line.strip()
alphabet=line.split(",")
    
#fourth line-accStates
line = sys.stdin.readline()
line = line.strip()
accStates=line.split(",")
    
#fifth line-initState
line = sys.stdin.readline()
line = line.strip()
initState=line

#init transitions
for state in states:
    value = {"$":["#"]}
    for letter in alphabet:
        value[letter] = ["#"]
    transitions[state] = value

#rest of input-transitions
for line in sys.stdin.readlines():
    line = line.strip()
    trans = line.split("->")
    stateLetter = trans[0].split(",")
    fromState = stateLetter[0]
    letter = stateLetter[1]
    toStates = trans[1].split(",")
    transitions[fromState][letter] = toStates

#program body
startStates = list(set(getAllEpsilon([initState])))
startStates.sort()

#glavna petlja
resultStates = []
for string in inputStrings:
    stringStates = [startStates]
    lastStates = startStates[:]
    for letter in string:
        currentStates = []
        for state in lastStates:
            currentStates.extend(getNextStates(state, letter))
        currentStates = list(set(getAllEpsilon(currentStates)))
        currentStates.sort()
        stringStates.append(currentStates)
        lastStates = currentStates[:]
    resultStates.append(stringStates)


for strings in resultStates:
    print "|".join(",".join(letters) if letters else "#" for letters in strings)
