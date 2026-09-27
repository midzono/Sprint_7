import allure
import pytest
import requests
from data import generate_order_data
from endpoints import BASE_URL, ORDERS_ENDPOINT

@allure.feature("Заказ")
@allure.story("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize("color",[pytest.param(["BLACK"],id="black"),pytest.param(["GREY"],id="grey"),pytest.param(["BLACK","GREY"],id="black_and_grey"),pytest.param(None,id="without_color")])
    @allure.title("Можно создать заказ с разными вариантами цвета")
    def test_create_order_with_different_colors_returns_track(self,color):
        response=requests.post(BASE_URL+ORDERS_ENDPOINT,json=generate_order_data(color))
        assert response.status_code==201; assert "track" in response.json(); assert isinstance(response.json()["track"],int)
