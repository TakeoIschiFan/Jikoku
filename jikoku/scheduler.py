from jikoku.models import *
from jikoku.utils import *
from datetime import time, timedelta
from pprint import pprint
import jikoku.config as config
from dataclasses import dataclass


@dataclass
class TrainData:
    train: Train
    busy_until: time

    def available(self, at_time: time) -> bool:
        return compare_times(at_time, self.busy_until) >= timedelta()


def schedule(services: list[Service], **kwargs) -> Schedule:
    conf = config.Config()
    for kword, value in kwargs.items():
        if kword in conf.__dict__:
            conf.__dict__[kword] = value
        else:
            print(f"unknown config item {kword}, skipping")

    print(f"using config {config}")

    services.sort(key=lambda s: s.start_time)

    trains: list[TrainData] = list()
    trips = list()

    for service in services:
        current_time = service.start_time

        available_trains = [t for t in trains if t.available(current_time)]

        if not available_trains:
            print("No train available, making a new one")
            t = TrainData(
                Train(f"a new train for {service}"),
                add_times(service.end_time, timedelta(minutes=conf.minimum_minutes_between_services))
            )
            trains.append(t)
            using_train = t
        else:
            using_train = available_trains[0]

        using_train.busy_until = add_times(service.end_time, timedelta(minutes=conf.minimum_minutes_between_services))
        trips.append(Trip(service, using_train.train))

    return Schedule(trips)
