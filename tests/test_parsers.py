import pytest

from minimal_web_scraper import parsers


@pytest.fixture
def set_parsers():
    parsers.utils.add_parser(BooksParser)
    parsers.utils.add_parser(BookParser)


# need to clean the parser list for test isolation
@pytest.fixture(autouse=True)
def del_parsers():
    parsers.utils._parsers.clear()


def test_find_parser(set_parsers):
    url = "https://books.toscrape.com/"
    parser = parsers.utils.find_parser(url)
    assert parser is BooksParser

    url = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    parser = parsers.utils.find_parser(url)
    assert parser is BooksParser

    url = "https://books.toscrape.com/catalogue/the-last-mile-amos-decker-2_754/index.html"
    parser = parsers.utils.find_parser(url)
    assert parser is BookParser

    url = "https://example.com"
    parser = parsers.utils.find_parser(url)

    assert parser is None


def test_pattern():
    pattern = r"[\w|\-|.|_|~]*"

    path = "/a/b/c.html"
    assert parsers.utils._pattern(path) == path

    path = "/a/{example}/b.html"
    assert parsers.utils._pattern(path) == f"/a/{pattern}/b.html"

    path = "/a/{e-._~}/{example-1}/b/{example-2}.html"
    assert parsers.utils._pattern(path) == f"/a/{pattern}/{pattern}/b/{pattern}.html"


def test_add_parser():
    parsers.utils.add_parser(BooksParser)
    assert len(parsers.utils._parsers) == 1
    assert parsers.utils._parsers.pop() is BooksParser


def test_add_imported_parser():
    desirable_result = {BooksParser, BookParser}
    parsers.utils.add_parser()
    assert len(parsers.utils._parsers) == 2
    assert parsers.utils._parsers == desirable_result


def test_exception_add_parser():
    with pytest.raises(TypeError):
        parsers.utils.add_parser(1)
    with pytest.raises(TypeError):
        parsers.utils.add_parser(NotAParser)


class BooksParser(parsers.base.BaseParser):
    scope_urls = [
        "https://books.toscrape.com/",
        "https://books.toscrape.com/catalogue/category/book_1/index.html",
        "https://books.toscrape.com/catalogue/category/books/{category-name}/index.html",
    ]

    @classmethod
    def parse(cls, html_content, encoding):
        pass


class BookParser(BooksParser):
    scope_urls = ["https://books.toscrape.com/catalogue/{book-name}/index.html"]


class NotAParser:
    pass
