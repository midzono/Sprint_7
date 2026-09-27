# Sprint_7

API-тесты учебного сервиса «Яндекс Самокат». Для каждой ручки используется отдельный класс. Тесты проверяют и статус, и тело ответа.

## Запуск
`pip install -r requirements.txt`
`pytest -v`

## Allure
`pytest --alluredir=allure-results`
`allure generate allure-results -o allure-report --clean`
`allure open allure-report`

В GitHub по требованиям проекта добавляется только сгенерированная папка `allure-report/`; `allure-results/` не пушится.

Курьеры для авторизации создаются фикстурой перед тестом и удаляются после. Курьеры, созданные в тестах создания, также удаляются после проверки.
