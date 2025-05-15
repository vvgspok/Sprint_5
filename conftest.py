from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helpers import generation_mail
import pytest
import requests


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    data = {
        "email": f"{generation_mail()}",
        "password": "Test123!",
        "submitPassword": "Test123!"

    }
    requests.post(
        url="https://qa-desk.stand.praktikum-services.ru/api/signup",
        data=data
    )
    return data

