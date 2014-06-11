
def getFileNames(directory, matchPattern=""):
    """Get the names of certain files in a directory and return list of names

    :param directory - path to directory with files
    :param matchPattern - pattern to match if getting only certain file names (default "")
    """
    import os
    import re
    dirList = os.listdir(directory)
    filenames = []
    for fname in dirList:
        if re.search(matchPattern, fname):
            filenames.append(fname)
    return filenames

def getContext(keyword, text):
    """Find all sentences within a given text that contain the specified keyword or phrase and return list of sentences

    :param keyword - target keyword
    :param text - input text string
    """
    from basicStats import getSentences
    matches = []
    sentences = getSentences(text)
    for sentence in sentences:
        if keyword in sentence:
            matches.append(sentence)
    return matches

def getAllStats(text):
    """Return list with all stats

    :param text - input text string
    """
    import basicStats as bs
    textStats = []
    tokens = bs.getTokens(text)
    sentences = bs.getSentences(text)
    sylInfo = bs.getSyllableInfo(text)
    avgSyl = sylInfo[0]
    sylCount = sylInfo[1]
    cmplxWords = sylInfo[2]
    textStats.append(len(tokens))
    textStats.append(bs.getTotalUniqueWords(text))
    textStats.append(bs.getUniqueTotalRatio(text))
    textStats.append(bs.getAvgWordLength(text))
    textStats.append(len(sentences))
    textStats.append(bs.getAvgSentLen(sentences))
    textStats.append(avgSyl/sylCount)
    textStats.append(bs.getGFIndex(len(tokens), len(sentences), cmplxWords, sylCount))
    textStats.append(bs.getFRES(len(tokens), len(sentences), avgSyl, sylCount))
    textStats.append(bs.getFKGL(len(tokens), len(sentences), avgSyl, sylCount))
    return textStats

def getAllLabels():
    """Return a list of column headings for stats returned from getAllStats function"""
    return ["TotTokens", "UniqueWords", "Unique2Total", "AvgWordLen", "TotSents",
            "AvgSentLen", "AvgSyllables", "GFIndex", "FRES", "FKGL"]


def writeCSV(filePath, labels, rows):
    """Given a output file path, headers and data, will write desired csv file

    :param filePath - file path string
    :param labels - list of labels
    :param rows - list of rows
    """
    import csv
    with open(filePath, 'w') as output:
        writer = csv.writer(output, delimiter=',')
        writer.writerow(labels)
        for row in rows:
 		    writer.writerow(row)