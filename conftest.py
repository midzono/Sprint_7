import pytest
import requests

from data import generate_courier_data
from endpoints import (
    BASE_URL,
    CREATE_COURIER_ENDPOINT,
    DELETE_COURIER_ENDPOINT,
    LOGIN_COURIER_ENDPOINT,
)


@pytest.fixture
def courier():
    data = generate_courier_data()

    requests.post(BASE_URL + CREATE_COURIER_ENDPOINT, json=data)

    yield data

    login_response = requests.post(
        BASE_URL + LOGIN_COURIER_ENDPOINT,
        json={
            "login": data["login"],
            "password": data["password"]
        }
    )

    if login_response.status_code == 200:
        requests.delete(BASE_URL + DELETE_COURIER_ENDPOINT.format(login_response.json()["id"]))


@pytest.fixture
def courier_cleanup():
    couriers = []

    yield couriers

    for data in couriers:
        login_response = requests.post(
            BASE_URL + LOGIN_COURIER_ENDPOINT,
            json={
                "login": data["login"],
                "password": data["password"]
            }
        )

        if login_response.status_code == 200:
            requests.delete(BASE_URL + DELETE_COURIER_ENDPOINT.format(login_response.json()["id"]))
