import pytest
from selenium import webdriver


@pytest.fixture
def selenium_webdriver():
    driver = webdriver.Firefox(executable_path="bin/geckodriver")
    yield driver
    driver.close()


def test_chernobyl_accident_date():
    driver = webdriver.Firefox(executable_path="bin/geckodriver")
    driver.get("https://wikipedia.org")
    search_field = driver.find_element_by_id("searchInput")
    search_field.send_keys("chernobyl disaster")
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()
    body_content = driver.find_element_by_id("bodyContent")
    paragraphs = body_content.find_elements_by_tag_name("p")
    assert "26 April 1986" in paragraphs[2].text
    driver.close()
