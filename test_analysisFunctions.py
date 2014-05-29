import analysisFunctions as af
import os
import shutil

text = "Here is some text. This text string is for testing."
dirname = os.path.dirname(os.path.realpath(__file__)) + "/test"

def setup():
    os.makedirs(dirname)
    f = open(dirname + "/doc1.txt", 'w')
    g = open(dirname + "/doc2.txt", 'w')
    f.close()
    g.close()

def test_getFileNames_noPattern():
    assert af.getFileNames(dirname) == ["doc1.txt", "doc2.txt"]

def test_getFileNames_Pattern():
    assert af.getFileNames(dirname, "2") == ["doc2.txt"]

def test_getContext():
    assert af.getContext("string", text) == [" This text string is for testing"]

def test_getAllStats():
    assert af.getAllStats(text)== [11, 9, 0.9, 3.8181818181818183, 2, 5.0, 0.9, 34.0, 125.62000000000002, -3.0199999999999996]


def test_getAllLabels():
    assert af.getAllLabels() == ["TotTokens", "UniqueWords", "Unique2Total", "AvgWordLen", "TotSents",
            "AvgSentLen", "AvgSyllables", "GFIndex", "FRES", "FKGL"]

def writeCSV(filePath, labels, rows):
    af.writeCSV(dirname + "text.csv", ["label1", "label2"], [["row11", "row12"], ["row21", "row22"]])
    test = open(dirname + "text.csv")
    text = test.read()
    assert text.split()[2] == "row11"

def teardown():
    shutil.rmtree(dirname)