import pytest

from minimal_web_scraper import parsers
from minimal_web_scraper.parsers import exceptions, base


@pytest.fixture
def set_parsers():
    parsers.add_parser(ParserTest)
    parsers.add_parser(ParserTestList)


# need to clean the parser list for test isolation
@pytest.fixture(autouse=True)
def del_parsers():
    parsers.utils._parsers.clear()


def test_find_parser(set_parsers):
    url = "test.com"
    parser = parsers.find_parser(url)
    assert parser is ParserTest

    url = "test.com/list"
    parser = parsers.find_parser(url)
    assert parser is ParserTestList


def test_exception_find_parser(set_parsers):
    url = "example.com"
    with pytest.raises(exceptions.ParserNotFound):
        parsers.find_parser(url)


def test_add_parser():
    parsers.add_parser(ParserTest)
    assert len(parsers.utils._parsers) == 1
    assert parsers.utils._parsers.pop() is ParserTest


def test_add_imported_parser():
    desirable_result = {ParserTest, ParserTestList}
    parsers.add_parser()
    assert len(parsers.utils._parsers) == 2
    assert parsers.utils._parsers == desirable_result


def test_exception_add_parser():
    with pytest.raises(TypeError):
        parsers.add_parser(1)
    with pytest.raises(TypeError):
        parsers.add_parser(NotAParser)


class ParserTest(base.BaseParser):
    scope_url = "test.com"

    @classmethod
    def parse(cls, html_content, encoding):
        pass


class ParserTestList(ParserTest):
    scope_url = "test.com/list"


class NotAParser:
    pass
