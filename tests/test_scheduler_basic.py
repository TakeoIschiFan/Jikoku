import pytest

from jikoku import scheduler
from jikoku.models import *
from datetime import time, timedelta

from jikoku.time import DailyTimePoint


def get_basic_schedule():
    starts = DailyTimePoint(hour=8)
    ends = DailyTimePoint(hour=9, minute=30)

    first = Service("a_service", [Stop("Teufort", starts), Stop("Badlands", ends)])
    first_return = Service(
        "a_service", [Stop("Badlands", starts), Stop("Teufort", ends)]
    )

    return [first + DailyTimePoint(hour=i) for i in range(13)] + (
        [first_return + DailyTimePoint(hour=i) for i in range(13)]
    )


@pytest.fixture
def basic() -> list[Service]:
    """Provide a basic schedule for a 1.5 hour route from an A (Teufort) to B (Badlans) station which runs hourly
    from 8-20h in both directions.
    """
    return get_basic_schedule()


def test_basic_schedule(basic):
    # with a default config, the basic schedule should require 4 trains
    schedule = scheduler.schedule(basic)
    assert schedule.number_of_trains == 4


def test_basic_schedule_custom_minimum_time_between_services(basic):
    # forcing a 35-minute wait for trains in the basic schedule should require 6 trains
    schedule = scheduler.schedule(basic, minimum_minutes_between_services=35)
    assert schedule.number_of_trains == 6
