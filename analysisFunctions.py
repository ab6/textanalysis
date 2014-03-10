
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