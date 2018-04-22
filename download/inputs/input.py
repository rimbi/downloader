"""
A generic input interface
"""


class Input(object):
    """A generic input interface"""

    def open(self):
        raise Exception('Not implemented')

    def close(self):
        raise Exception('Not implemented')

    def read(self, size):
        raise Exception('Not implemented')
