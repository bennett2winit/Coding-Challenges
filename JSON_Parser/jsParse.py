import sys

fileContent = ''
for line in sys.stdin:
    fileContent += line

def main(file):
    bracket = bracketCheck(file)
    keyVal = keyCheck(file)
    if bracket > 0:
        print('invalid JSON file: ' + str(bracket))
    elif keyVal > 0:
        print('invalid JSON file: ' + str(keyVal))
    else:
        print("Valid JSON")

def bracketCheck(file):
    opened = False
    closed = False
    for i in file:
        if i == '{':
            opened = True
            closed = False
        elif i == '}' and opened == False:
            return 1
        elif i == '}' and opened == True:
            closed = True
            opened = False
    if opened == False and closed == True:
        return 0
    else:
        return 2

def keyCheck(file):
    key = False
    value = False
    quoteCounter = 0
    # Iterate through file to check for key and value combos. ',' resets them so that we can check for multiple values
    for i in file:
        if i == '"':
            quoteCounter += 1
        elif quoteCounter > 2:
            return 3
        elif quoteCounter == 2 and i == ':':
            key = True
            quoteCounter = 0
        elif key == True and quoteCounter == 2  and i == '}':
            value = True
        elif quoteCounter == 2 and i == ',':
            key = False
            value = False
            quoteCounter = 0
    if key == True and value == True:
        return 0
    else:
        return 2
       
main(fileContent)

'''
1 = file doesn't start with a {
2 = Undefined
3 = too many quotes
'''

