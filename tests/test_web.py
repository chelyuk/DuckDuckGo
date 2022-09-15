"""
This module contains web test cases for the tutorial.
Tests use Selenium Webdriver with Chrome and ChromeDriver.
The fixture set up and clean up the ChromeDriver instance.
"""
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


def test_basic_duckduckgo_search(browser):
    PHRASE = 'panda'

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
