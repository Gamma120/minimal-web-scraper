class BaseParserException(Exception):
    """Common, base class for all non-exit parsers exception."""

    pass


class ParserNotFound(BaseParserException):
    """Exception raised when the scraper does not find a parser associated to an URL."""

    pass
