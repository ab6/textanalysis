from textanalysis.analysis import basicStats as bs
import nltk

text = "Here is some text. This text string is for testing."

def test_nsyl():
    d = nltk.corpus.cmudict.dict()
    assert bs.nsyl("happy", d) == [2]

def test_getWords():
    assert bs.getWords(text) == ["Here", "is", "some", "text.", "This", "text", "string", "is", "for", "testing."]

def test_getTokens():
    assert bs.getTokens(text) == ['Here', 'is', 'some', 'text.', 'This', "text", 'string', 'is', 'for', 'testing', '.']

def test_getTotalUniqueWords():
    assert bs.getTotalUniqueWords(text) == 9

def test_getUniqueTotalRatio():
    assert bs.getUniqueTotalRatio(text) == 0.9

def test_getAvgWordLength():
    assert bs.getAvgWordLength(text) == 3.8181818181818183

def test_getSentences():
    assert bs.getSentences(text) == ["Here is some text.", "This text string is for testing."]

def test_getAvgSentLen():
    assert bs.getAvgSentLen(text) == 0.8235294117647058

def test_getSyllableInfo():
    assert bs.getSyllableInfo(text) == (9.0, 10.0, 8.0)

def test_getGFIndex():
    assert bs.getGFIndex(10, 2, 0, 11) == 2.0

def test_getFRES():
    assert bs.getFRES(10, 2, 1.1, 11) == 193.3

def test_getFKGL():
    assert bs.getFKGL(10, 2, 1, 11) == -13.64

#Can only be run on linux (unless you got enchant to install on something else)
#def test_getSpellAcc(words):
# def test_getSpellAcc():
#     assert bs.getSpellAcc(["Here", "is", "some", "text", "This", "text", "string", "is", "for", "testing"]) == 1

