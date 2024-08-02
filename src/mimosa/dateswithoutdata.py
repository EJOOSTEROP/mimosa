"""Functions to find a list of gas_day_start dates missing in the target schema.

tuples_of_missing_dates() is the main output of the module. The rest are helper functions.
"""

import datetime
import os
from datetime import date, timedelta  # F401

import duckdb
from dotenv import find_dotenv, load_dotenv

import mimosa.utilities as tern

DT_BASE = datetime.date(1900, 1, 1)

_ = load_dotenv(find_dotenv())


def date_to_integer(dt_time):
    """Convert a date to an integer representation.

    Args:
        dt_time (datetime): The input date and time.

    Returns:
        int: The integer representation of the input date.
    """
    return (dt_time - DT_BASE).days


def integer_to_date(integer_value):
    """Convert an integer value to a date.

    Parameters:
    integer_value (int): The integer value to be converted to a date.

    Returns:
    datetime.date: The date corresponding to the integer value.
    """
    return DT_BASE + timedelta(days=integer_value)


def get_existing_dates_as_integer(start_dt=date(2018, 1, 1), end_dt=None):
    """Retrieve a list of distinct gas day start dates from the landing schema.

    The dates are then converted to a list of integers which can be used to expediently
    find missing dates.

    Parameters:
    start_dt: First date for which data should be loaded
    end_dt: Last date for which data should be loaded

    Returns:
    Returns the list of integer interpretation of dates for which data exists,
    plus the day before start date and the day after end date.
    """
    if not end_dt:
        end_dt = datetime.datetime.now(tz=datetime.timezone.utc).date()

    # connect to MotherDuck, string slighly different than for dlt hence the replace
    conn_str = os.environ["DESTINATION__MOTHERDUCK__CREDENTIALS"].replace("/", "")
    con = duckdb.connect(conn_str)
    query = "select distinct gas_day_start from landing.storage where gas_day_start >= $start_date and gas_day_start <= $end_date order by 1 asc"
    result = con.execute(
        query,
        {
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "end_date": end_dt.strftime("%Y-%m-%d"),
        },
    ).fetchall()

    # convert results to list of integers. Only consider first column.
    dates_list = [
        date_to_integer(
            datetime.datetime.strptime(date[0], "%Y-%m-%d").astimezone().date()
        )
        for date in result
    ]

    if not dates_list:
        dates_list.extend([date_to_integer(start_dt) - 1, date_to_integer(end_dt) + 1])
    else:
        min_date, max_date = date_to_integer(start_dt), date_to_integer(end_dt)
        if dates_list[0] > min_date:
            dates_list.insert(0, min_date - 1)
        if dates_list[-1] < max_date:
            dates_list.append(max_date + 1)

    return dates_list


def get_missing_dates(existing_dates_as_integer):
    """Takes a list of existing dates as input and returns a list of missing dates.

    >>> print(get_missing_dates([1, 3]))
    [datetime.date(1900, 1, 3)]

    >>> print(get_missing_dates([1, 3, 4, 7]))
    [datetime.date(1900, 1, 3), datetime.date(1900, 1, 6), datetime.date(1900, 1, 7)]

    >>> print(get_missing_dates([1, 2, 3]))
    []

    >>> print(get_missing_dates([]))
    []

    """
    return [
        integer_to_date(row) for row in tern.missing_elements(existing_dates_as_integer)
    ]


def get_sequence_ranges(sequence):
    """Return a list of tuples with the first and last value of each sequence.

    Given a sequence of integers with gaps, return a list of tuples with
    the first and last value of each sequence. A fixed offset is added to the
    last value of each sequence.

    Parameters:
    sequence (List[int]): The sequence of integers with gaps.

    Returns:
    List[Tuple[int, int]]: The list of tuples containing the first and last value of each sequence.

    >>> print(get_sequence_ranges([]))
    []

    >>> print(get_sequence_ranges([2]))
    [(2, 3)]

    >>> print(get_sequence_ranges([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]

    >>> print(get_sequence_ranges([1, 2, 3, 5, 7, 8, 9, 11]))
    [(1, 4), (5, 6), (7, 10), (11, 12)]

    """
    ranges = []
    if len(sequence) > 0:
        offset = 1
        start = sequence[0]
        for i in sequence:
            prior = sequence[sequence.index(i) - 1]
            if i - prior > 1:
                ranges.append((start, sequence[sequence.index(i) - 1] + offset))
                start = i
                prior = start

        ranges.append((start, sequence[-1] + offset))
    return ranges


def convert_integer_tuples_to_date_tuples(integer_tuples):
    """Convert a list of integer tuples into a list of date tuples.

    Parameters:
    integer_tuples (List[Tuple[int, int]]): The list of integer tuples to be converted.

    Returns:
    List[Tuple[object, object]]: The list of data tuples containing the converted values.

    >>> print(convert_integer_tuples_to_date_tuples([(1, 3), (4, 7)]))
    [(datetime.date(1900, 1, 2), datetime.date(1900, 1, 4)), (datetime.date(1900, 1, 5), datetime.date(1900, 1, 8))]

    >>> print(convert_integer_tuples_to_date_tuples([]))
    []

    """
    return [(integer_to_date(x), integer_to_date(y)) for x, y in integer_tuples]


def tuples_of_missing_dates(start_dt=date(2018, 1, 1), end_dt=None):
    """Generates tuples of missing dates.

    This function generates tuples of missing dates based on existing dates in
    the database (represented as integers).

    It returns the missing dates as a list of date tuples, containing the start and end dates
    for all missing date sequences.
    """
    missing_integers = [
        date_to_integer(date)
        for date in get_missing_dates(
            get_existing_dates_as_integer(start_dt=start_dt, end_dt=end_dt)
        )
    ]
    return convert_integer_tuples_to_date_tuples(get_sequence_ranges(missing_integers))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
