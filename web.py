import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Firefox(executable_path="bin/geckodriver")
    yield driver
    driver.close()


def test_chernobyl_fact(driver, fact):
    driver.get("https://wikipedia.org")
    search_field = driver.find_element_by_id("searchInput")
    search_field.send_keys("chernobyl disaster")
    submit_button = driver.find_element_by_xpath("//button[@type='submit']")
    submit_button.click()
    body_content = driver.find_element_by_id("bodyContent")
    paragraphs = body_content.find_elements_by_tag_name("p")
    assert fact in paragraphs[2].text


def test_fukushima(driver):
    driver.get("https://en.wikipedia.org/wiki/Chernobyl_disaster")
    link = driver.find_elements_by_xpath("//a[@href='/wiki/Fukushima_Daiichi_nuclear_disaster']")[0]
    link.click()
    p = driver.find_element_by_css_selector(".mw-parser-output > p:nth-child(8)")
    assert "11 March 2011" in p.text
    return 0
