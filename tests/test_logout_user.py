from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import TestLocators


class TestLogout:

    def test_logout_user(self, driver, create_user):

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INPUT_FIELD_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_LOGIN).send_keys(create_user['email'])
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS).send_keys(create_user['password'])
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CLICK_BUTTON_LOGOUT))
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGOUT).click()
        get_text_button = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION))
        get_name_user = driver.find_elements(*TestLocators.SEARCH_PROFILE_NAME)
        get_avatar_user = driver.find_elements(*TestLocators.SEARCH_AVATAR)

        assert get_name_user == [] and get_avatar_user == [] and get_text_button.text == 'Вход и регистрация'

