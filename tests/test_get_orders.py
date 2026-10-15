import allure
import requests

from endpoints import BASE_URL, ORDERS_ENDPOINT


@allure.feature("Заказ")
@allure.story("Получение списка заказов")
class TestGetOrders:
    @allure.title("В ответе возвращается список заказов")
    def test_get_orders_returns_list(self):
        with allure.step("Получить список заказов"):
            response = requests.get(BASE_URL + ORDERS_ENDPOINT)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить наличие списка заказов"):
            assert "orders" in response.json()
            assert isinstance(response.json()["orders"], list)
