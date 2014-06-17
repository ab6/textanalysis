from infoExtraction import keywordExtraction as ke

def identifyPersons(text, entities):
    '''
    Given entities already found in text, determine their relation to the child or case.
    :param text: target text
    :param entities: list of Persons
    :return: List of person, relation tuples
    '''
    # take persons.txt and for each entity,
    # find entry in persons that is closest in distance to that entity within given sentence

def calculateCompositeKeywordScore(keywordScoreDict):
    '''
    Take multiple keyword scores and produce aggregated score
    :param keywordScoreDict: dict with all keyword scores
    :return: composite keyword score
    '''
    score = 0.0
    return score

def calculateKeywordScore(text, keywords):
    '''
    Calculate keyword score for text
    :param text: target text
    :param keywords: list of keywords
    :return: keyword score
    '''
    score = 0.0
    keyworddict = ke.getKeywords(text, keywords)
    return score

