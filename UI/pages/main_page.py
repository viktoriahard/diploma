from UI.locators.main_page_locators import bn_catalog
from UI.pages.base_page import BasePage


class MainPage(BasePage):

    def click_bn_catalog(self):
        self.click(bn_catalog)
