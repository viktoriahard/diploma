import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from UI.pages.cart_page import CartPage
from UI.pages.catalog_page import CatalogPage
from UI.pages.item_page import ItemPage
from UI.pages.items_list_page import ItemsListPage
from UI.pages.main_page import MainPage


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.onliner.by/")
    yield driver


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def items_list_page(driver):
    yield ItemsListPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)