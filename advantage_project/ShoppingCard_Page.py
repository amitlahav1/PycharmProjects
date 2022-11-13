from selenium import webdriver
from selenium.webdriver.common.by import By


class ShoppingCard_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

#return the "shopping cart" text in the page of shopping cart.
    def shopping_card_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='select  ng-binding']").text

    def edit_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='edit ng-scope']")

    #edit product, choose product that you want to edit (num_of_product) , from 1 = the first product - "user friendly"
    def click_edit_product(self, num_of_product:int):
        num_of_product -= 1
        return self.driver.execute_script("arguments[0].click();", self.edit_product()[num_of_product])

    # QTY of the first product in the shopping cart page
    def qty_first_product_shipping_page(self):
        self.list = self.driver.find_elements(By.CSS_SELECTOR,
                                              "html>body>div>section>article>div>table>tbody>tr>td>label")
        qty = self.list[4].text
        qty = int(qty)
        return qty

    # QTY of the second product in the shopping cart page
    def qty_second_product_shipping_page(self):
        self.list = self.driver.find_elements(By.CSS_SELECTOR,
                                              "html>body>div>section>article>div>table>tbody>tr>td>label")
        qty = self.list[10].text
        qty = int(qty)
        return qty

    # QTY of the third product in the shopping cart page

    def qty_third_product_shipping_page(self):
        self.list = self.driver.find_elements(By.CSS_SELECTOR,
                                              "html>body>div>section>article>div>table>tbody>tr>td>label")
        qty = self.list[16].text
        qty = int(qty)
        return qty

    # return the price of the product in shopping cart . user put the num of product(from 1)
    def price_product(self, number_of_product_from1: int):
        price = self.driver.find_element(By.XPATH, f"//article/div/table/tbody/tr[{number_of_product_from1}]/td/p").text
        price = price[1:]
        price = float(price)
        return price

    # return the name of product . user put the num of product in shopping cart page
    def name_product(self, num_of_product):
        name = self.driver.find_element(By.XPATH, f"//table/tbody/tr[{num_of_product}]/td[2]/label").text
        return name

    #click on checkout
    def click_checkout(self):
        self.checkout = self.driver.find_element(By.ID, "checkOutButton").click()


