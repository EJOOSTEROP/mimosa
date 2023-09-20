"""Various random snippets."""
from datetime import date, timedelta
from typing import Iterator


def daterange(start_date: date, end_date: date) -> Iterator[date]:
    """Generates a range of dates.

    Args:
        start_date (date): The start date of the range
        end_date (date): The end date of the range

    Yields:
        Iterator[date]: A generator that yields each date in the range

    >>> import datetime
    >>> start_date = datetime.datetime.strptime("2023-08-10", "%Y-%m-%d").astimezone()
    >>> end_date = datetime.datetime.strptime("2023-08-15", "%Y-%m-%d").astimezone()
    >>> print([dte.strftime("%Y-%m-%d") for dte in daterange(start_date, end_date)])
    ['2023-08-10', '2023-08-11', '2023-08-12', '2023-08-13', '2023-08-14']
    >>> print([dte.strftime("%Y-%m-%d") for dte in daterange(end_date, start_date)])
    ['2023-08-10', '2023-08-11', '2023-08-12', '2023-08-13', '2023-08-14']
    >>> print([dte.strftime("%Y-%m-%d") for dte in daterange(start_date, None)])
    ['2023-08-10']
    >>> print([dte.strftime("%Y-%m-%d") for dte in daterange(None, end_date)])
    ['2023-08-14']
    >>> print([dte.strftime("%Y-%m-%d") for dte in daterange(None, None)])
    []
    >>> print([dte.strftime("%Y-%m-%d") for dte in daterange(start_date, start_date)])
    []
    """
    if start_date is None and end_date is None:
        start_date = date(2023, 8, 10)
        end_date = start_date
    elif end_date is None:
        end_date = start_date + timedelta(days=1)
    elif start_date is None:
        start_date = end_date - timedelta(days=1)

    if start_date > end_date:  # reversed dates work. Is this desired?
        start_date, end_date = end_date, start_date

    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


class MissingEnvironmentVariableError(Exception):
    """Raised when a required environment variable is missing."""


if __name__ == "__main__":
    import doctest

    doctest.testmod()
