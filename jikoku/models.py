from dataclasses import dataclass
from datetime import time, timedelta

from jikoku.utils import add_times, subtract_times


@dataclass
class Stop:
    stop_name: str
    stop_time: time

    def __add__(self, other):
        if isinstance(other, timedelta):
            return Stop(self.stop_name, add_times(self.stop_time, other))
        else:
            raise NotImplementedError()

    def __iadd__(self, other):
        if isinstance(other, timedelta):
            self.stop_time = add_times(self.stop_time, other)
        else:
            raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, timedelta):
            return Stop(self.stop_name, subtract_times(self.stop_time, other))
        else:
            raise NotImplementedError()

    def __isub__(self, other):
        if isinstance(other, timedelta):
            self.stop_time = subtract_times(self.stop_time, other)
        else:
            raise NotImplementedError()


@dataclass
class Service:
    name: str
    # TODO: These times should be coupled via a getter to the first and last stop times...
    start_time: time
    end_time: time
    stops: list[Stop]

    def __add__(self, other):
        if isinstance(other, timedelta):
            new_name = self.name + "_shift_by_" + str(other)
            return Service(new_name, add_times(self.start_time, other), add_times(self.end_time, other),
                           [stop + other for stop in self.stops])
        else:
            raise NotImplementedError()

    def __iadd__(self, other):
        if isinstance(other, timedelta):
            self.start_time = add_times(self.start_time, other)
            self.end_time = add_times(self.end_time, other)
            self.stops = [stop + other for stop in self.stops]
        else:
            raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, timedelta):
            new_name = self.name + "_shift_by_minus" + str(other)
            return Service(new_name, subtract_times(self.start_time, other), subtract_times(self.end_time, other),
                           [stop + other for stop in self.stops])
        else:
            raise NotImplementedError()

    def __isub__(self, other):
        if isinstance(other, timedelta):
            self.start_time = subtract_times(self.start_time, other)
            self.end_time = subtract_times(self.end_time, other)
            self.stops = [stop + other for stop in self.stops]
        else:
            raise NotImplementedError()


@dataclass
class Train:
    # TODO this should be unique, any way to enforce?
    name: str


@dataclass
class Trip:
    service: Service
    train: Train


@dataclass
class Schedule:
    trips: list[Trip]

    @property
    def number_of_trains(self):
        return len({t.train.name for t in self.trips})
