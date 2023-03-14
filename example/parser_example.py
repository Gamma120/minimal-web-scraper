# parser_example.py

from bs4 import BeautifulSoup
import re

from minimal_web_scraper.parsers import BaseParser


class BooksParser(BaseParser):
    base_url = "https://books.toscrape.com/"

    scope_url = "books.toscrape.com"

    @classmethod
    def parse(cls, html_content: bytes, encoding: str | None) -> list[dict]:
        scraped_items = []
        soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
        books = soup.find_all("article", class_="product_pod")

        for book in books:
            item = {
                "name": None,
                "url": None,
                "availability": None,
                "img_url": None,
                "price": None,
            }

            item["name"] = book.h3.a["title"]
            item["url"] = cls.base_url + book.h3.a["href"]
            item["availability"] = book.find("p", class_="availability").get_text()
            item["img_url"] = cls.base_url + book.img["src"]
            item["price"] = book.find("p", class_="price_color").get_text()

            if item["price"]:
                item["price"] = float(item["price"][2:])
            if item["availability"]:
                matched = re.search("(In stock|Out of stock)", item["availability"])
                item["availability"] = matched[0]

            scraped_items.append(item)

        return scraped_items


class BookParser(BaseParser):
    base_url = "https://books.toscrape.com/"

    scope_url = "books.toscrape.com/catalogue/"

    @classmethod
    def parse(cls, html_content: bytes, encoding: str | None) -> list[dict]:
        soup = BeautifulSoup(html_content, "html.parser", from_encoding=encoding)
        book = soup.find("article", class_="product_page")

        item = {
            "name": None,
            "url": None,
            "availability": None,
            "img_url": None,
            "price": None,
        }

        item["name"] = book.img["alt"]
        item["availability"] = book.find("p", class_="availability").get_text()
        item["img_url"] = cls.base_url + book.img["src"]
        item["price"] = book.find("p", class_="price_color").get_text()

        if item["price"]:
            item["price"] = float(item["price"][2:])
        if item["availability"]:
            matched = re.search("(In stock|Out of stock)", item["availability"])
            item["availability"] = matched[0]

        return [item]
