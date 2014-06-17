from textanalysis.infoExtraction import keywordExtraction as ke
from textanalysis.analysis import basicStats as bs

def calculateRelationsScore(relationsList, possibles):
    '''
    Calculate score based on the mentions of named entities and their relationship to case
    :param text: target text
    :param relationsList: list of tuples of entities and their relations
    :return: relations score
    '''
    score = 0.0
    #Count number of relations in possibles and divide by number of possibles
    for name, relation in relationsList:
        if relation in possibles:
            score += 1
    return score/len(possibles)

def calculateCompositeKeywordScore(text, keywordDir):
    '''
    Take keyword directory and produce aggregated score
    :param text: target text
    :param keywordDir: directory storing keyword lists
    :return: composite keyword score
    '''
    compscore = 0.0
    keywordLists = ke.getAllKeywordsLists(keywordDir)
    scores = []
    for entry in keywordLists:
        scores.append(calculateKeywordScore(text, keywordLists[entry]))
    #Add up individual keyword scores
    for score in scores:
        compscore = compscore + score
    return compscore

def calculateKeywordScore(text, keywords):
    '''
    Calculate keyword score for text
    :param text: target text
    :param keywords: list of keywords
    :return: keyword score
    '''
    score = 0.0
    keyworddict = ke.getKeywordFreqs(text, keywords)
    for k in keyworddict:
        score += keyworddict[k]
    #Count up keyword frequencies and divide by total number of words in text
    score = score/len(bs.getWords(text))
    return score

