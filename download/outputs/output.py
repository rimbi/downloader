"""
A generic output interface
"""


class Output(object):
    """A generic output interface"""

    def open(self):
        raise Exception('Not implemented')

    def close(self):
        raise Exception('Not implemented')

    def write(self, data):
        raise Exception('Not implemented')
