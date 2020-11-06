#This is the work of Diego Castro, djc16j
#Class : This assignment was initially for Theory of Computation Programming Assignment 1, but I have heavily modified it.
'''
This program is made to detect if a person suffers from Huntington's Disease, it uses a DFA (definite-Finite-Automata,
to detect chains and repeated CAG substring in the provided text file. If there are over 40 repeated CAG substrings,
the person will experience syntoms from Huntingtons disease and the program will output POSITIVE.
'''


import math
import random
from pathlib import Path
import os
##TESTING PURPOSES
def clearFile(Filename):
    open(Filename, "w").close()
    print(Filename+" cleared!\n")
def deleteFile(Filename):
    os.remove(Filename)
    #had to add this bc it was making my computer super slow and would not even let me add/delete the text from the testcases
def AddToFile(Filename,numElements):
    #this can be use to add randomly generated characters to the file
    f = open(Filename, "a")
    choices = ['A', 'C', 'G', 'T']
    for i in range(0, numElements):
        rand = random.randint(0, 3)
        f.write(choices[rand])
    f.close()

def ReadGenome(Filename):
    if Path(Filename).is_file():
        f = open(Filename, "r")
        CAG = f.read()
        counter = 0
        state = 0
        max = 0
        current = 0
        for i in range(0, len(CAG)):
            if (i == 0):
                print("Processing....0% Done!")
            if (i == math.floor(len(CAG) * .10)):
                print("Processing....10% Done!")
            if (i == math.floor(len(CAG) * .20)):
                print("Processing....20% Done!")
            if (i == math.floor(len(CAG) * .30)):
                print("Processing....30% Done!")
            if (i == math.floor(len(CAG) * .40)):
                print("Processing....40% Done!")
            if (i == math.floor(len(CAG) * .50)):
                print("Processing....50% Done!")
            if (i == math.floor(len(CAG) * .60)):
                print("Processing....60% Done!")
            if (i == math.floor(len(CAG) * .70)):
                print("Processing....70% Done!")
            if (i == math.floor(len(CAG) * .80)):
                print("Processing....80% Done!")
            if (i == math.floor(len(CAG) * .90)):
                print("Processing....90% Done!")
            if (state == 0 and CAG[i] == 'C'):
                state = 1
                continue
            elif (state == 1 and CAG[i] == 'A'):
                state = 2
                continue
            elif (state == 2 and CAG[i] == 'G'):
                state = 3
                continue
            elif (state == 3 and CAG[i] == 'C'):
                state = 4
                continue
            elif (state == 4 and CAG[i] == 'A'):
                state = 5
                continue
            elif (state == 5 and CAG[i] == 'G'):
                counter = counter + 1
                current = current + 1
                if max < current:
                    max = current
                state = 6
                continue
            elif (state == 6 and CAG[i] == 'C'):
                state = 4
                continue
            else:
                state = 0
                current = 0
                continue
        # print(CAG)
        print("Longest Chain is = ", max)
        print("Num of repeated CAG's is: ", counter)
        if (counter >= 40):
            print("POSITIVE")
        else:
            print("NEGATIVE")
    else:
        print("File "+Filename+" not found.\n")


mode = input("Choose the mode : T (Test), R,(Read)    ")
while mode!='T' and mode != 'R':
    print("Try again.")
    mode = input("Choose the mode : T (Test), R,(Read)    ")
if (mode == 'R'):
    filename = input("Enter the file you want to read: ")
    ReadGenome(filename)
if (mode == 'T'):
    test_f=input("What do you want to name the test file?     ")
    num_elements = int(input("How many characters do you want to add to the test file?      "))
    f = open(test_f, "w+")
    AddToFile(test_f,num_elements)
    ReadGenome(test_f)
    clear = input("Do you want to delete the test file? Y/N     ")
    while clear != 'Y' and clear != 'N':
        print("Try again.")
        clear = input("Do you want to delete the test file? Y/N     ")
    if clear == "Y":
        deleteFile(test_f)








