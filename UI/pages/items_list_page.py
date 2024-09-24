import allure
from selenium.webdriver import ActionChains
from UI.locators.items_list_page_locators import apple_box, ipad_item
from UI.pages.base_page import BasePage


class ItemsListPage(BasePage):

    def click_apple(self):
        with allure.step():
            self.driver.execute_script("window.scrollTo(0, 400);")
            self.click(apple_box)

    @property
    def apple_list(self):
        return self.wait_for(ipad_item)

    def click_item(self):
        with allure.step():
            action = ActionChains(self.driver)
            action.move_to_element(self.apple_list).perform()
            action.click().perform()
