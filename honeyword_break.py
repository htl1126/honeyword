import sys
import csv
from difflib import SequenceMatcher
import re
import string
import difflib

numberOfWords= 1.0
firstCapitalizedWords=0
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
"""
def commonLength(wordList):
    dictionary=dict()
    for word in wordlist:
        if len(word) in dictionary:
            dictionary[len(word)]+=1
        else 
"""
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
    firstCapitalizedWords = capDict[1] / numberOfWords
    print "First Capitalized Words"
    print firstCapitalizedWords
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

def hasSpecialChars(str):
    return any(char in set(string.punctuation) for char in str)

def countSpecial(word):
    numSpecChar = 0
    for letter in word:
        if hasSpecialChars(letter):
            numSpecChar += 1
    return numSpecChar

#take in input text file, ouput a dictionary of special characters {1, 20; 2, 30...etc}
#NOTE that for key = 4, that accounts for 4 or more special characters
def freqSpecial(input):
    freqDict = dict([(0,0),(1, 0),(2,0),(3,0),(4,0)])
   # for i, wordList in enumerate(input):
    numSpecChar = 0
    for word in input:

        numFreq = countSpecial(word)
            #print numFreq
        numSpecChar = numFreq
        '''for letter in word:
            if hasSpecialChars(letter):
                numSpecChar += 1'''

        if (numSpecChar > 4):
            freqDict[4] += 1
        else:      
            freqDict[numSpecChar]+= 1
        ''' if numFreq > 4:
            freqDict[4] += 1
        else:
            freqDict[numFreq] += 1'''
    return freqDict

def readRockYouData(size=None, filename='rockyou-withcount.txt'):
    word_lst = []
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            word = line.split(' ')[1]
            word_lst.append(word)
            count += 1
            if size and count == size:
                break
    return word_lst


def findMostSimilarStringFromPool(word):
    cut_off_val = 0.9
    string_pool = readRockYouData(100)
    output_string_pool =[]
    output_string_pool.append( difflib.get_close_matches(word, string_pool,
                                                   cutoff=cut_off_val))
    if len(output_string_pool) and word != output_string_pool[0]:
        return 1
    else:
        return 0

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

 

def main(num_sweetword, num_set, filename):
    #input_data = read_data(filename, num_set, num_sweetword)
    input_data = read_txt(filename)
    inputArray = parseDataArray(input_data)
    capDict = findNumberOfFirstCharCapitalizedWords(inputArray)
    begDigitDic = findNumberOfDigitsAddedAtTheBeginning(inputArray)
    endDigitDic = findNumberOfDigitsAddedAtTheEnd(inputArray)
    splCharDic = freqSpecial(inputArray)
    print findMostSimilarStringFromPool(inputArray)

    print countSpecial("he@#$o")
    #print inputArray
    # guesses = guess_honeyword(input_data)
    # for guess in guesses:
    #     print guess

if __name__ == '__main__':

    honeywords = sys.argv[1]
    passwords =sys.argv[2]
    numberOfWords = float(honeywords)* float(passwords)
    main(honeywords,passwords , sys.argv[3])
    
    