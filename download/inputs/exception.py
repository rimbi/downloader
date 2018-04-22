"""
A module for input exceptions
"""


class InputException(BaseException):
    pass


class InvalidHttpInputAddress(InputException):
    pass


class HttpInputNotFound(InputException):
    pass