import allure

from UI.locators.cart_page_locators import cart_item_price, bn_buy
from UI.pages.base_page import BasePage


class CartPage(BasePage):

    def check_cart_items_amount(self, num_items: int):
        with allure.step():
            cart_amount = self.text(cart_item_price)
            expected_amount = f"{num_items}"
            assert expected_amount in cart_amount

    def check_cart_title(self):
        with allure.step():
            page_title = self.driver.title
            assert page_title == "Корзина заказов onliner.by"

    def check_submit_is_clickable(self):
        with allure.step():
            self.wait_for_element_to_be_clickable(bn_buy)
