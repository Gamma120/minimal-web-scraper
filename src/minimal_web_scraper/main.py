import re
from urllib.parse import urlparse

import requests

from .parsers.utils import find_parser

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) \
        Gecko/20100101 Firefox/108.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,\
        image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",  # br is not supported by requests
    "Accept-Language": "en,fr;q=0.8,fr-FR;q=0.5,en-US;q=0.3",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-GPC": "1",
}


def download(target_url: str, timeout: int = 1) -> tuple[bytes, str | None]:
    """
    Download the html content of the url, using requests library.

    Use a custom header.

    :param target_url: url to download
    :type target_url: str
    :raise ValueError: if the target_url is not a valid url
    :raise: may raise exceptions from the requests and urlparse library
    :return: content of the html page and the encoding
    """
    # add scheme if not provided
    if not re.match(r"^https?://", target_url):
        target_url = "https://" + target_url

    url = urlparse(target_url)
    scheme = url.scheme
    host = url.hostname
    if not (scheme and host):
        raise ValueError(f"Invalid url: {target_url}")

    referer = scheme + "://" + host
    headers.update({"Host": host, "Referer": referer})
    response = requests.get(target_url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.content, response.encoding


def scrape(url: str) -> list[dict]:
    """
    Orchestrate the download and parse of the ressource at the url.

    :param url: url to parse
    :return: a list of dictionnaries which contain extracted informations by
        a implemented subclass of :meth:`parsers.BaseParser.parse`
    """
    parser = find_parser(url)
    content, encoding = download(url)
    scraped_content = parser.parse(content, encoding)
    return scraped_content
