import sys

fileContent = ''
for line in sys.stdin:
    fileContent += line

def main(file):
    bracket = bracketCheck(file)
    keyValid = keyCheck(file)
    if bracket > 0:
        print('invalid JSON file: ' + str(bracket))
    elif keyValid > 0:
        print('invalid JSON file: err. no. ' + str(keyValid))
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
    keyCount = 1
    key = False
    value = False
    keyVal = ''
    valueVal = ''
    # Iterate through file to check for key and value combos. ',' resets them so that we can check for multiple values
    for i in file:
        if i == ':':
            key = checkKey(keyVal)
            if key == False:
                print(f"Key Error in line {keyCount}")
                return 4
            keyVal = ''
        elif i == ',' and key != True:
            print("no key found")
        elif i == ',':
            value = checkValue(valueVal)
            if value == False:
                print(f"Value Error in line {keyCount}")
                return 6
            keyCount += 1
            valueVal = ''
            key = False
            value = False
        elif key == False and i != ':':
            keyVal += i
        elif key == True and i == "}":
            value = checkValue(valueVal)
            if value == False:
                print(f"Value Error in line {keyCount}")
                return 6
                break
        elif key == True and i != ',':
            valueVal += i
    # The final conditional checks to see if, after all the resets, key and value are BOTH true
    if key == True and value == True:
        return 0
    else:
        return 2

def checkValue(val):
    validVars = ['null', 'true', 'false']
    stringCheck = checkKey(val)
    if stringCheck == True:
        return True
    elif val.strip() in validVars:
        return True
    else:
        try:
            int(val)
            return True
        except:
            return False

def checkKey(val):
    quoteCounter = 0
    for i in val:
        if i == '"':
            quoteCounter += 1
    if quoteCounter == 2:
        return True
    else:
        return False
    


main(fileContent)

'''
1 = file doesn't start with a {
2 = Undefined
3 = too many quotes
4 = no string
5 = wrong value type
6 = invalid value
'''

