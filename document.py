"""
Document class to hold a single document plus metadata
"""

__authors__ = "Cristian Capdevila"


class Document(object):
    """
    A class to hold text documents. Eventually, all readers will
    return a Document and all analysis functions will take one.
    """

    def __init__(self, text, name=None, filename=None, idnum=None):
        """
        A Document class

        :param text: The actual text.
        :type text: str.
        :param name: A name for the document.
        :type name: str.
        :param filename: The name of the file containing the document.
        :type filename: str.
        :param idnum: An identifier number.
        :type idnum: int.

        """
        self.text = text
        self.name = name
        self.filename = filename
        self.idnum = idnum
