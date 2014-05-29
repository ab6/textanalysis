import entityExtraction as ee
import os

text = "Mark works at IBM in Seattle."
stanfordPath = ""

def test_org_entities_stan():
    assert ee.org_entities_stan([("per1", "PER"), ("loc1", "LOC"), ("org1", "ORG"), ("per2", "PER"), ("loc2", "LOC")]) \
           == {'LOC': ['loc1', 'loc2'], 'ORG': ['org1'], 'PER': ['per1', 'per2']}

def test_get_model_name_default():
    assert ee.get_model_name() == '/classifiers/english.all.3class.distsim.crf.ser.gz'

def test_get_model_name_notdefault():
    assert ee.get_model_name(False) == '/classifiers/english.muc.7class.distsim.crf.ser.gz'

#Tests to make sure stanfordPath variable is set above
def test_stanfordPath():
    try:
        assert os.path.isdir(stanfordPath)
    except Exception as e:
        print "Must first set stanfordPath variable"
        raise e
        skiptest(stanfordExtractionTests)

class stanfordExtractionTests():

    def test_extract_entities_stanford(self):
        assert ee.extract_entities_stanford(text, stanfordPath, '/classifiers/english.all.3class.distsim.crf.ser.gz') \
               == [['Mark', 'PERSON'], ['IBM', 'ORGANIZATION'], ['Seattle', 'LOCATION']]

    def test_extract_persons_stanford(self):
        assert ee.extract_persons_stanford(text, stanfordPath, '/classifiers/english.all.3class.distsim.crf.ser.gz') \
               == [('Mark', 1)]

def test_extract_entities_nltk():
    assert ee.extract_entities_nltk(text) == [('Seattle', 1), ('IBM', 1), ('Mark', 1)]
