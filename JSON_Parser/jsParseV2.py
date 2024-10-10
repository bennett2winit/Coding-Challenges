import sys

class file:
    def __init__(self, fileName):
        print(fileName)
        self.fileName = fileName

    def getContent(self):
        for line in self.fileName:
            print(line)

    def printContent(self):
        print(self.getContent())

JSON = file(sys.stdin)
JSON.getContent()
