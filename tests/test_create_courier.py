import allure
import pytest
import requests
from data import generate_courier_data
from endpoints import BASE_URL, CREATE_COURIER_ENDPOINT, DELETE_COURIER_ENDPOINT, LOGIN_COURIER_ENDPOINT

@allure.feature("Курьер")
@allure.story("Создание курьера")
class TestCreateCourier:
    @allure.title("Можно создать курьера")
    def test_create_courier_success(self):
        data=generate_courier_data(); response=requests.post(BASE_URL+CREATE_COURIER_ENDPOINT,json=data)
        assert response.status_code==201
        assert response.json()=={"ok":True}
        login=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json={"login":data["login"],"password":data["password"]})
        requests.delete(BASE_URL+DELETE_COURIER_ENDPOINT.format(login.json()["id"]))

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_identical_couriers_returns_error(self):
        data=generate_courier_data(); first=requests.post(BASE_URL+CREATE_COURIER_ENDPOINT,json=data); second=requests.post(BASE_URL+CREATE_COURIER_ENDPOINT,json=data)
        assert first.status_code==201; assert first.json()=={"ok":True}
        assert second.status_code==409
        assert second.json()=={"code":409,"message":"Этот логин уже используется. Попробуйте другой."}
        login=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json={"login":data["login"],"password":data["password"]}); requests.delete(BASE_URL+DELETE_COURIER_ENDPOINT.format(login.json()["id"]))

    @pytest.mark.parametrize("missing_field",["login","password"])
    @allure.title("Нельзя создать курьера без обязательного поля")
    def test_create_courier_without_required_field_returns_error(self,missing_field):
        data=generate_courier_data(); data.pop(missing_field); response=requests.post(BASE_URL+CREATE_COURIER_ENDPOINT,json=data)
        assert response.status_code==400
        assert response.json()=={"code":400,"message":"Недостаточно данных для создания учетной записи"}

    @allure.title("Нельзя создать курьера с существующим логином")
    def test_create_courier_with_existing_login_returns_error(self):
        first=generate_courier_data(); created=requests.post(BASE_URL+CREATE_COURIER_ENDPOINT,json=first); second=generate_courier_data(); second["login"]=first["login"]; response=requests.post(BASE_URL+CREATE_COURIER_ENDPOINT,json=second)
        assert created.status_code==201; assert created.json()=={"ok":True}; assert response.status_code==409
        assert response.json()=={"code":409,"message":"Этот логин уже используется. Попробуйте другой."}
        login=requests.post(BASE_URL+LOGIN_COURIER_ENDPOINT,json={"login":first["login"],"password":first["password"]}); requests.delete(BASE_URL+DELETE_COURIER_ENDPOINT.format(login.json()["id"]))
