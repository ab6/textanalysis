import nltk
import re


def nsyl(word, d):
    """
    Function needed to check the number of syllables
    :param word - input word
    :param d - syllabic dictionary
    """
    if word.lower() in d.keys():
        return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]
    else:
        return [0]


def getWords(text):
    """
    Total number of words, split on whitespace
    :param text - input text string
    """
    return text.split()


def getTokens(text):
    """
    Total number or tokens, split using nltk tokenize
    :param text - input text string
    """
    tokens = nltk.word_tokenize(text)
    return tokens


def getTotalUniqueWords(text):
    """
    Total number of unique words, split on whitespace
    :param text: input text string
    :return: total number of unique words
    """
    return len(set(text.split()))


def getUniqueTotalRatio(text):
    """
    Ratio of total unique words to total words
    :param text: input text string
    :return: ratio
    """
    if len(getWords(text)) > 0:
        return float(getTotalUniqueWords(text)) / len(getWords(text))
    else: return "NA"


def getAvgWordLength(text):
    """
    Provides average word length
    :param text: input text string
    :return: sum of word lengths divided by total words
    """
    avgWord = 0.0
    words = getTokens(text)
    for word in words:
        avgWord += len(word)
    if len(words) > 0:
        return avgWord / len(words)
    else: return "NA"


def getSentences(text):
    """
    Using nltk sentence detection, finds all sentences in text
    :param text: input text string
    :return: list of sentences
    """
    sent_det = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_det.tokenize(text.strip())
    return sentences


#average length of sentences
#Parameters: list of strings (sentences)
def getAvgSentLen(sentences):
    avgSent = 0.0
    for sentence in sentences:
        avgSent += len(sentence.split())
    if len(sentences) > 0:
        return avgSent / len(sentences)
    else: return "NA"


#Returns a triple with the average number of syllables,
# the total words that were counted, and
# the total number of complex words
def getSyllableInfo(text):
    temp = {}
    d = nltk.corpus.cmudict.dict()
    avgSyl = 0.0
    sylCount = 0.0
    cmplxWords = 0.0
    for word in set(getTokens(text)):
        if word not in temp:
            avgSyl += nsyl(word, d)[0]
            temp[word] = avgSyl
        else:
            avgSyl = temp[word]
        if avgSyl > 0:
            sylCount += 1
            if avgSyl >= 3:
                cmplxWords += 1
    return (avgSyl, sylCount, cmplxWords)


#Gunning fog index
# Parameters:
#   number of tokens
#   number of sentences
#   number of complex words
#   total number of syllables
def getGFIndex(numTokens, numSentences, cmplxWords, sylCount):
    if numSentences > 0 and sylCount > 0:
        return (.4 * ((numTokens / numSentences) + 100 * (cmplxWords / sylCount)))
    else: return "NA"


#Flesch Reading Ease
# Parameters:
#   number of tokens
#   number of sentences
#   average number of syllables
#   total number of syllables
def getFRES(numTokens, numSentences, avgSyl, sylCount):
    if numSentences > 0 and sylCount > 0:
        return (206.835 - 1.015 * (numTokens / numSentences) - 84.6 * (avgSyl / sylCount))
    else: return "NA"


#Flesch-Kincaid Grade Level
# Parameters:
#   number of tokens
#   number of sentences
#   average number of syllables
#   total number of syllables
def getFKGL(numTokens, numSentences, avgSyl, sylCount):
    if numSentences > 0 and sylCount > 0:
        return (0.39 * (numTokens / numSentences) + 11.8 * (avgSyl / sylCount) - 15.59)
    else: return "NA"


# Gets spelling accuracy
# Parameters: list of words
def getSpellAcc(words):
    import enchant

    sc = enchant.Dict("en_US")
    #Number of misspelled words
    count = 0.0
    for word in words:
        if sc.check(word):
            count += 1
    if len(words) > 0:
        return (count / len(words))
    else: return 0

