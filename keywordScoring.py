

def getKeywordScore(text, keywords):
    '''

    :param text:
    :param keywords: list of keywords
    :return: keyword score
    '''
    score = 0.0
    return score

def loadKeywords(keywordFile):
    '''Open keyword file and return list of those keywords

    :param keywordFile: file with list of keywords, one keyword per line
    :return: list of keywords
    '''
    with open(keywordFile, 'r') as f:
        keywordList = []
        for line in f.readlines():
            keywordList.append(line.strip().lower())
    return keywordList