from bs4 import BeautifulSoup
import logging

# https://www.jreast-timetable.jp/2309/timetable-v/624d1.html

Log = logging.getLogger(__name__)


def parse(path):
    with open(path) as file:
        soup = BeautifulSoup(file, "html.parser")
        table = soup.find(class_="paper_table")
        Log.info(table)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parse("pages/keiyoline_fromsoga.html")
