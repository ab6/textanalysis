"""
Document class to hold a single document plus metadata
"""

__authors__ = "Cristian Capdevila"


class Document(object):
    """
    A class to hold text documents. Eventually, all readers will
    return a Document and all analysis functions will take one.
    """

    def __init__(self, text, name=None, filename=None, caseid=None,
                 recordid=None, casetype=None, isgood=None, comments=None):
        """
        A Document class

        :param text: The actual text.
        :type text: str
        :param name: A name for the document.
        :type name: str
        :param filename: The name of the file containing the document.
        :type filename: str
        :param caseid: An case identifier number.
        :type caseid: int
        :param recordid: Record id number.
        :type recordid: int
        :param casetype: Type of case.
        :type casetype: int
        :param isgood: Is the narrative good?
        :type isgood: bool
        :param comments: Any extra comments.
        :type comments: str
        """
        self.text = text
        self.name = name
        self.filename = filename
        self.caseid = caseid
        self.recordid = recordid
        self.casetype=casetype
        self.isgood=isgood
        self.comments=comments
