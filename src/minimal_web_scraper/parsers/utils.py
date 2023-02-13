from typing import Type

from .base import BaseParser
from .exceptions import ParserNotFound


def find_parser(url: str):
    """Find the parser for the associate url.
    The scope_url attribut of the parser is compared to the argument.

    Args:
        url (str):
    Raises:
        NotImplementedError: no parser is associated to the url
    Returns:
        associated parser
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

    Args:
        parser (Type[BaseParser] | None, optional): The parser must be a subclass of BaseParser.
        If no parser is provided, add_parser will add all parsers imported. Defaults to None.

    Raises:
        TypeError: raised when the argument parser is not a subclass of BaseParser
    """
    if parser:
        if not issubclass(parser, BaseParser) and parser is not BaseParser:
            raise TypeError(f"Argument is not a subclass of BaseParser: {repr(parser)}")
        _parsers.add(parser)
    else:
        for parser in _get_all_subclasses(BaseParser):
            # don't really understand why mypy considers that parser could be None
            _parsers.add(parser)  # type: ignore[arg-type]


def _get_all_subclasses(cls) -> list:
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(_get_all_subclasses(subclass))

    return all_subclasses


_parsers: set[Type[BaseParser]] = set()
