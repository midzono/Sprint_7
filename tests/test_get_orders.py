import allure
import requests
from endpoints import BASE_URL, ORDERS_ENDPOINT

@allure.feature("Заказ")
@allure.story("Получение списка заказов")
class TestGetOrders:
    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_returns_list(self):
        response=requests.get(BASE_URL+ORDERS_ENDPOINT)
        assert response.status_code==200; assert "orders" in response.json(); assert isinstance(response.json()["orders"],list)
