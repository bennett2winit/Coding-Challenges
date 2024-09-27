import sys

# Gets the arguments from the command line
try:
    fileName = sys.argv[2]
    fileContent = open(sys.argv[2], "r")
    option = sys.argv[1]
except:
    # After checking for 2 arguements we check to see if the first argument is a file
    try:
        fileContent = open(sys.argv[1], "r")
        fileName = sys.argv[1]
        option = "none"
    # And if it isn't the input is piped
    except:
        fileContent = ""
        fileName = ""
        for line in sys.stdin:
            fileContent += line
        try:
            option = sys.argv[1]
        except:
            option = "none"

content = ''
for i in fileContent:
    for char in i:
        content += char

def sizeCount(content):
    size = len(content.encode('utf-8'))
    return(size) 

def lineCount(content):
    # content = open(file, "r")
    size = 0
    for i in content:
        if i == "\n":
            size += 1
    
    return(size)

def wordCount(content):
    # content = open(file, "r")
    blank = [' ', '\n', '\t', '\r'] 
    words = 0
    whiteSpace = 0
    for i in content:
        for char in i:
            if char in blank and whiteSpace == 0:
                words += 1
                whiteSpace += 1
            elif char not in blank and whiteSpace > 0:
                whiteSpace = 0
    
    return(words)

def charCount(content):
    # content = open(file, "r")
    charCount = 0
    for i in content:
        for char in i:
            charCount += 1
    
    return(charCount)

   
# Here we have the main function. Using a switch statement to speedracer.
 
match option:
    case "-c":
        print(sizeCount(content), fileName) 
    case "-l":
        print(lineCount(content), fileName)
    case "-w":
        print(wordCount(content), fileName)
    case "-m":
        print(charCount(content), fileName)
    case _:
        print(lineCount(content), wordCount(content), sizeCount(content), fileName) 
