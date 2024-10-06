import sys

fileContent = ''
for line in sys.stdin:
    fileContent += line

def main(file):
    bracket = bracketCheck(file)
    keyValid = keyCheck(file)
    if bracket > 0:
        print('check invalid JSON file: ' + str(bracket))
    elif keyValid > 0:
        print('invalid JSON file: err. no. ' + str(keyValid))
    else:
        print("Valid JSON")

def bracketCheck(file):
    opened = False
    nested = 0
    closed = False
    for i in file:
        if i == '{' and nested == 0:
            opened = True
            closed = False
            nested += 1
        elif i == '{' and nested != 0:
            nested += 1
        elif i == '}' and opened == False:
            return 1
        elif i == '}' and nested == 1:
            closed = True
            opened = False
        elif i == '}':
            nested -= 1
    if opened == False and closed == True:
        return 0
    else:
        return 2

def keyCheck(file):
    keyCount = 1
    brackCount = 0
    key = False
    value = False
    keyVal = ''
    valueVal = ''
    # Iterate through file to check for key and value combos. ',' resets them so that we can check for multiple values
    letter = 0
    for num in range(len(file)):
        i = file[letter]
        if i == ':':
            key = checkKey(keyVal)
            if key == False:
                print(f"Key Error in line {keyCount}")
                return 4
            keyVal = ''
        elif i == '{' and brackCount == 0:
            brackCount += 1
        elif i == ',' and key != True:
            print("no key found")
        elif i == ',' and value == True:
            valueVal = ''
            key = False
            value = False
            keyCount += 1
        elif i == ',' and value == False:
            value = checkValue(valueVal)
            if value == False:
                print(f"Value Error in line {keyCount}")
                return 6
            valueVal = ''
            key = False
            value = False
            keyCount += 1
        elif key == False and i != ':':
            keyVal += i
        elif key == True and i == "}":
            keyCount += 1
            value = checkValue(valueVal)
            if value == False:
                print(f"Value Error in line {keyCount}")
                return 6
                break
        elif key == True and i == "{" and brackCount > 0:
            brackCount += 1
            value, letter = getBrackets(file[letter + 1:], keyCount, letter)
            keyCount += 1
        elif key == True and i != ',':
            valueVal += i
        letter += 1
        if letter >= len(file):
            break
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
    elif val.strip() == '[]':
        return True
    elif val.strip() in validVars:
        return True
    elif isinstance(val, list):
        return True
    else:
        try:
            int(val.strip())
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
    
def getBrackets(file, lineNo, num):
    info = ''
    for letter in file:
        if letter == '}':
            num += 1
            break
        elif letter == '{':
            num += 1
            getBrackets(file[(file.index(letter) + 1):], lineNo, num)
        else:
            num += 1
            info += letter
    keyNum = keyCheck(info)
    if len(info.strip()) == 0:
        return True,num 
    elif keyNum > 0:
        print(f"key error on line {lineNo}")
        return False,num 
    else:
        return True,num

main(fileContent)

'''
1 = file doesn't start with a {
2 = Undefined
3 = too many quotes
4 = no string
5 = wrong value type
6 = invalid value
'''

