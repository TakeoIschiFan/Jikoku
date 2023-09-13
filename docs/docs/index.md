# Quickstart

## Installation
Jikoku is available on PyPI. Install via using (preferably in a virtual environment) via:
```bash
pip install jikoku
```

## First Jikoku Schedule

To test if the installation works, we're going to make a very simple service pattern for Jikoku to schedule.

Create a file called `my_schedule.py`.

Let's now define a simple service. In Jikoku, a service is simply a list of consecutive stops that a train calls at.
Here we model a city-pair connection between two cities as pictured below:

```mermaid
flowchart LR
    A[Teufort] --> B[Badlands]
    B[Badlands]--> A[Teufort]
```

```python
from jikoku.time import DailyTimePoint
from jikoku.models import Service, Stop
from jikoku.scheduler import schedule

# Define a start and arrival time for the first train of the day
starts = DailyTimePoint(hour=8)
ends = DailyTimePoint(hour=9, minute=30)

# Define a first service and its return service
first = Service("a_service", [Stop("Teufort", starts), Stop("Badlands", ends)])
first_return = Service("a_service", [Stop("Badlands", starts), Stop("Teufort", ends)])

# Repeat those services throughout the day
all_services = [first + DailyTimePoint(hour=i) for i in range(3)] + ([first_return + DailyTimePoint(hour=i) for i in range(3)] )

print(schedule(all_services))
"""prints the following:
train-ZT4bwn
        09:00:00 - 10:30:00: Teufort => Badlands
        11:00:00 - 12:30:00: Badlands => Teufort
train-eP9nMb
        08:00:00 - 09:30:00: Badlands => Teufort
        10:00:00 - 11:30:00: Teufort => Badlands
train-hVGMEI
        08:00:00 - 09:30:00: Teufort => Badlands
        10:00:00 - 11:30:00: Badlands => Teufort
train-jzVbxj
        09:00:00 - 10:30:00: Badlands => Teufort
        11:00:00 - 12:30:00: Teufort => Badlands
"""
```
 
## Next steps

You might want to look at a real word example [here](/todo),
or delve into more advanced concepts such as:

- [How to configure the scheduler]()
- [the API reference](/API reference)