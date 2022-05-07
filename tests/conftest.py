import re

import pytest
import requests_mock


@pytest.fixture
def request_mock():
    with requests_mock.Mocker() as m:
        yield m


@pytest.fixture
def httpbin_mock(request_mock):
    return request_mock.post(
        "https://httpbin.org/post", text='{"message": "Hello, World!"}'
    )


@pytest.fixture
def swapi_people(request_mock):
    swapi_resp = {
        "count": 1,
        "next": "",
        "previous": None,
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/2/",
                    "https://swapi.dev/api/films/3/",
                    "https://swapi.dev/api/films/6/",
                ],
                "species": [],
            },
        ],
    }
    request_mock.get("https://swapi.dev/api/people", json=swapi_resp)
    return swapi_resp


@pytest.fixture
def swapi_empty_people(request_mock):
    swapi_resp = {
        "count": 1,
        "next": "",
        "previous": None,
        "results": [],
    }
    request_mock.get("https://swapi.dev/api/people", json=swapi_resp)
    return swapi_resp


@pytest.fixture
def swapi_people_two_pages(request_mock):
    swapi_resp_1 = {
        "count": 2,
        "next": "https://swapi.dev/api/people/?page=2",
        "previous": None,
        "results": [
            {
                "name": "Luke Skywalker",
                "height": "172",
                "films": [
                    "https://swapi.dev/api/films/1/",
                    "https://swapi.dev/api/films/2/",
                    "https://swapi.dev/api/films/3/",
                    "https://swapi.dev/api/films/6/",
                ],
                "species": [],
            },
        ],
    }
    swapi_resp_2 = {
        "count": 2,
        "next": "",
        "previous": None,
        "results": [
            {
                "name": "Wiktor Rutka",
                "height": "176",
                "films": [
                    "https://swapi.dev/api/films/imaginary_movie/",
                ],
                "species": ["https://swapi.dev/api/species/developer/"],
            },
        ],
    }
    return request_mock.get(
        re.compile("https://swapi.dev/api/people.*"),
        [{"json": swapi_resp_1}, {"json": swapi_resp_2}],
    )


@pytest.fixture
def swapi_people_many_species(request_mock):
    swapi_resp = {
        "count": 1,
        "next": "",
        "previous": None,
        "results": [
            {
                "name": "Wiktor Rutka",
                "height": "176",
                "films": [],
                "species": [
                    "https://swapi.dev/api/species/developer/",
                    "https://swapi.dev/api/species/developer2/",
                ],
            },
        ],
    }
    request_mock.get("https://swapi.dev/api/people", json=swapi_resp)
    return swapi_resp


@pytest.fixture
def swapi_people_error(request_mock):
    return request_mock.get("https://swapi.dev/api/people/", status_code=501)


@pytest.fixture
def swapi_species(request_mock):
    return request_mock.get(
        re.compile("https://swapi.dev/api/species/developer.*"),
        json={"name": "Developer"},
    )


@pytest.fixture
def httpbin_error(request_mock):
    return request_mock.post("https://httpbin.org/post", status_code=501)
