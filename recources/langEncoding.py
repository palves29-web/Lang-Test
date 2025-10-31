import json
import random
import os

class LangEncoding():
    def __init__(self):
        self.data = ''
        self.words = ''
        with open("recources/json/langEncoding.json", 'r') as file:
            self.data = json.load(file)

        with open("recources/other/words.txt") as file:
            self.words = file.read()

        self.constantindexlist = []
        self.vowelindexlist = []

        self.length = 0

    def Generate(self):
        constantindexlist = self.constantindexlist
        vowelindexlist = self.vowelindexlist

        constants = self.data['Constants']
        vowels = self.data['Vowels']

        returnvalue = ''

        usedindex = False

        index = 0
        while index < self.length:
            for c in constantindexlist:
                if index == c:
                    usedindex = True
                    returnvalue = f"{returnvalue}{constants[random.randint(0, constants.__len__() - 1)]}"

            for v in vowelindexlist:
                if index == v:
                    usedindex = True
                    returnvalue = f"{returnvalue}{vowels[random.randint(0, vowels.__len__() - 1)]}"

            if not usedindex:
                returnvalue = f"{returnvalue} "
            usedindex = False
            index += 1
        return returnvalue

    def Encode(self, string: str):
        index = 0
        letterindex = 0
        
        constantindexlist = self.constantindexlist
        vowelindexlist = self.vowelindexlist

        constants = self.data['Constants']
        vowels = self.data['Vowels']
        for letter in string:
            letterindex = 0
            if index + 1 == len(string):
                checkstring = string[index]
            else:
                checkstring = f'{string[index + 1]}'.upper

            isvowel = False

            for constant in constants:
                if index != 0:
                    letter = letter.lower()
                    constant = constant.lower()
                else:
                    letter = letter.upper()
                if letter == constant:
                    constantindexlist.append(index)
                    for vowel in vowels:
                        if vowel == checkstring:
                            vowelindexlist.append(letterindex)
                            isvowel = True
                            break
                letterindex += 1

            letterindex = 0

            if not isvowel:
                for vowel in vowels:
                    if index != 0:
                        letter = letter.lower()
                        vowel = vowel.lower()
                    else:
                        letter = letter.upper()
                    if index != 0:
                        letter = letter.lower()
                        vowel = vowel.lower()
                    else:
                        letter = letter.upper()
                    if letter == vowel:
                        vowelindexlist.append(index)
                        break
                    letterindex += 1
                index += 1

        self.length = string.__len__()
        return self.Generate()

words = ''

with open("recources/other/words.txt", 'r') as file:
    words = file.read().split(f',')


List = []

for i in words:
    List.append(LangEncoding().Encode(i))

returnValue = ''

for i in List:
    for l in i:
        if ord(l) >= 65 and ord(l) <= 90:
            returnValue = f'{returnValue}{l}'
    if i != List[-1]:
        returnValue = f'{returnValue},'

with open('recources/other/encodedWords.txt', "w") as file:
    file.write(returnValue)