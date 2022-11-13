from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Checkout_Page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    # send user name
    def input_user_name_2(self, txt: str):
        USER = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "ng-valid ng-scope ng-dirty ng-valid-parse ng-touched invalid"))).click()
        USER.send_keys(txt)

    # send password
    def input_password(self, txt: str):
        self.password = self.driver.find_element(By.NAME, "passwordInOrderPayment").click()
        self.password.send_keys(txt)

    # click login
    def click_login(self):
        self.login = self.driver.find_element(By.CSS_SELECTOR, "[id='login_btnundefined']")
        self.login.click()

    # click next on payment
    def click_next(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[id='next_btn'][role='button']"))).click()

    # chose cc by the radio button
    def click_radio_creditcard(self):
        self.radio_button = self.driver.find_element(By.NAME, "masterCredit")
        self.radio_button.click()

    # scroll down
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

    # go to my orders page
    def user_my_orders_bottun_TG(self):
        myorders_bottun = self.driver.find_elements(By.CSS_SELECTOR, "#menuUserLink>div>label")
        myorders_bottun[1].click()

    # go to my acount page
    def user_my_acount_bottun_TG(self):
        self.myorders_bottun = self.driver.find_elements(By.CSS_SELECTOR, "#menuUserLink>div>label")
        self.myorders_bottun[0].click()

    # delete your acount page
    def delete_my_account_tg(self):
        bottun_del = self.driver.find_element(By.CLASS_NAME, "deleteBtnText").click()

    # press yes on delete my acount
    def yes_delete_my_account_tg(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='deletePopupBtn deleteRed']").click()

    # click registration ?????
    def click_registration(self):
        self.regi = self.driver.find_element(By.ID, "registration_btnundefined").click()

    # go to checkout from cart
    def click_cahekout_in_cart(self):
        self.chekgOut = self.driver.find_element(By.ID, "checkOutButton").click()

    # find len of list table order
    def list_table_order(self):
        list = self.driver.find_elements(By.CSS_SELECTOR, "[class='ng-binding']")
        return len(list)

    # find safepay username element
    def safepay_username(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='safepay_username'][type='text']"))).click()

    # send keys to safepay username
    def safepay_username_send_k(self, txt: str):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='safepay_username'][type='text']"))).send_keys(
            txt)

    # send safepay elemnet
    def safepay_password(self, txt: str):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[name='safepay_password'][type='password']"))).click()

    # send keys to safepay password
    def safepay_password_send_k(self, txt: str):
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[name='safepay_password'][type='password']"))).send_keys(txt)

    # click pay now in safepay
    def pay_now_btn_SAFEPAY(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "pay_now_btn_SAFEPAY"))).click()

    # prove the txt -no items-
    def empty_cart_prove_txt(self):
        cart = self.driver.find_element(By.CSS_SELECTOR,
                                        "[class='center roboto-medium ng-scope'][translate='Your_shopping_cart_is_empty']").text
        return cart

    # get the empty cart seantnce len
    def empty_cart_prove_len(self):
        cart = self.driver.find_element(By.CSS_SELECTOR,
                                        "[class='center roboto-medium ng-scope'][translate='Your_shopping_cart_is_empty']").text
        return len(cart)

    # pay noy mastercredit
    def pay_now_btn_MasterCredit_01(self):
        pay = self.driver.find_elementent(By.ID, "pay_now_btn_MasterCredit").click()

    # save the prove of no orders ???
    def no_orders_prove(self):
        no_orders_txt = self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-bold ng-binding']")
        return no_orders_txt.text

    # take the no item sentance
    def no_items_in_cart_prove(self):
        empty_txt = self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-bold ng-scope']")
        return empty_txt.text
