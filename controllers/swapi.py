from functools import cache

import pandas as pd
import requests

from config import CSV_PATH, EXTERNAL_SERVICE_URL, SWAPI_PEOPLE_URL


def fetch_characters():
    """Fetch all characters from SWAPI and make some preprocessing

    preprocessing:
    - sort by number of films DESC
    - return first 10 characters
    """

    next_url = SWAPI_PEOPLE_URL
    char_table = pd.DataFrame()

    # downside of this approach is that we are fetching all data from SWAPI and loading it into memory
    # that's why in each step I'm trying to reduce the amount of data to only required columns in the output
    while next_url:
        resp = requests.get(next_url).json()
        next_url = resp.get("next", None)
        tmp_char_table = pd.DataFrame.from_dict(resp.get("results", {}))
        tmp_char_table = tmp_char_table[["name", "species", "height", "films"]]
        tmp_char_table["species"] = tmp_char_table["species"].apply(_fetch_species)
        tmp_char_table["appearance"] = tmp_char_table["films"].apply(len)
        tmp_char_table["height"] = tmp_char_table["height"].apply(_maybe_convert_to_int)
        tmp_char_table = tmp_char_table[["name", "species", "height", "appearance"]]
        char_table = pd.concat([char_table, tmp_char_table])
    # remove characters that have unknown height
    char_table.dropna(subset=["height"], inplace=True)
    char_table = char_table.sort_values(
        by=["appearance", "height"], ascending=False
    ).head(10)
    char_table = char_table.sort_values(by=["height"], ascending=False)

    # create `media` dir if not exists
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    char_table.head(10).to_csv(CSV_PATH, index=False)
    send_to_external(char_table)


def send_to_external(char_table: pd.DataFrame):
    try:
        requests.post(
            EXTERNAL_SERVICE_URL,
            data=char_table.to_csv(),
            headers={"Content-Type": "text/csv"},
        )
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


@cache
def _maybe_convert_to_int(s: str) -> int | None:
    """Convert string to int if possible"""
    try:
        return int(s)
    except ValueError:
        return None


def _fetch_species(species_urls: list[str]) -> str:
    """Fetch species from SWAPI and return list of names"""
    for s_url in species_urls:
        return _fetch_specie(s_url)


@cache
def _fetch_specie(specie_url: str) -> str:
    """Fetch single specie from SWAPI

    NOTE: this resource is cached to not make same requests multiple times
    """
    return requests.get(specie_url).json().get("name", "")
