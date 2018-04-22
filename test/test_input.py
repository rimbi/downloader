import pytest

from download.inputs.exception import InvalidHttpInputAddress, HttpInputNotFound
from download.inputs.http_input import HttpInput


def test_accepts_http_input():
    HttpInput('http://www.veneta-travel.com/uploads/hotels/hotel_1157/hotel_573341_stambolli2017.jpg')


def test_accepts_https_input():
    HttpInput('https://www.veneta-travel.com/uploads/hotels/hotel_1157/hotel_573341_stambolli2017.jpg')


def test_throws_not_found():
    with pytest.raises(HttpInputNotFound):
        HttpInput('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.pn').open()


def test_only_accepts_http_or_https_address():
    with pytest.raises(InvalidHttpInputAddress):
        HttpInput('ftp://www.veneta-travel.com/uploads/hotels/hotel_1157/hotel_573341_stambolli2017.jpg')


def test_only_accepts_http_or_https_address():
    with pytest.raises(InvalidHttpInputAddress):
        HttpInput('ftp://www.veneta-travel.com/uploads/hotels/hotel_1157/hotel_573341_stambolli2017.jpg')
