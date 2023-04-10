"""Subpackage of minimal_web_scraper. Provide the API to build parsers and manage them."""

from .utils import add_parser as add_parser
from .base import BaseParser as BaseParser
from .exceptions import ParserNotFound as ParserNotFound
