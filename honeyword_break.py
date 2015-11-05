import sys
import csv
from difflib import SequenceMatcher
import re

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def findNumberOfDigits(wordlist):
    digitCountDict = dict()
    for word in wordlist:
        digitCount = len([c for c in word if c.isdigit()])
        if digitCount in digitCountDict:
            digitCountDict[digitCount] += 1
        else:
            digitCountDict[digitCount] = 1
    return digitCountDict

def removeHoneyWordsWithRecurringNumberOfDigits(wordList):
    d = findNumberOfDigits(wordList)
    key, value = d.popitem()
    if(value > 3):
        print wordList
        for word in wordList:
            if(len([c for c in word if c.isdigit()]) == key):
                wordList.remove(word)
    return wordList

def findNumberOfDigitsAddedAtTheEnd(wordList):
    numDigitDict = dict()
    for word in wordList:
        key =0
        if re.match('.*?([0-9]+)$', word):
            key = len(re.match('.*?([0-9]+)$', word).group(1))
        if key in numDigitDict:
            numDigitDict[key] += 1
        else:
            numDigitDict[key] = 1
    return numDigitDict

def findNumberOfFirstCharCapitalizedWords(wordList):
    capDict = dict()
    for word in wordList:
        key = 0
        if(word.istitle()):
            key = 1
        if key in capDict:
            capDict[key] += 1
        else:
            capDict[key] = 1
    return capDict


def findNumberOfDigitsAddedAtTheBeginning(wordList):
    numDigitDict = dict()
    for word in wordList:
        key =0
        if re.match('([0-9]+).*?$', word):
            key = len(re.match('([0-9]+).*?$', word).group(1))
        if key in numDigitDict:
            numDigitDict[key] += 1
        else:
            numDigitDict[key] = 1
    return numDigitDict

def read_data(filename, num_set, num_sweetword):
    data = []
    with open(filename, 'r') as f:
        csv_data = csv.reader(f, delimiter=',')
        for row in csv_data:
            data.append(row)
    return data

def read_txt(filename):
    data =[]
    f = open(filename, 'r')
    for line in f:
        data.append(line.rstrip())
    return data

def getNumberofDigitsAddedAtTheBeginningforString(word):
    if re.match('([0-9]+).*?$', word):
        return len(re.match('([0-9]+).*?$', word).group(1))
    else:
        return 0

def getNumberofDigitsAddedAtTheEndforString(word):
    if re.match('.*?([0-9]+)$', word):
        return len(re.match('.*?([0-9]+)$', word).group(1))
    else:
        return 0
        
def parseDataArray(data):
    honeyArray = []
    for line in data:
        wordArray = line.split(",")
        honeyArray += wordArray
    return honeyArray

def findPatternForNoise(input_data):
    pass

def guess_honeyword(input_data):
    pass
 

def main(num_sweetword, num_set, filename):
    #input_data = read_data(filename, num_set, num_sweetword)
    input_data = read_txt(filename)
    inputArray = parseDataArray(input_data)
    capDict = findNumberOfFirstCharCapitalizedWords(inputArray)
    begDigitDic = findNumberOfDigitsAddedAtTheBeginning(inputArray)
    endDigitDic = findNumberOfDigitsAddedAtTheEnd(inputArray)
    
    # guesses = guess_honeyword(input_data)
    # for guess in guesses:
    #     print guess
 
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])