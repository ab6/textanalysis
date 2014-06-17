Required libraries:
	enchant
	pyenchant
	nltk
	from nltk.download(): cmudict, punkt, words, & maxent_ne_chunker
	pytest (if running unit tests)

If doing entity extraction, need the stanford tagger downloaded and unzipped.
http://nlp.stanford.edu/software/CRF-NER.shtml

Notes:
textanalysis directory needs to be in same parent directory as code you are running.

Testing:
Uncomment out test_getSpellAcc function in test_basicStats.py
Set stanfordPath variable in test_entityExtraction.py as path to where you unzipped the stanford tagger.
Run tests using the command "py.test"
