import logging
from itertools import zip_longest

from bs4 import BeautifulSoup, Tag, PageElement
from datetime import time

from jikoku.models import *
from jikoku.scheduler import schedule
from jikoku.visuals import pretty_print_schedule

Log = logging.getLogger(__name__)


def parse(path: str) -> list[Service]:
    with open(path) as file:
        services = list()
        Log.debug(f"Started parsing file {path}")

        soup = BeautifulSoup(file, "html.parser")
        table = soup.find(class_="paper_table")

        def cleanup_row(row) -> list:
            cols = list()
            for el in row:
                if el == "\n":
                    continue
                if isinstance(el, Tag):
                    if el.name != "td":
                        continue

                    cols.append(el.get_text(strip=True))

            return cols

        def to_time(four_string: str) -> time:
            return time(hour=int(four_string[:2]), minute=int(four_string[2:]))

        service_name_row = cleanup_row(table.find("tr", class_="tableTr_trainNumber"))
        service_type_row = cleanup_row(table.find("tr", class_="tableTr_trainName"))
        raw_station_rows = [row for row in table.find_all("tr") if not row.has_attr("class")]
        # extract the name out of the th tag before cleaning up the station rows
        station_names = [r.find("th").text for r in raw_station_rows]
        station_rows = [cleanup_row(r) for r in raw_station_rows]

        if t := table.find("tr", class_="tableTr_previous"):
            through_service_row = cleanup_row(t)
        elif t := table.find("tr", class_="tableTr_next"):
            through_service_row = cleanup_row(t)
        else:
            through_service_row = list()

        for i, (service_name, service_type, through_service) in enumerate(
                zip_longest(service_name_row, service_type_row, through_service_row)):
            Log.debug(f"Parsing service {service_name}")
            if service_type != "普通":
                Log.debug("skipping because it is not a 普通 service.")
                continue

            if through_service:
                Log.debug(f"skipping because it has through to {through_service}.")
                continue

            def get_stops_or_fail(names, rows):

                stops = list()
                for station_name, station_row in zip(names, rows):
                    Log.debug(f"trying station {station_name}")
                    content = station_row[i]
                    match content:
                        case "":
                            continue
                        case "||":
                            continue
                        case "レ":
                            return "Train stop had a レ in the table, which indicates rapid service"
                        case "・":
                            return "Train stop had a ・ in the table, which indicates through service"
                        case "＝":
                            return stops
                        case _:
                            Log.debug(f"found station {station_name} calling at {content}")
                            time = to_time(content)
                            stops.append(Stop(station_name, time))

                return stops

            stops = get_stops_or_fail(station_names, station_rows)
            if isinstance(stops, str):
                Log.debug(stops)
                return

            services.append(Service.from_stops(f"{service_name}-from-{path}", stops))
    return services


if __name__ == "__main__":
    loglevel = logging.DEBUG
    logging.basicConfig(
        level=loglevel,
        format="%(asctime)s - %(levelname)s@%(module)s:%(lineno)d - %(message)s",
        datefmt="[%H:%M:%S]",
    )

    services = parse("pages/keiyoline_from_soga.html") + parse("pages/keiyoline_from_tokyo.html")
    Log.debug(services)
    s = schedule(services)
    Log.debug(pretty_print_schedule(s))
