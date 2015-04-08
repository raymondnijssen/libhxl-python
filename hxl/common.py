"""
Common information for HXL.
"""

TOKEN = r'[A-Za-z][_0-9A-Za-z]*'

class HXLException(Exception):
    """Base class for all HXL-related exceptions."""

    def __init__(self, message):
        super(Exception, self).__init__(message)
        self.message = message

    def __str__(self):
        return "<HXException: " + str(self.message) + ">"
