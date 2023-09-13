from jikoku.models import Stop, Service
from datetime import time, timedelta

from jikoku.time import DailyTimePoint


def test_shift_stop():
    a_stop = Stop("test_stop", DailyTimePoint(hour=8))

    # shifting by 0 minutes should not modify the stop
    b_stop = a_stop + DailyTimePoint()
    assert a_stop == b_stop

    # adding and removing timedelta should not modify the stop
    delta = DailyTimePoint(hour=6, minute=9)
    c_stop = a_stop + delta - delta
    assert a_stop == c_stop


def test_stop_24h_rollover():
    a_stop = Stop("test_stop", DailyTimePoint(hour=23))
    delta = DailyTimePoint(hour=6, minute=9)

    assert not (a_stop + delta).stop_time.same_time(DailyTimePoint(hour=5, minute=9))
