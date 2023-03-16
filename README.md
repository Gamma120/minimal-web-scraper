# Minimal-Web-Scraper


A minimal library to scrape web pages. The user must implement its own parsers using libraries like [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/).

Here, you can find an overview of the library. For more details, read the [documentation](https://minimal-web-scraper.readthedocs.io/en/latest/index.html).

This project is in development state, and the **author doesn’t guarantee the stability of its API**.

This is a personal project without any other ambition that to learn how to develop a Python library.


## Installation

```bash
pip install git+https://github.com/Gamma120/minimal-web-scraper.git
```

### Dependencies

This library depends on:

- Python 3.10 or newer
- request


## Overview

The target this website aimed to practice scraping: https://books.toscrape.com/.

Here is a small script for demonstration. You can find it here: [example.py](example/example.py) and [parser_example.py](example/parser_example.py).

```python
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
```

Output:

```
                                        name  price
    0                   A Light in the Attic  51.77
    1                     Tipping the Velvet  53.74
    2                             Soumission  50.10
    3                          Sharp Objects  47.82
    4  Sapiens: A Brief History of Humankind  54.23
```


## Links

- Documentation: [Readthedocs](https://minimal-web-scraper.readthedocs.io/en/latest/index.html)
- Contact: [gamma_120@simplelogin.com](mailto:gamma_120+github@simplelogin.com)
