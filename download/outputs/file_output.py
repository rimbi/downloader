"""
File output module
"""

from download.outputs.output import Output


class FileOutput(Output):
    """An implementation of file output resource"""

    def __init__(self, path):
        self.__path = path
        self.__f = None

    def open(self):
        self.__f = open(self.__path, 'wb')

    def close(self):
        self.__f.close()

    def write(self, data):
        self.__f.write(data)