from io import StringIO

import pandas as pd
import pytest

from controllers.swapi import fetch_characters


def test_fetch_characters(swapi_people, httpbin_mock):
    fetch_characters()
    assert (
        httpbin_mock.last_request.text.strip()
        == "name,species,height,appearance\nLuke Skywalker,,172,4"
    )


def test_fetch_empty_characters(swapi_empty_people, httpbin_mock):
    with pytest.raises(SystemExit):
        fetch_characters()


def test_fetch_many_pages(swapi_people_two_pages, httpbin_mock, swapi_species):
    fetch_characters()
    table = pd.read_csv(StringIO(httpbin_mock.last_request.text))
    # table = pd.read_csv(httpbin_mock.last_request.text)
    assert len(table) == 2
    assert len(table[table["name"] == "Wiktor Rutka"]) == 1
    assert len(table[table["name"] == "Luke Skywalker"]) == 1


def test_fetch_many_species(swapi_people_many_species, httpbin_mock, swapi_species):
    fetch_characters()
    table = pd.read_csv(StringIO(httpbin_mock.last_request.text))
    # table = pd.read_csv(httpbin_mock.last_request.text)
    assert len(table) == 1
    assert (
        table[table["name"] == "Wiktor Rutka"]["species"].values[0]
        == "Developer,Developer"
    )


def test_fetch_httpbin_error(swapi_people_many_species, httpbin_error, swapi_species):
    with pytest.raises(SystemExit):
        fetch_characters()
