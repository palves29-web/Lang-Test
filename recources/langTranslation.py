import os

class Translate():
    def __init__(self):
        self.fromlangpath = 'recources/other/words.txt'
        self.tolangpath = 'recources/other/encodedWords.txt'

        self.outputpath = 'recources/other/last.txt'

        self.fromlangcontent = ''
        self.tolangcontent = ''

        with open(self.fromlangpath, 'r') as file: 
            self.fromlangcontent = file.read().upper().split(',')
        with open(self.tolangpath) as file:
            self.tolangcontent = file.read().upper().split(',')
    def Translate(self, string: str):
        if self.tolangcontent.__len__() == self.fromlangcontent.__len__():
            index = 0
            returnvalue = []
            finalreturnvalue = ''
            for word in string.split(' '):
                index = 0
                for w1 in self.fromlangcontent:
                    if word.upper() == w1:
                        returnvalue.append(self.tolangcontent[index])
                        break
                    index += 1
            for i in returnvalue.__str__():
                if ord(i) >= 65 and ord(i) <= 90 or i == ' ':
                    finalreturnvalue = f'{finalreturnvalue}{i}'
            
            with open(self.outputpath, 'w') as file:
                file.write(finalreturnvalue)

            print(finalreturnvalue)

Translate().Translate(input('STRING/SENTANCE: '))