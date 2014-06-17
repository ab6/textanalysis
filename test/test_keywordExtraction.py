from textanalysis.infoExtraction import keywordExtraction as ke

text = open("test/sampleText.txt", "r").read()
keywords = open("test/keywords/keywords.txt", "r").read().split()

def test_getKeywordFreqs():
    assert ke.getKeywordFreqs(text, keywords) == {'cowley': 4, 'daughter': 1, 'month': 11}

def test_getAllKeywordsLists():
    assert ke.getAllKeywordsLists("test/keywords") == {'keywords': ['daughter', 'cowley', 'month'],
                                                       'keywords2': ['keyword1', 'keyword2', 'keyword3']}

def test_loadKeywords():
    assert ke.loadKeywords("test/keywords/keywords.txt") == ['daughter', 'cowley', 'month']

def test_getContext():
    assert ke.getContext('daughter', text) == \
           ['Abridged biography of Miss Prudence Cowley, fifth daughter of Archdeacon Cowley of Little Missendell, Suffolk.']

