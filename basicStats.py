import nltk
import os
import re

#Get the names of certain files in a directory
def getFileNames(directory, matchPattern=""):
    dirList = os.listdir(directory)
    filenames = []
    for fname in dirList:
        if re.search(matchPattern, fname):
            filenames.append(fname)
    return filenames

#Function needed to check the number of syllables
def nsyl(word, d):
	if word.lower() in d.keys():
		return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
	else:
		return [0]

#total number of words, split on whitespace
def getWords(text):
    return text.split()

#total number or tokens, split using nltk tokenize
def getTokens(text):
    tokens = nltk.word_tokenize(text)
    return tokens

#total number of unique words, split on whitespace
def getTotalUniqueWords(text):
    return len(set(text.split()))

#ratio of total unique words to total words
def getUniqueTotalRatio(text):
    return float(getTotalUniqueWords(text))/len(getWords(text))

#average word length
def getAvgWordLength(text):
    avgWord = 0.0
    words = getTokens(text)
    for word in words:
        avgWord += len(word)
    return avgWord/len(words)

#get sentences
def getSentences(text):
    sent_det = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_det.tokenize(text.strip())
    return sentences

# Utility function to return a list of sentences.
# @param text The text that must be split in to sentences.
# From RAKE code
def splitSentences(text):
	sentenceDelimiters = re.compile(u'[.!?,;:\t\\-\\"\\(\\)\\\'\u2019\u2013]')
	sentenceList = sentenceDelimiters.split(text)
	return sentenceList

#average length of sentences
def getAvgSentLen(sentences):
    avgSent = 0.0
    for sentence in sentences:
        avgSent += len(sentence.split())
    return avgSent/len(sentences)

#Returns a triple with the average number of syllables,
# the total words that were counted, and
# the total number of complex words
def getSyllableInfo(text):
    temp = {}
    d = nltk.corpus.cmudict.dict()
    avgSyl = 0.0
    sylCount = 0.0
    cmplxWords = 0.0
    for word in set(getTokens(text)):
        if word not in temp:
            avgSyl += nsyl(word, d)[0]
            temp[word] = avgSyl
        else:
            avgSyl = temp[word]
        if avgSyl > 0:
            sylCount += 1
            if avgSyl >= 3:
                cmplxWords += 1
    return (avgSyl, sylCount, cmplxWords)

#Gunning fog index
def getGFIndex(numTokens, numSentences, cmplxWords, sylCount):
    return (.4*((numTokens/numSentences) + 100*(cmplxWords/sylCount)))

#Flesch Reading Ease
def getFRES(numTokens, numSentences, avgSyl, sylCount):
    return (206.835 - 1.015*(numTokens/numSentences) - 84.6*(avgSyl/sylCount))

#Flesch-Kincaid Grade Level
def getFKGL(numTokens, numSentences, avgSyl, sylCount):
    return (0.39*(numTokens/numSentences)+11.8*(avgSyl/sylCount) - 15.59)

# def getSpellAcc(words):
#     import enchant
#     sc = enchant.Dict("en_US")
#     #Number of misspelled words
#     count = 0.0
#     for word in words:
#         if sc.check(word):
#             count += 1
#     return (count/len(words))

