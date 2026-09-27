import allure
import pytest
import requests
from endpoints import BASE_URL, LOGIN_COURIER_ENDPOINT

@allure.feature("Курьер")
@allure.story("Логин курьера")
class TestLoginCourier:
    @allure.title("Зарегистрированный курьер может авторизоваться")
    def test_login_courier_success(self,courier):
        response=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json={"login":courier["login"],"password":courier["password"]})
        assert response.status_code==200; assert "id" in response.json(); assert isinstance(response.json()["id"],int)

    @pytest.mark.parametrize("missing_field",["login","password"])
    @allure.title("Нельзя авторизоваться без обязательного поля")
    def test_login_courier_without_required_field_returns_error(self,courier,missing_field):
        data={"login":courier["login"],"password":courier["password"]}; data.pop(missing_field); response=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json=data)
        assert response.status_code==400; assert response.json()=={"code":400,"message":"Недостаточно данных для входа"}

    @pytest.mark.parametrize("field",["login","password"])
    @allure.title("Нельзя авторизоваться с неправильными данными")
    def test_login_courier_with_wrong_data_returns_error(self,courier,field):
        data={"login":courier["login"],"password":courier["password"]}; data[field]="wrong_data_123"; response=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json=data)
        assert response.status_code==404; assert response.json()=={"code":404,"message":"Учетная запись не найдена"}

    @allure.title("Нельзя авторизоваться под несуществующим пользователем")
    def test_login_nonexistent_courier_returns_error(self):
        response=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json={"login":"nonexistent_login_123456","password":"nonexistent_password_123456"})
        assert response.status_code==404; assert response.json()=={"code":404,"message":"Учетная запись не найдена"}
