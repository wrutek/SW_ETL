from pathlib import Path
from urllib.parse import urljoin

SWAPI_URL = "https://swapi.dev/api/"
SWAPI_PEOPLE_URL = urljoin(SWAPI_URL, "people")

CSV_DIR = Path(__file__).parent.resolve().joinpath("media")
CSV_NAME = "swapi_people.csv"
CSV_PATH = Path.joinpath(CSV_DIR, CSV_NAME)

EXTERNAL_SERVICE_URL = "http://httpbin.org/post"
