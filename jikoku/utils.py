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
