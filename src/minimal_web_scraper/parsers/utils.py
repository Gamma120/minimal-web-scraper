from typing import Type, Any
from urllib.parse import urlparse
import re

from .base import BaseParser


def find_parser(url: str) -> Type[BaseParser] | None:
    """Find the parser for the associate URL.

    The scope_urls attribute of the parser is compared to the argument.

    :param url:
    :raise ParserNotFound: raised when no registered parser can handle `url`
    :returns: associated parser
    """
    url_parsed = urlparse(url)

    for parser in _parsers:
        for scope_url in parser.scope_urls:
            scope_parsed = urlparse(scope_url)
            if url_parsed.netloc == scope_parsed.netloc:
                pattern = _pattern(scope_parsed.path)
                if re.fullmatch(pattern, url_parsed.path):
                    return parser

    return None


def _pattern(path: str) -> str:
    # based on https://www.rfc-editor.org/rfc/rfc3986#section-2.3
    pattern = r"[\w|\-|.|_|~]*"
    path_splited = re.split("{" + pattern + "}", path)
    full_pattern: str = ""
    for i in range(len(path_splited) - 1):
        full_pattern += path_splited[i] + pattern
    full_pattern += path_splited[-1]
    return full_pattern


def add_parser(parser: Type[BaseParser] | None = None) -> None:
    """Add the given parser in the list that the scraper checks for parsing data.

    :param parser: the parser must be a subclass of BaseParser.
        If no parser is provided, it will add all parsers imported (default None).
    :raise TypeError: raised when the argument parser is not a subclass of :class:`BaseParser`
    """
    if parser:
        if not issubclass(parser, BaseParser) and parser is not BaseParser:
            raise TypeError(f"Argument is not a subclass of BaseParser: {repr(parser)}")
        _parsers.add(parser)
    else:
        for sub_parser in _get_all_subclasses(BaseParser):
            _parsers.add(sub_parser)


def _get_all_subclasses(cls: Any) -> list[Any]:
    """Find all subclasses of `cls`"""
    all_subclasses: list[Any] = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(_get_all_subclasses(subclass))

    return all_subclasses


_parsers: set[Type[BaseParser]] = set()
