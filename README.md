# Ask Academic Date

[
![PyPI](https://img.shields.io/pypi/v/ask_schools.svg)
![PyPI](https://img.shields.io/pypi/pyversions/ask_schools.svg)
![PyPI](https://img.shields.io/github/license/guinslym/ask_schools.svg)
](https://pypi.org/project/ask_schools/)
[![TravisCI](https://travis-ci.org/guinslym/ask_schools.svg?branch=master)](https://travis-ci.org/guinslym/ask_schools)


This package helps convert Ask School suffixes to the school full name.


## Installation

**Ask Academic Date** can be installed from PyPI using `pip` or your package manager of choice:

```
pip install ask_academic_dates
# or
poetry add ask_academic_dates
```


## Usage


Example:

```python

from ask_academic_dates import find_academic_year
from datetime import date

def check_find_academic_year():
  given_date = date(2019,5,3)
  result = find_academic_year(given_date)
  assert result == '2018-2019'
```

## Code of Conduct

Everyone interacting in the project's codebases, issue trackers, chat rooms, and mailing lists is expected to follow the [PyPA Code of Conduct](https://www.pypa.io/en/latest/code-of-conduct/).

### Todo
1.  Test
2.  Refactor
3.  Add docstring
4.  Add a Makefile
5.  Add show terminal graph for a given month
6.  Create a .rst file and add metadata for 
