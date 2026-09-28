import allure
import pytest
import requests

from endpoints import BASE_URL, LOGIN_COURIER_ENDPOINT


@allure.feature("Курьер")
@allure.story("Логин курьера")
class TestLoginCourier:
    @allure.title("Зарегистрированный курьер может авторизоваться")
    def test_login_courier_success(self, courier):
        data = {
            "login": courier["login"],
            "password": courier["password"]
        }

        with allure.step("Авторизоваться под зарегистрированным курьером"):
            response = requests.post(BASE_URL + LOGIN_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 200

        with allure.step("Проверить наличие id в ответе"):
            assert "id" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title("Нельзя авторизоваться без обязательного поля")
    def test_login_courier_without_required_field_returns_error(self, courier, missing_field):
        data = {
            "login": courier["login"],
            "password": courier["password"]
        }
        data.pop(missing_field)

        with allure.step("Отправить запрос без обязательного поля"):
            response = requests.post(BASE_URL + LOGIN_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 400

        with allure.step("Проверить тело ответа"):
            assert response.json() == {
                "code": 400,
                "message": "Недостаточно данных для входа"
            }

    @pytest.mark.parametrize("field", ["login", "password"])
    @allure.title("Нельзя авторизоваться с неправильными данными")
    def test_login_courier_with_wrong_data_returns_error(self, courier, field):
        data = {
            "login": courier["login"],
            "password": courier["password"]
        }
        data[field] = "wrong_data_123"

        with allure.step("Авторизоваться с неправильными данными"):
            response = requests.post(BASE_URL + LOGIN_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить тело ответа"):
            assert response.json() == {
                "code": 404,
                "message": "Учетная запись не найдена"
            }

    @allure.title("Нельзя авторизоваться под несуществующим пользователем")
    def test_login_nonexistent_courier_returns_error(self):
        data = {
            "login": "nonexistent_login_123456",
            "password": "nonexistent_password_123456"
        }

        with allure.step("Авторизоваться под несуществующим пользователем"):
            response = requests.post(BASE_URL + LOGIN_COURIER_ENDPOINT, json=data)

        with allure.step("Проверить код ответа"):
            assert response.status_code == 404

        with allure.step("Проверить тело ответа"):
            assert response.json() == {
                "code": 404,
                "message": "Учетная запись не найдена"
            }
