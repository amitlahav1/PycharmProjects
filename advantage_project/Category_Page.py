from selenium import webdriver
from selenium.webdriver.common.by import By


class Category_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

# return list with all products in the category
    def products_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")

# choose a product , with num of product - the left is 1  - "user friendly"
    def choose_product(self, number_of_product: int):
        number_of_product = number_of_product - 1
        self.products_list()[number_of_product].click()

# return the name of category
    def name_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

