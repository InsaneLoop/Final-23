# Placeholder for UI tests
# Directory: tests/test_ui.py
from utils.driver_pool import DriverPool
from utils.orm import save_test_result
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.parametrize("username, password", [
    ("valid_user", "valid_pass"),
    ("invalid_user", "invalid_pass"),
    ("user_with_special_chars", "pass!@#")
])
def test_web_ui(username, password):
    pool = DriverPool()
    driver = pool.get_driver('chrome')
    driver.get("https://example.com/login")

    login_page = LoginPage(driver)
    login_page.set_username(username)
    login_page.set_password(password)
    login_page.click_login()

    # Check result based on user input
    if username == "valid_user":
        assert "Welcome" in driver.page_source
        save_test_result("test_web_ui_valid", "Passed")
    else:
        assert "Error" in driver.page_source
        save_test_result("test_web_ui_invalid", "Failed")

    pool.quit_all()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "loginBtn")

    def set_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input)).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
