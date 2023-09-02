# Jikoku  
  
Flexible and extendable Python utility for generating working timetables from general schedule data.  
  
## Basic Usage Example

```python
from jikoku.models import Stop, Service
from jikoku.scheduler import schedule
from datetime import time, timedelta

# Define a simple service and return service
starts = time(hour=8)
ends = time(hour=9, minute=30)

first = Service("a_service", starts, ends, [Stop("Teufort", starts), Stop("Badlands",ends)])
first_return = Service( "a_return_service",starts , ends, [Stop("Badlands", starts), Stop("Teufort", ends)])

# Copy those services throughout the day
all_services = [first + timedelta(hours=i) for i in range(4)] + ([first_return + timedelta(hours=i) for i in range(4)])

# Schedule the services
generated_schedule = schedule(all_services)
print(generated_schedule)
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

See [the Documentation](/docs) for more examples, including real word schedules from JR & SNCF! 
  
## Installation  
  
Jikoku is not available on PyPI yet. For now, download the source code and build the package locally, preferable using [Poetry](https://github.com/python-poetry/poetry).

```bash
git clone https://github.com/TakeoIschiFan/Jikoku
cd Jikoku
poetry install
```
After which, a Jikoku package should be installed in the local Poetry virtual environment.