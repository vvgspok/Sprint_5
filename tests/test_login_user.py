from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.locators import TestLocators


class TestLogin:

    def test_login_user(self, driver, create_user):

        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN_AND_REGISTRARION).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_INPUT_FIELD_LOGIN))
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_LOGIN).send_keys(create_user['email'])
        driver.find_element(*TestLocators.SEARCH_INPUT_FIELD_PASS).send_keys(create_user['password'])
        driver.find_element(*TestLocators.CLICK_BUTTON_LOGIN).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_HOME_PAGE))
        get_home_page = driver.find_element(*TestLocators.SEARCH_HOME_PAGE)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_PROFILE_NAME))
        get_user_name = driver.find_element(*TestLocators.SEARCH_PROFILE_NAME)

        get_avatar_user = driver.find_element(*TestLocators.SEARCH_AVATAR)

        assert get_user_name.text == 'User.' and get_avatar_user != [] and get_home_page != []




