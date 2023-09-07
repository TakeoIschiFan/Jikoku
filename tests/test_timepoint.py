from jikoku.time import DailyTimePoint


def test_add_two_daily_times():
    a = DailyTimePoint(hour=2)
    b = DailyTimePoint(hour=3, minute=4)
    c = a + b
    assert c._t == 304


def test_add_two_daily_times_date_boundary():
    a = DailyTimePoint(hour=2)
    b = DailyTimePoint(day=1, hour=3, minute=4)
    assert (a + b)._t > 24 * 60


def test_daily_time_str():
    # check left padding of early hours
    early = DailyTimePoint(hour=3, minute=4)
    assert str(early) == "03:04"

    # late hours should obey 24h clock
    late = DailyTimePoint(hour=23, minute=59)
    assert str(late) == "23:59"

    # Check tomorrow dates
    next_day = DailyTimePoint(hour=25, minute=59)
    assert str(next_day) == "Tomorrow at 01:59"

    next_day_2 = DailyTimePoint(day=1, hour=3, minute=59)
    assert str(next_day_2) == "Tomorrow at 03:59"

    # Check dates in the future
    far_day = DailyTimePoint(day=69, hour=4, minute=30)
    assert str(far_day) == "In 69 days at 04:30"

    # Check dates in the past
    yester_day = DailyTimePoint(day=-1, hour=23, minute=59)
    assert str(yester_day) == "Yesterday at 23:59"

    far_day = DailyTimePoint(day=-69, hour=4, minute=30)
    assert str(far_day) == "69 days ago at 04:30"





