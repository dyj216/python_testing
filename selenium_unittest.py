import unittest
from selenium import webdriver


SERVER = "localhost:7272"
DELAY = 0
VALID_USER = "demo"
VALID_PASSWORD = "mode"
LOGIN_URL = f"http://{SERVER}/"
WELCOME_URL = f"http://{SERVER}/welcome.html"
ERROR_URL = f"http://{SERVER}/error.html"


class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path="bin/geckodriver")

    def tearDown(self) -> None:
        self.driver.close()

    def test_valid_login(self):
        self.driver.get(LOGIN_URL)
        self._input_username(VALID_USER)
        self._input_password(VALID_PASSWORD)
        self._submit_credentials()
        self.assertEqual(WELCOME_URL, self.driver.current_url)
        self.assertEqual("Welcome Page", self.driver.title)

    def test_invalid_login(self):
        for username, password in [
            ("invalid", VALID_PASSWORD),
            (VALID_USER, "invalid"),
            ("invalid", "whatever"),
            ("", VALID_PASSWORD),
            (VALID_USER, ""),
            ("", ""),
        ]:
            with self.subTest(username=username, password=password):
                self.driver.get(LOGIN_URL)
                self._input_username(username)
                self._input_password(password)
                self._submit_credentials()
                self.assertEqual(ERROR_URL, self.driver.current_url)
                self.assertEqual("Error Page", self.driver.title)

    def _input_username(self, username):
        login_field = self.driver.find_element_by_id("username_field")
        login_field.send_keys(username)

    def _input_password(self, password):
        password_field = self.driver.find_element_by_id("password_field")
        password_field.send_keys(password)

    def _submit_credentials(self):
        login_button = self.driver.find_element_by_id("login_button")
        login_button.click()


if __name__ == '__main__':
    unittest.main()
