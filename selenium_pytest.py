import pytest
from selenium import webdriver


SERVER = "localhost:7272"
DELAY = 0
VALID_USER = "demo"
VALID_PASSWORD = "mode"
LOGIN_URL = f"http://{SERVER}/"
WELCOME_URL = f"http://{SERVER}/welcome.html"
ERROR_URL = f"http://{SERVER}/error.html"


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Firefox(executable_path="bin/geckodriver")
    driver.maximize_window()
    yield driver
    driver.close()


def test_valid_login(driver: webdriver.Firefox):
    driver.get(LOGIN_URL)
    input_username(driver, VALID_USER)
    input_password(driver, VALID_PASSWORD)
    submit_credentials(driver)
    assert driver.current_url == WELCOME_URL
    assert driver.title == "Welcome Page"


def input_username(driver, username):
    login_field = driver.find_element_by_id("username_field")
    login_field.send_keys(username)


def input_password(driver, password):
    password_field = driver.find_element_by_id("password_field")
    password_field.send_keys(password)


def submit_credentials(driver):
    login_button = driver.find_element_by_id("login_button")
    login_button.click()


@pytest.mark.parametrize(
    "username,password",
    [
        ("invalid", VALID_PASSWORD),
        (VALID_USER, "invalid"),
        ("invalid", "whatever"),
        ("", VALID_PASSWORD),
        (VALID_USER, ""),
        ("", ""),
    ]
)
def test_invalid_login(driver: webdriver.Firefox, username, password):
    driver.get(LOGIN_URL)
    input_username(driver, username)
    input_password(driver, password)
    submit_credentials(driver)
    assert driver.current_url == ERROR_URL
    assert driver.title == "Error Page"
