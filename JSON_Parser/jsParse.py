import sys

fileContent = ''
for line in sys.stdin:
    fileContent += line 


def bracketCheck(file):
    opened = False
    closed = False
    for i in fileContent:
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
print(bracketCheck(fileContent))
        
'''
1 = file doesn't start with a {
2 = Undefined
'''

