import re

wordList = ["1231Asdbc","Asdbasdc123","asdbsdfadc123","asdbasdfc123","1213111asdadsfbc","1231asasdfdbc","asasddbc","asdasbc","asassdbc","asdaadfbc","asdbasdfc"]



def findCommonLength(honeywords):
	wordLenDict = dict()
	for word in honeywords:
		key = len(word)
		if key in wordLenDict:
			wordLenDict[key] += 1
		else:
			wordLenDict[key] = 1
	return wordLenDict



def findNumberOfDigits(wordlist):
	digitCountDict = dict()
	for word in wordlist:
		digitCount = len([c for c in word if c.isdigit()])
		if digitCount in digitCountDict:
			digitCountDict[digitCount] += 1
		else:
			digitCountDict[digitCount] = 1
	return digitCountDict

def removeHoneyWordsWithRecurringNumberOfDigits(wordlist):
	d = findNumberOfDigits(wordList)
	key, value = d.popitem()
	if(value > 3):
		print wordList
		for word in wordList:
			if(len([c for c in word if c.isdigit()]) == key):
				wordList.remove(word)
	return wordList

def findNumberOfDigitsAddedAtTheEnd(wordlist):
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

def findNumberOfFirstCharCapitalizedWords(wordlist):
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


def findNumberOfDigitsAddedAtTheBeginning(wordlist):
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


def removeNoise():
	d = findCommonLength(wordList)
	key, value = d.popitem()
	if(value > 2):
		for word in wordList:
			if(len(word) == key):
				wordList.remove(word)
	return wordList

def parseInputasArray():
	


print wordList
print findNumberOfFirstCharCapitalizedWords()
