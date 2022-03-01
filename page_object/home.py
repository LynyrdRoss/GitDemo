from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_object.checkout import CheckOut


class HomePage:
    new_variable_to_push_one = 'Ross'
    new_variable_to_push_two = 'Lynyrd'
    new_variable_to_push_three = 'LynyrdRoss'

    def __init__(self, driver):
        self.driver = driver

    def click_shop(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            "a[href*='shop']"
        ).click()

        return CheckOut(self.driver)

    def input_name(self, name):
        self.driver.find_element(
            By.NAME,
            'name'
        ).send_keys(name)

    def input_email(self, email):
        self.driver.find_element(
            By.NAME,
            'email'
        ).send_keys(email)

    def tick_ice_cream_box(self):
        self.driver.find_element(
            By.ID, 'exampleCheck1'
        ).click()

    def select_gender(self, gender='Male'):
        gender_list = Select(
            self.driver.find_element(
                By.ID, 'exampleFormControlSelect1'
            )
        )

        gender_list.select_by_visible_text(gender)

    def click_submit(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "[type='submit']"
        ).click()

    @staticmethod
    def new_function_for_git():
        for i in range(1, 3):
            print('test only')

    @staticmethod
    def two_new_function():
        for i in range(1, 3):
            print('New function example')
