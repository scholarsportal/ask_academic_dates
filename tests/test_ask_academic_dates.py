from ask_academic_dates import __version__
from ask_academic_dates import find_academic_year
from datetime import date

def test_version():
    assert __version__ == '0.1.0'

def test_check_find_academic_year():
    given_date = date(2019,5,3)
    result = find_academic_year(date(2019,5,3))
    assert result == '2018-2019'