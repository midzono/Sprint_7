import allure
import pytest
import requests

from data import generate_order_data
from endpoints import BASE_URL, ORDERS_ENDPOINT


@allure.feature("Заказ")
@allure.story("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize(
        "color",
        [
            pytest.param(["BLACK"], id="black"),
            pytest.param(["GREY"], id="grey"),
            pytest.param(["BLACK", "GREY"], id="black_and_grey"),
            pytest.param(None, id="without_color")
        ]
    )
    @allure.title("Можно создать заказ с разными вариантами цвета")
    def test_create_order_with_different_colors_returns_track(self, color):
        data = generate_order_data(color)

        with allure.step("Создать заказ"):
            response = requests.post(BASE_URL + ORDERS_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 201

        with allure.step("Проверить наличие track в ответе"):
            assert "track" in response.json()
