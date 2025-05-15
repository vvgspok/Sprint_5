from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import TestLocators
from helpers import generation_mail, generation_mail_not_mask
from data import password, existing_login, color_input


class TestRegistration:

    def test_user_registration(self, driver):

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CLICK_BUTTON_NO_ACCOUNT))
        driver.find_element(*TestLocators.CLICK_BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INPUT_FIELD_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_LOGIN).send_keys(generation_mail())
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS_REPEAT).send_keys(password)
        driver.find_element(*TestLocators.CLICK_BUTTON_CREATE_ACCOUNT).click()
        get_user_name = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_PROFILE_NAME))
        get_home_page = driver.find_element(*TestLocators.SEARCH_HOME_PAGE)
        get_avatar_user = driver.find_element(*TestLocators.SEARCH_AVATAR)

        assert get_user_name.text == 'User.' and get_avatar_user != [] and get_home_page != []

    def test_user_registration_not_by_mail_mask(self, driver):

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CLICK_BUTTON_NO_ACCOUNT))
        driver.find_element(*TestLocators.CLICK_BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INPUT_FIELD_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_LOGIN).send_keys(generation_mail_not_mask())

        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS_REPEAT).send_keys(password)
        driver.find_element(*TestLocators.CLICK_BUTTON_CREATE_ACCOUNT).click()

        error_text = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_TEXT_ERROR))

        field_email = driver.find_element(*TestLocators.SEARCH_COLOR_EMAIL)
        color_field_email = field_email.value_of_css_property('border')

        field_pass = driver.find_element(*TestLocators.SEARCH_COLOR_PASS)
        color_field_pass = field_pass.value_of_css_property('border')

        field_repeat_pass = driver.find_element(*TestLocators.SEARCH_COLOR_REPEAT_PASS)
        color_field_repeat_pass = field_repeat_pass.value_of_css_property('border')

        assert color_field_email == color_input and color_field_pass == color_input\
               and color_field_repeat_pass == color_input and error_text.text == 'Ошибка'

    def test_registering_an_existing_user(self, driver):

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.CLICK_BUTTON_NO_ACCOUNT))
        driver.find_element(*TestLocators.CLICK_BUTTON_NO_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_LOGIN).send_keys(existing_login)
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS).send_keys(password)
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS_REPEAT).send_keys(password)
        driver.find_element(*TestLocators.CLICK_BUTTON_CREATE_ACCOUNT).click()

        error_text = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_TEXT_ERROR))

        field_email = driver.find_element(*TestLocators.SEARCH_COLOR_EMAIL)
        color_field_email = field_email.value_of_css_property('border')

        field_pass = driver.find_element(*TestLocators.SEARCH_COLOR_PASS)
        color_field_pass = field_pass.value_of_css_property('border')

        field_repeat_pass = driver.find_element(*TestLocators.SEARCH_COLOR_REPEAT_PASS)
        color_field_repeat_pass = field_repeat_pass.value_of_css_property('border')

        assert color_field_email == color_input and color_field_pass == color_input\
               and color_field_repeat_pass == color_input and error_text.text == 'Ошибка'
