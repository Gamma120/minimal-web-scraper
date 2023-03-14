# example.py

import pandas as pd

import minimal_web_scraper as scraper
from minimal_web_scraper import parsers

# import the parsers modules to add them to the scraper list of parsers
import parser_example

# add all parsers imported (which are subclass of BaseParser)
parsers.add_parser()

# or add them manually
# parsers.add_parser(parser_example.BookParser)
# parsers.add_parser(parser_example.BooksParser)

# scrape the URL in argument and return a dictionary of parsed data
data = scraper.scrape("https://books.toscrape.com/")

# Pretty output formatting with pandas
books = pd.DataFrame(data=data, columns=["name", "price"])
print(books.head(5))
