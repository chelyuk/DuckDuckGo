"""
This module contains web test cases for the tutorial.
Tests use Selenium Webdriver with Chrome and ChromeDriver.
The fixture set up and clean up the ChromeDriver instance.
"""
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    # Wait implicitly for elements zto be ready before attemping interactions
    driver.implicitly_wait(5)

    # Return the driver object at the end of setup
    yield driver

    driver.find_element
    # For cleanup. quit the driver
    driver.quit()

def test_basic_duckduckgo_search(browser):
    # Set up some test case data
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    # Navigate to the DuckDuckGo home page
    browser.get(URL)

    # Find the search input element
    # In the DOM, it has an 'id' attribute of 'search_form_input_homepage'
    search_input = browser.find_element(By.ID,'search_form_input_homepage')

    # Send a search phrase to the input and hit the RETURN key
    search_input.send_keys(PHRASE + Keys.RETURN)

    # Verify that results appear on the results page
    link_divs = browser.find_elements(By.CSS_SELECTOR,'#links > div')
    assert len(link_divs) > 0

    # Verify that at least one search results contains the search phrase
    xpath = f"//div[@id='links']//*[contains(text(). '{PHRASE}')]"
    phrase_results = browser.find_elements(By.XPATH,xpath)
    assert len(phrase_results) > 0

    # Verify that the search phrase is the same
    search_input = browser.find_elements(By.ID,'search_form_input')
    assert search_input.get_attribute('value') == PHRASE