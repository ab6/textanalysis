"""
General utility functions
"""

from ntpath import basename
from textanalysis.document import Document

def read_pipes_old(path_to_file):
    """
    Reads in a file with documents separated by

    :param path_to_file: The full path to the file containing the document.
    :type path_to_file: str.

    :returns: [Document] -- A list of Document objects.

    :raises: IOError
    """
    with open(path_to_file, 'r') as document_file:
        filename = basename(path_to_file)
        texts = document_file.read().replace('\n', "").split('|')
        documents = [Document(text, filename=filename) for text in texts]
        return documents

def read_pipes(path_to_file):
    """
    Reads in a file formatted with one document per line, with a name and the
    text seperated by the '|' character.

    :param path_to_file: The full path to the fle containing the documents.
    :type path_to_file: str.

    :returns: [Document] -- A list of Document objects

    :raises: IOError
    """
    with open(path_to_file, 'r') as document_file:
        filename = basename(path_to_file)
        documents = list()
        for line in document_file:
            line_tuple = line.strip('\n').split('|')
            if len(line_tuple) is not 2:
                raise IOError("Error reading {}:"
                              "Not a pipesv file.".format(filename))
            name, text = line_tuple
            documents.append(Document(' '.join(text.split()).strip(), name=name, filename=filename))
        return documents
