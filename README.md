Minimal-Web-Scraper
===================

A minimal library to scrape web pages. The user must implement its own parsers using libraries like [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/).

Here, you can find an overview of the library. For more details, see the [documentation]().

Installation
------------

```bash
pip install git+https://github.com/Gamma120/minimal-web-scraper.git
```

A Simple Example
--------------

 Script [example.py](example/example.py) using parsers from [parser_example.py](example/parser_example.py)

```python
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
```

Links
-----

- Documentation:
- Contact: [gamma_120@simplelogin.com](mailto:gamma_120+github@simplelogin.com)




