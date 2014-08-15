"""
General utility functions
"""

from ntpath import basename
from document import Document

def read_plaintext(path_to_file):
    """
    Reads in a plaintext file containing a single document.

    :param path_to_file: The full path to the file containing the document.
    :type path_to_file: str.

    :returns: [Document] -- A list of Document objects.

    :raises: IOError
    """
    with open(path_to_file, 'r') as document_file:
        filename = basename(path_to_file)
        text = document_file.read()
        return [Document(text, filename=filename)]

def read_pipesv(path_to_file):
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
            documents.append(Document(text, name=name, filename=filename))
        return documents
