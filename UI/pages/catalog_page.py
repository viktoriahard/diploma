import allure
from selenium.webdriver import ActionChains
from UI.locators.catalog_page_locators import bn_electronics, tablets_category, bn_tablets
from UI.pages.base_page import BasePage


class CatalogPage(BasePage):

    @property
    def tablets(self):
        return self.wait_for(tablets_category)

    @property
    def tablets_list(self):
        return self.wait_for(bn_tablets)

    def click_bn_electronics(self):
        with allure.step():
            self.click(bn_electronics)

    def move_to_tablets(self):
        with allure.step():
            action = ActionChains(self.driver)
            action.move_to_element(self.tablets).perform()
            action.move_to_element(self.tablets_list).perform()
            action.click().perform()