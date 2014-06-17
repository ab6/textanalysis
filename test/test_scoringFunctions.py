from textanalysis.scoring import scoringFunctions as sf

text = open("test/sampleText.txt", "r").read()
keywords = open("test/keywords/keywords.txt", "r").read().split()

def test_calculateRelationsScore():
    assert sf.calculateRelationsScore([['Thomas Beresford', 'unknown'], ['Prudence Cowley', 'daughter']],
                                      ["daughter", "father", "sister", "mother"]) == 0.25

def test_calculateCompositeKeywordScore():
    assert sf.calculateCompositeKeywordScore(text, "test/keywords") == 0.06640625

def test_calculateKeywordScore():
    assert sf.calculateKeywordScore(text, keywords) == 0.0625