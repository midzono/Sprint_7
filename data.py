import random
import string

def generate_random_string(length=10):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_courier_data():
    return {"login": generate_random_string(), "password": generate_random_string(), "firstName": generate_random_string()}

def generate_order_data(color=None):
    data = {"firstName":"Александра","lastName":"Тест","address":"Москва, Тестовая улица, 1","metroStation":4,"phone":"+7 900 000 00 00","rentTime":1,"deliveryDate":"2026-12-01","comment":"API test"}
    if color is not None: data["color"] = color
    return data
