from locators.locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import generation_name_ad, random_price, random_description


class TestCreatingAnAd:

    def test_ad_creation_by_unauthorized_user(self, driver):

        driver.find_element(*TestLocators.CLICK_BUTTON_PLACE_AN_AD).click()
        get_title_text = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_TITLE_LINK_TO_THE_AD_LOG_IN))

        assert get_title_text.text == "Чтобы разместить объявление, авторизуйтесь"

    def test_ad_creation_by_authorized_user(self, driver, create_user):

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INPUT_FIELD_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_LOGIN).send_keys(create_user['email'])
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS).send_keys(create_user['password'])
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_PROFILE_NAME))
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CLICK_BUTTON_PLACE_AN_AD))
        driver.find_element(*TestLocators.CLICK_BUTTON_PLACE_AN_AD).click()
        new_ad_name = generation_name_ad()
        driver.find_element(*TestLocators.SEARCH_INPUT_NAME).send_keys(new_ad_name)
        driver.find_element(*TestLocators.SEARCH_INPUT_DESCRIPTION).send_keys(random_description())
        driver.find_element(*TestLocators.SEARCH_INPUT_PRICE).send_keys(random_price())
        driver.find_element(*TestLocators.CLICK_ITEM_CONDITION_USED).click()
        driver.find_element(*TestLocators.CLICK_DROPDOWN_CATEGORY).click()
        driver.find_element(*TestLocators.CLICK_RANDOM_CATEGORY).click()
        driver.find_element(*TestLocators.CLICK_DROPDOWN_CITY).click()
        driver.find_element(*TestLocators.CLICK_RANDOM_CITY).click()
        driver.find_element(*TestLocators.CLICK_BUTTON_PUBLISH).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_HOME_PAGE))
        driver.find_element(*TestLocators.CLICK_BUTTON_PROFILE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_AD_NAME_IN_PROFILE))
        get_ad_name = driver.find_element(*TestLocators.SEARCH_AD_NAME_IN_PROFILE)

        assert get_ad_name.text == new_ad_name
