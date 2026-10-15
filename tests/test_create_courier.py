import allure
import pytest
import requests

from data import generate_courier_data
from endpoints import BASE_URL, CREATE_COURIER_ENDPOINT


@allure.feature("Курьер")
@allure.story("Создание курьера")
class TestCreateCourier:
    @allure.title("Можно создать курьера")
    def test_create_courier_success(self, courier_cleanup):
        data = generate_courier_data()
        courier_cleanup.append(data)

        with allure.step("Создать курьера"):
            response = requests.post(BASE_URL + CREATE_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 201

        with allure.step("Проверить тело ответа"):
            assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_identical_couriers_returns_error(self, courier):
        with allure.step("Создать второго курьера с теми же данными"):
            response = requests.post(BASE_URL + CREATE_COURIER_ENDPOINT, json=courier)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 409

        with allure.step("Проверить тело ответа"):
            assert response.json() == {
                "code": 409,
                "message": "Этот логин уже используется. Попробуйте другой."
            }

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Нельзя создать курьера без обязательного поля")
    def test_create_courier_without_required_field_returns_error(self, missing_field, courier_cleanup):
        data = generate_courier_data()
        data.pop(missing_field)

        with allure.step("Отправить запрос на создание курьера без обязательного поля"):
            response = requests.post(BASE_URL + CREATE_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 400

        with allure.step("Проверить тело ответа"):
            assert response.json() == {
                "code": 400,
                "message": "Недостаточно данных для создания учетной записи"
            }

    @allure.title("Нельзя создать курьера с существующим логином")
    def test_create_courier_with_existing_login_returns_error(self, courier):
        data = generate_courier_data()
        data["login"] = courier["login"]

        with allure.step("Создать курьера с существующим логином"):
            response = requests.post(BASE_URL + CREATE_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 409

        with allure.step("Проверить тело ответа"):
            assert response.json() == {
                "code": 409,
                "message": "Этот логин уже используется. Попробуйте другой."
            }
