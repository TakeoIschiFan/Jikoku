from jikoku.models import Stop, Service
from datetime import time, timedelta


def test_shift_stop():
    a_stop = Stop("test_stop", time(hour=8))

    # shifting by 0 minutes should not modify the stop
    b_stop = a_stop + timedelta()
    assert a_stop == b_stop

    # adding and removing timedelta should not modify the stop
    delta = timedelta(hours=6, minutes=9)
    c_stop = a_stop + delta - delta
    assert a_stop == c_stop


def test_stop_24h_rollover():
    a_stop = Stop("test_stop", time(hour=23))
    delta = timedelta(hours=6, minutes=9)

    assert (a_stop + delta).stop_time == time(hour=5, minute=9)
