from decorator import contextmanager


class Copy(object):
    """A generic copy command implementation"""

    def __init__(self, input, output, chunk_size=1024):
        self.__input = input
        self.__output = output
        self.__chunk_size = chunk_size

    def execute(self):
        with self.open_resources():
            while True:
                data = self.__input.read(self.__chunk_size)
                if not data:
                    break
                self.__output.write(data)

    @contextmanager
    def open_resources(self):
        self.__input.open()
        self.__output.open()
        yield
        self.__input.close()
        self.__output.close()