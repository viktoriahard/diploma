import allure

from UI.locators.item_page_locators import bn_add_to_cart, bn_move_to_cart
from UI.pages.base_page import BasePage


class ItemPage(BasePage):

    def add_to_cart(self):
        with allure.step():
            self.wait_for(bn_add_to_cart)
            self.click(bn_add_to_cart)

    def move_to_cart(self):
        with allure.step():
            self.wait_for(bn_move_to_cart)
            self.click(bn_move_to_cart)
