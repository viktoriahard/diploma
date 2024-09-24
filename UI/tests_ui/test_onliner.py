import time

import allure
import pytest


class TestAddTabletToCart:

    @allure.title("Test Ipad")
    @allure.id("1")
    @allure.description("Choose an item and add it to cart")
    @allure.feature("Apple Ipad")
    @pytest.mark.smoke
    def test_ipad(self, main_page, catalog_page, items_list_page, item_page, cart_page):
        main_page.click_bn_catalog()
        time.sleep(7)  # cookie settings
        catalog_page.click_bn_electronics()
        catalog_page.move_to_tablets()

        items_list_page.click_apple()
        time.sleep(5)
        items_list_page.click_item()

        item_page.add_to_cart()
        item_page.move_to_cart()

        cart_page.check_cart_items_amount(1)
        cart_page.check_cart_title()
        cart_page.check_submit_is_clickable()




