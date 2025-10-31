import os

def Slice(string: str, i1: int, i2: int):
    returnvalue = string[:i1] + string[i2:]
    return returnvalue

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
    def TranslateTo(self, string: str):
        if self.tolangcontent.__len__() == self.fromlangcontent.__len__():
            index = 0
            returnvalue = []
            finalreturnvalue = ''
            for word in string.split(' '):
                newword = ''
                index = 0
                for w1 in self.fromlangcontent:
                    if word[-1] == '.':
                        newword = word.strip('.')
                    else:
                        newword = word
                    if newword.upper() == w1:
                        returnvalue.append(self.tolangcontent[index])
                        print(self.tolangcontent[index])
                        break
                    index += 1

                if word[-1] == '.':
                    returnvalue.append('.')

            check = False
            for i in returnvalue.__str__():
                if ord(i) >= 65 and ord(i) <= 90:
                    finalreturnvalue = f'{finalreturnvalue}{i}'
                if i == ' ' and not check:
                    check = True
                    finalreturnvalue = f'{finalreturnvalue}{i}'
                elif i == '.':
                    check = True
                    finalreturnvalue = f'{finalreturnvalue}{i}'
                elif i == ' ' and check: 
                    check = False

            if ' ' == returnvalue.__str__()[0]:
                    finalreturnvalue = Slice(finalreturnvalue.__str__())

            with open(self.outputpath, 'w') as file:
                file.write(finalreturnvalue)
        else:
            print('WHAT', self.tolangcontent.__len__(), self.fromlangcontent.__len__())
    
    def TranslateFrom(self, string: str):
        if self.tolangcontent.__len__() == self.fromlangcontent.__len__():
            index = 0
            returnvalue = []
            finalreturnvalue = ''
            for word in string.split(' '):
                newword = ''
                index = 0
                for w1 in self.tolangcontent:
                    if word[-1] == '.':
                        newword = word.strip('.')
                    else:
                        newword = word
                    if newword.upper() == w1:
                        returnvalue.append(self.fromlangcontent[index])
                        break
                    index += 1

                if word[-1] == '.':
                    returnvalue.append('.')

            check = False
            for i in returnvalue.__str__():
                if ord(i) >= 65 and ord(i) <= 90:
                    finalreturnvalue = f'{finalreturnvalue}{i}'
                if i == ' ' and not check:
                    check = True
                    finalreturnvalue = f'{finalreturnvalue}{i}'
                elif i == '.':
                    check = True
                    finalreturnvalue = f'{finalreturnvalue}{i}'
                elif i == ' ' and check: 
                    check = False

            if ' ' == returnvalue.__str__()[0]:
                    finalreturnvalue = Slice(finalreturnvalue.__str__())

            with open(self.outputpath, 'w') as file:
                file.write(finalreturnvalue)

            print(finalreturnvalue)

Translate().TranslateTo(input('STRING/SENTANCE: '))