"""Various random snippets."""

from datetime import date, timedelta
from typing import Iterator, Optional


def daterange(
    start_date: Optional[date] = None, end_date: Optional[date] = None
) -> Iterator[date]:
    """Generates an iterator of dates in a range of dates.

    Args:
        start_date (date): The start date of the range
        end_date (date): The end date of the range

    Yields:
        Iterator[date]: A generator that yields each date in the range

    >>> import datetime
    >>> start_date = datetime.datetime.strptime("2023-08-10", "%Y-%m-%d").astimezone()
    >>> end_date = datetime.datetime.strptime("2023-08-15", "%Y-%m-%d").astimezone()

    >>> for dte in daterange(start_date, end_date):
    ...     print(dte.strftime("%Y-%m-%d"))
    2023-08-10
    2023-08-11
    2023-08-12
    2023-08-13
    2023-08-14

    >>> for dte in daterange(end_date, start_date):
    ...     print(dte.strftime("%Y-%m-%d"))
    2023-08-10
    2023-08-11
    2023-08-12
    2023-08-13
    2023-08-14

    >>> for dte in daterange(start_date):
    ...     print(dte.strftime("%Y-%m-%d"))
    2023-08-10

    >>> for dte in daterange(end_date = end_date):
    ...     print(dte.strftime("%Y-%m-%d"))
    2023-08-14

    >>> for dte in daterange():
    ...     print(dte.strftime("%Y-%m-%d"))

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

    if start_date > end_date:  # reversed dates are accepted. Is this desired?
        start_date, end_date = end_date, start_date

    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def chunker(seq: list, size: int) -> Iterator[list]:
    """Generate an iterator that yields chunks of the sequence with the specified size.

    Args:
        seq (list): The sequence to be chunked.
        size (int): The size of each chunk.

    Yields:
        Iterator[list]: A generator that yields lists of size `size` from `seq`.

    >>> for chunk in chunker([1, 2, 3, 4, 5], 2):
    ...     print(chunk)
    [1, 2]
    [3, 4]
    [5]
    """
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def missing_elements(li):
    """Find all missing values in sequence of integers.

    Given a list li, this function finds the missing elements in the range
    from the first to the last element of the list and returns
    them as a sorted list.

    >>> print(missing_elements([1, 2, 3, 5, 7, 8, 9, 11]))
    [4, 6, 10]

    >>> print(missing_elements([1]))
    []

    >>> print(missing_elements([]))
    []
    """
    if not li:
        li = [1]
    start, end = li[0], li[-1]
    return sorted(set(range(start, end + 1)).difference(li))


class MissingEnvironmentVariableError(Exception):
    """Raised when a required environment variable is missing."""


if __name__ == "__main__":
    import doctest

    doctest.testmod()
