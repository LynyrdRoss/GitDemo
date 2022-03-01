from selenium.webdriver.common.by import By

from page_object.confirm import Confirm


class CheckOut:
    new_variable_to_push_from_checkout_one = 'One'
    new_variable_to_push_from_checkout_two = 'Two'
    new_variable_to_push_from_checkout_three = 'Three'

    def __init__(self, driver):
        self.driver = driver

    def get_product_title(self):
        return self.driver.find_elements(
            By.CSS_SELECTOR,
            '.card-title a'
        )

    def click_blackberry_button(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            '.card-footer button'
        ).click()

    def click_checkout_btn(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "a[class*='btn-primary']"
        ).click()

    def proceed_to_checkout(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[class*='btn-success']"
        ).click()

        return Confirm(self.driver)

    def new_click_checkout_btn(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            "a[class*='btn-primary']"
        ).click()

    @staticmethod
    def two_new_function():
        for i in range(1, 3):
            print('New function example')
