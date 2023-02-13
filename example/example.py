# example.py

import pandas as pd

import minimal_web_scraper as scraper
from minimal_web_scraper import parsers

# Import the parsers modules to add them to the scraper list of parsers
import parser_example

# add all parsers imported (which are subclass of BaseParser)
parsers.add_parser()

# or add them manually
# parsers.add_parser(parser_example.BookParser)
# parsers.add_parser(parser_example.BooksParser)

# Scrape the url in argument and return a dictionnary of parsed data
data = scraper.scrape("https://books.toscrape.com/")

# Pretty formatting with pandas
books = pd.DataFrame(data)
print(books.head(5))
