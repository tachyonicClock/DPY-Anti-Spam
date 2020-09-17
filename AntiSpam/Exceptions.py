"""
A file devoted to some nice custom exceptions of mine
"""


class DuplicateMessage(Exception):
    """Raised because you attempted to create a message object, using the exact same id's."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = self.__doc__

    def __str__(self):
        return self.message


class ObjectMismatch(Exception):
    """Raised because you attempted add a message to a user, but that user didn't create that message."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = self.__doc__

    def __str__(self):
        return self.message