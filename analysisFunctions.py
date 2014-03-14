
#Get the names of certain files in a directory
def getFileNames(directory, matchPattern):
    import os
    import re
    dirList = os.listdir(directory)
    filenames = []
    for fname in dirList:
        if re.search(matchPattern, fname):
            filenames.append(fname)
    return filenames

#Find all sentences within a given text that contain the specified keyword or phrase
def getContext(keyword, text):
    from basicStats import splitSentences
    matches = []
    sentences = splitSentences(text)
    for sentence in sentences:
        if keyword in sentence:
            matches.append(sentence)
    return matches

def getAllStats(text):
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
    return ["TotTokens", "UniqueWords", "Unique2Total", "AvgWordLen", "TotSents",
            "AvgSentLen", "AvgSyllables", "GFIndex", "FRES", "FKGL"]

def writeCSV(filePath, labels, rows):
    import csv
    with open(filePath, 'w') as output:
        writer = csv.writer(output, delimiter=',')
        writer.writerow(labels)
        for row in rows:
 		    writer.writerow(row)