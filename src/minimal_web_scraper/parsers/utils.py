from typing import Type, Any

from .base import BaseParser
from .exceptions import ParserNotFound


def find_parser(url: str) -> Type[BaseParser]:
    """Find the parser for the associate URL.

    The scope_url attribute of the parser is compared to the argument.

    :param url:
    :raise ParserNotFound: raised when no registered parser can handle `url`
    :returns: associated parser
    """
    selected_parser = None
    most_index = 0
    for parser in _parsers:
        index = url.find(parser.scope_url)
        tmp_index = index + len(parser.scope_url)
        if index != -1 and tmp_index > most_index:
            most_index = tmp_index
            selected_parser = parser

    if not selected_parser:
        raise ParserNotFound(f"No parser found for the URL: {url}")

    return selected_parser


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
