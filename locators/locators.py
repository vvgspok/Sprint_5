from selenium.webdriver.common.by import By
from helpers import random_city, random_category


class TestLocators:

    CLICK_BUTTON_LOGIN_AND_REGISTRARION = By.XPATH, "//*[text()='Вход и регистрация']"
    CLICK_BUTTON_NO_ACCOUNT = By.XPATH, "//*[text()='Нет аккаунта']"
    CLICK_BUTTON_LOGIN = By.XPATH, "//button[text()='Войти']"
    CLICK_BUTTON_CREATE_ACCOUNT = By.XPATH, "//*[text()='Создать аккаунт']"
    CLICK_BUTTON_PLACE_AN_AD = By.XPATH, "//*[text()='Разместить объявление']"
    CLICK_BUTTON_LOGOUT = By.XPATH, "//Button[text()='Выйти']"

    CLICK_ITEM_CONDITION_USED = By.XPATH, "//*[text()='Б/У']/preceding-sibling::div"
    CLICK_DROPDOWN_CATEGORY = By.XPATH, "//*[@name='category']/following-sibling::button"
    CLICK_RANDOM_CATEGORY = By.XPATH, f"//*[@name='category']/parent::*/following-sibling::div//*[text()='{random_category()}']"
    CLICK_DROPDOWN_CITY = By.XPATH, "//*[@name='city']/following-sibling::button"
    CLICK_RANDOM_CITY = By.XPATH, f"//*[@name='city']/parent::*/following-sibling::div//*[text()='{random_city()}']"
    CLICK_BUTTON_PUBLISH = By.XPATH, "//*[text()='Опубликовать']"
    CLICK_BUTTON_PROFILE = By.XPATH, "//*[@class='circleSmall']"

    SEARCH_HOME_PAGE = By.XPATH, "//*[contains(@class, 'homePage_homepage')]"
    SEARCH_INPUT_FIELD_LOGIN = By.NAME,"email"
    SEARCH_INPUT_FIELD_PASS = By.NAME, "password"
    SEARCH_INPUT_FIELD_PASS_REPEAT = By.NAME, "submitPassword"
    SEARCH_INPUT_NAME = By.XPATH, "//*[@name='name']"
    SEARCH_INPUT_DESCRIPTION = By.XPATH, "//textarea[@name='description']"
    SEARCH_INPUT_PRICE = By.XPATH, "//*[@name='price']"
    SEARCH_AVATAR = By.XPATH, "//*[@class='svgSmall']"
    SEARCH_PROFILE_NAME = By.XPATH, "//*[contains(@class, 'profileText')]"
    SEARCH_TITLE_LINK_TO_THE_AD_LOG_IN = By.XPATH, "//*[text()='Чтобы разместить объявление, авторизуйтесь']"
    SEARCH_TEXT_ERROR = By.XPATH, "//*[contains(@class, 'input_span') and text()='Ошибка']"
    SEARCH_COLOR_EMAIL = By.XPATH, "//*[@name = 'email']/parent::div"
    SEARCH_COLOR_PASS = By.XPATH, "//*[@name = 'password']/parent::div"
    SEARCH_COLOR_REPEAT_PASS = By.XPATH, "//*[@name = 'submitPassword']/parent::div"
    SEARCH_BLOCK_MY_AD = By.XPATH, "//*[text() = 'Мои объявления']"
    SEARCH_AD_NAME_IN_PROFILE = By.XPATH, "//*[@class='about']/child::h2"
    DOC = By.XPATH, "//*[text() = 'Документация']"