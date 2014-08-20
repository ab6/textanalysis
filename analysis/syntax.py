import nltk
import basicStats as bs
import stat_parser as sp
from collections import Counter

def tagPOS(text):
    """

    :param text:
    :return:
    """
    tokens = bs.getTokens(text)
    output = nltk.pos_tag(tokens)
    return output

def getParser(package):
    """
    Get specific parser in order not to have to initiate it every time
    :param package: pass in name of parser software package
    :return: chosen parser
    """
    if package is "pyStatParser":
        return sp.Parser()

def tagStatParser(text, parser):
    """
    Parse text with pyStatParser
    :param text: input text string
    :param parser: instantiated parser
    :return: parsed text
    """
    if text.startswith("("):
        text = text.replace("(", "[")
    return parser.parse(text)

def getSentenceTypes(text, parser):
    types = Counter()
    sents = bs.getSentences(text)
    for sent in sents:
        if len(sent.split()) < 20:
            parsed = tagStatParser(sent, parser)
            if hasattr(parsed, 'node'):
                types[parsed.flatten().node] += 1
    return types

