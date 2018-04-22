"""
Http input module
"""


import urllib2

from download.inputs.exception import InvalidHttpInputAddress, HttpInputNotFound
from download.inputs.input import Input


class HttpInput(Input):
    """An implementation of http input resource"""

    def __init__(self, url):
        url = url.strip()
        if not any(url.lower().startswith(x) for x in ('http://', 'https://')):
            raise InvalidHttpInputAddress
        self.__url = url
        self.__response = None

    def open(self):
        try:
            self.__response = urllib2.urlopen(self.__url)
        except urllib2.HTTPError:
            raise HttpInputNotFound

    def close(self):
        self.__response.close()

    def read(self, size):
        return self.__response.read(size)