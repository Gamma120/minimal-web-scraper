import pytest
import requests

import minimal_web_scraper as scraper


def test_download():
    url = "example.com"
    response, encoding = scraper.main.download(url)
    assert isinstance(response, bytes) and encoding == "UTF-8"


def test_exception_download():
    with pytest.raises(ValueError):
        url = ""
        scraper.main.download(url)
    with pytest.raises(requests.HTTPError):
        # Error HTTP 404
        url = "https://example.com/testest"
        scraper.main.download(url)
