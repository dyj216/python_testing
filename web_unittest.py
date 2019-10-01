import unittest
from selenium import webdriver


class NuclearDisasterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path="bin/geckodriver")

    def tearDown(self) -> None:
        self.driver.close()

    def test_chernobyl_date(self):
        self.driver.get("https://wikipedia.org")
        search_field = self.driver.find_element_by_id("searchInput")
        search_field.send_keys("chernobyl disaster")
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        body_content = self.driver.find_element_by_id("bodyContent")
        paragraphs = body_content.find_elements_by_tag_name("p")
        self.assertTrue("26 April 1986" in paragraphs[2].text)

    @unittest.expectedFailure
    def test_chernobyl_us_spies(self):
        self.driver.get("https://wikipedia.org")
        search_field = self.driver.find_element_by_id("searchInput")
        search_field.send_keys("chernobyl disaster")
        submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()
        body_content = self.driver.find_element_by_id("bodyContent")
        paragraphs = body_content.find_elements_by_tag_name("p")
        self.assertTrue("US spies" in paragraphs[2].text)

    def test_chernobyl(self):
        for fact in ["26 April 1986", "US Spies"]:
            with self.subTest(fact=fact):
                self.driver.get("https://wikipedia.org")
                search_field = self.driver.find_element_by_id("searchInput")
                search_field.send_keys("chernobyl disaster")
                submit_button = self.driver.find_element_by_xpath("//button[@type='submit']")
                submit_button.click()
                body_content = self.driver.find_element_by_id("bodyContent")
                paragraphs = body_content.find_elements_by_tag_name("p")
                self.assertTrue(fact in paragraphs[2].text)

    def test_fukushima(self):
        self.driver.get("https://en.wikipedia.org/wiki/Chernobyl_disaster")
        link = self.driver.find_elements_by_xpath("//a[@href='/wiki/Fukushima_Daiichi_nuclear_disaster']")[0]
        link.click()
        p = self.driver.find_element_by_css_selector(".mw-parser-output > p:nth-child(8)")
        self.assertIn("11 March 2011", p.text)
