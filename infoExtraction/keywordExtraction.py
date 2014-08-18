import re
from collections import Counter
from textanalysis.analysis import analysisFunctions as af
from textanalysis.analysis import basicStats as bs

def getKeywordFreqs(text, keywords):
    '''
    Find and count all keywords in the text
    :param text: target text
    :param keywords: list of keywords
    :return: dict with keywords found and their frequency
    '''
    keywordctr = Counter()
    for keyword in keywords:
        matches = re.findall(keyword, text.lower())
        if matches > -1:
            keywordctr[keyword] = len(matches)
    return keywordctr

def getAllKeywordsLists(keywordDir):
    '''
    Load all keyword lists into dict with classification
    :param keywordDir: directory containing keyword lists
    :return: dict with type of keywords as keys and list of keywords as value
    '''
    keywordDict = {}
    files = af.getFileNames(keywordDir)
    for file in files:
        keywords = loadKeywords(keywordDir + "/" + file)
        keywordDict[file[:-4]] = keywords
    return keywordDict

def loadKeywords(keywordFile):
    '''
    Open keyword file and return list of those keywords
    :param keywordFile: file with list of keywords, one keyword per line
    :return: list of keywords
    '''
    with open(keywordFile, 'r') as f:
        keywordList = []
        for line in f.readlines():
            keywordList.append(line.strip().lower())
    return keywordList

def getContext(keyword, text):
    """
    Find all sentences within a given text that contain the specified keyword or phrase and return list of sentences
    :param keyword - target keyword
    :param text - input text string
    """
    matches = []
    sentences = bs.getSentences(text)
    for sentence in sentences:
        if keyword in sentence:
            matches.append(sentence)
    return matches

