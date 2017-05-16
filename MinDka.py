# -*- coding: utf-8 -*-
import sys
import pprint
from sets import Set

transitions = {}
unreachableStates = []
reachableStates = []

pp = pprint.PrettyPrinter(indent=4)


#find reachable states
def getAllReachable(states):
    for state in states:
        for letter in alphabet:
            rStates = transitions[state][letter]
            for r in rStates:
                if r not in states:
                    states.append(r)
    return states

#first line-states
line = sys.stdin.readline()
line = line.strip()
states=line.split(",")
    
#second line-alphabet
line = sys.stdin.readline()
line = line.strip()
alphabet=line.split(",")
    
#third line-accStates
line = sys.stdin.readline()
line = line.strip()
accStates=line.split(",")
    
#fourth line-initState
line = sys.stdin.readline()
line = line.strip()
initState=line

#init transitions
for state in states:
    value = {}
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

#pp.pprint(transitions)


#find and remove unreachables
reachableStates.append(initState)
reachableStates = list(set(getAllReachable(reachableStates)))
reachableStates.sort()

#pp.pprint(reachableStates)
for state in states:
    if state not in reachableStates:
        del transitions[state]

#
# 3. algoritam iz knjige
#

# dvije liste parova stanja: markedPairs i remainingPairs (to be checked)
markedPairs = []
remainingPairs = []

# dictionary lista parova pridruzenih nekom paru:
# { (p1, p2): [ (p3, p4), (p5, p6) ]
#    ... }
assignedPairs = {}

# pomocne funkcije

def makePair(state1, state2):
    """
    return sorted tuple (pair) of states
    """
    if state1 < state2:
        return (state1, state2)
    else:
        return (state2, state1)

def nextPair(pair, letter):
    """
    return pair of states after transition with letter
    pair is a (p,q) tuple
    letter is in alphabet
    """
    return makePair(transitions[pair[0]][letter][0],transitions[pair[1]][letter][0])

def markPair(pair):
    """
        mark a pair,
        don't remove it from remaining pairs list here, because
        it messes up the for loop in 2. korak
        pair is a (p,q) tuple
        """
    markedPairs.append(pair)

def markAssignedPairs(pair):
    """
        recursively mark pairs in lists assigned to the pair
        pair is a (p,q) tuple
        """
    # check if key pair exists
    if pair in assignedPairs:
        # mark all pairs in the list
        for p in assignedPairs[pair]:
            markPair(p)
            # and all pairs assigned to the freshly marked pairs
            markAssignedPairs(p)

def addToPairList(pair1, pair2):
    """
        add pair2 to list assigned to pair1 in assignedPairs
        pair1, pair2 are (p,q) tuples
        """
    # if pair1 already exists in assignedPairs dictionary,
    # append pair2 to its list
    if pair1 in assignedPairs:
        assignedPairs[pair1].append(pair2)
    else:
        # create new list containing pair2 and assign to pair1
        assignedPairs[pair1] = [pair2]


#generate pairs
for state1 in reachableStates:
    for state2 in reachableStates:
        if state1 < state2:
            if (state1 in accStates and state2 not in accStates) or (state1 not in accStates and state2 in accStates):
                markedPairs.append(makePair(state1,state2))
            else:
                remainingPairs.append(makePair(state1,state2))

delta = []
sljedeci = []
#blabla
for pair in remainingPairs:
    varijabla = 0
    for letter in alphabet:
        if nextPair(pair,letter) in markedPairs:
            varijabla = 1
    if varijabla:
            markPair(pair)
            markAssignedPairs(pair)
    else:
        for letter in alphabet:
            sljedeci = nextPair(pair, letter)
            if sljedeci[0]!=sljedeci[1]:
                addToPairList(sljedeci,pair)

# remove marked pairs from remaining pairs list
remainingPairs = [x for x in remainingPairs if x not in markedPairs]
#pp.pprint(remainingPairs)

for (p, q) in remainingPairs:
    if q == initState:
        initState = p
    if q in transitions:
        del transitions[q]
    for state in transitions:
        for letter in alphabet:
            if transitions[state][letter][0] == q:
                value = transitions[state]
                value[letter] = [p]
                transitions[state] = value

#pp.pprint(transitions)

#output
#new states
newStates = []
newAccStates = []
for state in sorted(transitions.keys()):
    newStates.append(state)
print ",".join(newStates)

#alphabet
print ",".join(alphabet)

#new acceptable states
for state in accStates:
    if state in newStates:
        newAccStates.append(state)
print ",".join(newAccStates)

#inital state
print initState

for state in newStates:
    for letter in alphabet:
        print "{},{}->{}".format(state, letter, transitions[state][letter][0])