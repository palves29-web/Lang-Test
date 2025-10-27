import json
import os

class LangEncoding():
    def __init__(self):
        self.data = ''
        with open("recources/json/langEncoding.json", 'r') as file:
            self.data = json.load(file)
            print(self.data)

    def Encode(self, string: str):
        index = 0
        letterindex = 0
        
        constantindexlist = []
        vowelindexlist = []

        constants = self.data['Constants']
        vowels = self.data['Vowels']
        for letter in string:
            letterindex = 0
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
                    if letter == vowel:
                        vowelindexlist.append(index)
                        break
                    letterindex += 1
                index += 1
        print(constantindexlist, vowelindexlist)
LangEncoding().Encode(input("STRING: "))