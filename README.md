# Sprint_7

Проект по тестированию API учебного сервиса «Яндекс Самокат».

## Технологии

- Python
- pytest
- requests
- Allure

## Установка

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск тестов

```bash
pytest
```

## Allure

```bash
pytest --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```
