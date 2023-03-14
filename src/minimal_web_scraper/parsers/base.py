from abc import ABCMeta, abstractmethod


class BaseParser(metaclass=ABCMeta):
    """Base class for creating custom parsers.

    Subclasses must override :meth:`parse` and :attr:`scope_url`.
    Parsers are not intended to be instantiated.
    """

    scope_url: str
    """Define which URLs the parser is intended to parse."""

    @classmethod
    def __repr__(cls) -> str:
        return f"{cls.__class__.__name__}"

    @classmethod
    def __str__(cls) -> str:
        return f"{cls.__class__.__name__} {cls.scope_url}"

    @classmethod
    @abstractmethod
    def parse(cls, html_content: bytes, encoding: str | None) -> list[dict]:
        """Abstract method to parse HTML chunks.

        :param html_content: the raw HTML to parse
        :param encoding: the associated encoding of the HTML
        :returns: Should return a list of dictionnaries of the extracted elements
        """
        pass
