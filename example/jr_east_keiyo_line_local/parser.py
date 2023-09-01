import logging

from bs4 import BeautifulSoup

from jikoku.models import *

Log = logging.getLogger(__name__)


def parse(path: str) -> list[Service]:
    with open(path) as file:

        soup = BeautifulSoup(file, "html.parser")
        table = soup.find(class_="paper_table")

        service_name_row = table.find("tr")
        service_count = len(service_name_row.find_all("td"))

        for i in range(service_count):
            service_name = service_name_row.find_all("td")[]



if __name__ == "__main__":
    loglevel = logging.DEBUG
    logging.basicConfig(
        level=loglevel,
        format="%(asctime)s - %(levelname)s@%(module)s:%(lineno)d - %(message)s",
        datefmt="[%H:%M:%S]",
    )

    parse("pages/keiyoline_from_tokyo.html")