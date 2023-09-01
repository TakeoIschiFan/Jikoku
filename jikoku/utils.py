from datetime import time, date, timedelta, datetime


def add_times(a_time: time, a_time_delta: timedelta):
    """
    Adds a timedelta to a time, ignoring 24h rollover.
    """
    return (datetime.combine(date.today(), a_time) + a_time_delta).time()


def subtract_times(a_time: time, a_time_delta: timedelta):
    """
    Adds a timedelta to a time, ignoring 24h rollover.
    """
    return (datetime.combine(date.today(), a_time) - a_time_delta).time()


def compare_times(a_time: time, b_time: time) -> timedelta:
    """
    Compares two times, ignoring 24 rollover, i.e. 23h - 1h the next day will give a time difference of 22 hours!
    """
    return datetime.combine(date.today(), a_time) - datetime.combine(date.today(), b_time)

