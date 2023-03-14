from abc import ABCMeta, abstractmethod


class BaseParser(metaclass=ABCMeta):
    scope_url: str

    @classmethod
    def __repr__(cls) -> str:
        return f"{cls.__class__.__name__}"

    @classmethod
    def __str__(cls) -> str:
        return f"{cls.__class__.__name__} {cls.scope_url}"

    @classmethod
    @abstractmethod
    def parse(cls, html_content: bytes, encoding: str | None) -> list[dict]:
        pass
