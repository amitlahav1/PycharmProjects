from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Home_Page import Home_Page
from Category_Page import Category_Page
from Product_Page import Product_Page
from ShoppingCard_Page import ShoppingCard_Page
from Checkout_Page import Checkout_Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from time import sleep


class TestProduct_Page(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        # Open browser (create a driver object)
        self.driver = webdriver.Chrome(service=service_chrome)

        # Go to the required URL
        self.driver.get("https://advantageonlineshopping.com/#/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        # create object
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.shopping_cart_page = ShoppingCard_Page(self.driver)
        self.checkout_page = Checkout_Page(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def test_1_correct_final_quantity(self):

        # add first product to cart
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        qty1 = '2'
        self.product_page.input_quantity(qty1)
        self.product_page.click_add_cart()
        # add another product
        self.home_page.click_website_logo()
        self.home_page.click_laptops()
        self.category_page.choose_product(1)
        qty2 = '4'
        self.product_page.input_quantity(qty2)
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        # check if the qty is equal between the total item in icon cart to the sum of qty .
        self.assertEqual(self.home_page.total_products_icon_cart(), self.home_page.total_products_title())

        # check if the QTY is equal between the qty that we put ,to total qty item in icon cart.
        qty1 = int(qty1)
        qty2 = int(qty2)
        self.assertEqual((qty2 + qty1), self.home_page.total_products_title())

    def test_2_true_details_icon_cart(self):
        # add first product to cart
        self.home_page.click_speakers()
        self.category_page.choose_product(1)
        qty_product3 = '4'
        price_product3 = self.product_page.price_product_float()
        self.product_page.choose_color_click(2)
        color_product_3 = self.product_page.name_color(2)
        name_product3 = self.product_page.name_product()
        if len(name_product3) > 27:
            name_product3 = name_product3[:27]
        self.product_page.input_quantity(qty_product3)
        self.product_page.click_add_cart()

        # add another product
        self.home_page.click_website_logo()
        self.home_page.click_tablets()
        self.category_page.choose_product(1)
        qty_product2 = '6'
        price_product_2 = self.product_page.price_product_float()
        self.product_page.choose_color_click(1)
        color_product_2 = self.product_page.name_color(1)
        name_product_2 = self.product_page.name_product()
        if len(name_product_2) > 27:
            name_product_2 = name_product_2[:27]
        self.product_page.input_quantity(qty_product2)
        self.product_page.click_add_cart()

        # add the last product
        self.home_page.click_website_logo()
        self.home_page.click_mice()
        self.category_page.choose_product(3)
        qty_product1 = '2'
        price_product1 = self.product_page.price_product_float()
        self.product_page.choose_color_click(3)
        color_product_1 = self.product_page.name_color(3)
        name_product_1 = self.product_page.name_product()
        if len(name_product_1) > 27:
            name_product_1 = name_product_1[:27]
        self.product_page.input_quantity(qty_product1)
        self.product_page.click_add_cart()

        # get names from icon cart. if len > 27 then we take the 27 first letters.
        # (Because in icon cart there are 27 first letters of the product)
        name_product_1_icon = self.home_page.name_product_icon_cart(1)
        if len(name_product_1_icon) > 27:
            name_product_1_icon = name_product_1_icon[:27]

        name_product_2_icon = self.home_page.name_product_icon_cart(2)
        if len(name_product_2_icon) > 27:
            name_product_2_icon = name_product_2_icon[:27]

        name_product_3_icon = self.home_page.name_product_icon_cart(3)
        if len(name_product_3_icon) > 27:
            name_product_3_icon = name_product_3_icon[:27]

        # test to name of product. need to be equal between product page to icon cart

        self.assertEqual(name_product_1_icon, name_product_1)
        self.assertEqual(name_product_2_icon, name_product_2)
        self.assertEqual(name_product_3_icon, name_product3)

        self.home_page.hover_icon_cart()
        # test to price. need to be equal between product page to icon cart
        qty_product1 = int(qty_product1)
        qty_product2 = int(qty_product2)
        qty_product3 = int(qty_product3)

        self.assertEqual((price_product1 * qty_product1), self.home_page.price_of_product_icon_cart(1))
        self.assertEqual((price_product_2 * qty_product2), self.home_page.price_of_product_icon_cart(2))
        self.assertEqual((price_product3 * qty_product3), self.home_page.price_of_product_icon_cart(3))

        # test to color. need to be equal between product page to icon cart
        self.assertEqual(color_product_1, self.home_page.color_product_icon_cart(1))
        self.assertEqual(color_product_2, self.home_page.color_product_icon_cart(2))
        self.assertEqual(color_product_3, self.home_page.color_product_icon_cart(3))

        # test to qty. need to be equal between product page to icon cart
        self.assertEqual(qty_product1, self.home_page.qty_of_product_icon_cart(1))
        self.assertEqual(qty_product2, self.home_page.qty_of_product_icon_cart(2))
        self.assertEqual(qty_product3, self.home_page.qty_of_product_icon_cart(3))

    def test_3_remove_product_from_icon_cart(self):
        # add first product to cart
        self.home_page.click_speakers()
        self.category_page.choose_product(1)
        name_product_2 = self.product_page.name_product()
        if len(name_product_2) > 27:
            name_product_2 = name_product_2[:27]
        self.product_page.click_add_cart()

        # add another product
        self.home_page.click_website_logo()
        self.home_page.click_speakers()
        self.category_page.choose_product(3)
        name_product = self.product_page.name_product()
        if len(name_product) > 27:
            name_product = name_product[:27]
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        # the len of the list products before remove item
        len_before_remove = self.home_page.len_list_products_at_icon_cart()

        # check if the product added according to his name .
        #if len > 27 then we take the 27 first letters.
        # (Because in icon cart there are 27 first letters of the product)

        product_name_icon_cart_1 = self.home_page.name_product_icon_cart(1)
        if len(product_name_icon_cart_1) > 27:
            product_name_icon_cart_1 = product_name_icon_cart_1[:27]

        self.assertEqual(name_product, product_name_icon_cart_1)

        # remove item ,  and check the len of products in icon cart.
        self.home_page.remove_product_icon_cart(1)
        self.assertNotEqual(len_before_remove, self.home_page.len_list_products_at_icon_cart())

        # check that the name of the product in icon cart is "name_product_2" that prove the product has remove.
        product_name_icon_cart_2 = self.home_page.name_product_icon_cart(1)
        if len(product_name_icon_cart_2) > 27:
            product_name_icon_cart_2 = product_name_icon_cart_2[:27]

        self.assertEqual(name_product_2, product_name_icon_cart_2)

    def test_4_go_shopping_cart_page(self):
        # add product to cart
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        self.product_page.click_add_cart()
        self.home_page.hover_icon_cart()
        #go to shopping cart page
        self.home_page.click_cart_icon()
        # if have the text "SHOPPING CART", and the element -  that we in correctly page (shopping cart)
        self.assertEqual(self.shopping_cart_page.shopping_card_text(), "SHOPPING CART")

    def test_5_total_price_and_qty_true(self):
        # add first product to cart
        self.home_page.click_speakers()
        self.category_page.choose_product(2)
        qty_product3 = '2'
        price_product3 = self.product_page.price_product_float()
        self.product_page.input_quantity(qty_product3)
        self.product_page.click_add_cart()

        # add another product
        self.home_page.click_website_logo()
        self.home_page.click_speakers()
        self.category_page.choose_product(1)
        qty_product2 = '3'
        price_product_2 = self.product_page.price_product_float()
        self.product_page.input_quantity(qty_product2)
        self.product_page.click_add_cart()

        # add the last product
        self.home_page.click_website_logo()
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        qty_product1 = '4'
        price_product1 = self.product_page.price_product_float()
        self.product_page.input_quantity(qty_product1)
        self.product_page.click_add_cart()

        # go to shopping cart page:
        self.home_page.click_cart_icon()
        # check that the qty we put in product page is equal to shopping cart page:
        qty_product1 = int(qty_product1)
        qty_product2 = int(qty_product2)
        qty_product3 = int(qty_product3)
        # product 1 in shopping cart:
        self.assertEqual(qty_product1, self.shopping_cart_page.qty_first_product_shipping_page())
        # product 2 in shopping cart:
        self.assertEqual(qty_product2, self.shopping_cart_page.qty_second_product_shipping_page())
        # product 3 in shopping cart:
        self.assertEqual(qty_product3, self.shopping_cart_page.qty_third_product_shipping_page())

        # check total price between product page to shopping cart .  product 1:
        self.assertEqual(self.shopping_cart_page.price_product(1), (qty_product1 * price_product1))
        # check total price between product page to shopping cart .  product 2:
        self.assertEqual(self.shopping_cart_page.price_product(2), (qty_product2 * price_product_2))
        # check total price between product page to shopping cart .  product 3:
        self.assertEqual(self.shopping_cart_page.price_product(3), (qty_product3 * price_product3))
        print(f"\nall the products in cart:\nproduct 1:\nNAME: {self.shopping_cart_page.name_product(1)}\nQTY:"
              f" {self.shopping_cart_page.qty_first_product_shipping_page()}\nPRICE: ${self.shopping_cart_page.price_product(1)}\n\nproduct 2:"
              f"\nNAME: {self.shopping_cart_page.name_product(2)}\nQTY: {self.shopping_cart_page.qty_second_product_shipping_page()}\n"
              f"PRICE: ${self.shopping_cart_page.price_product(2)}\n\nproduct 3:\nNAME: {self.shopping_cart_page.name_product(3)}\n"
              f"QTY: {self.shopping_cart_page.qty_third_product_shipping_page()}\nPRICE: ${self.shopping_cart_page.price_product(3)} ")

    def test_6_edit_QTY_for_2_product_in_ShoppingCart(self):
        # add product to cart
        self.home_page.click_mice()
        self.category_page.choose_product(2)
        self.product_page.input_quantity('3')
        self.product_page.click_add_cart()

        # add another product
        self.home_page.click_website_logo()
        self.home_page.click_speakers()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('2')
        self.product_page.click_add_cart()

        # go to shopping cart page
        self.home_page.hover_icon_cart()
        self.home_page.click_cart_icon()
        # edit first product (QTY) , from QTY: 2 to QTY: 4
        self.shopping_cart_page.click_edit_product(1)
        qty_product1 = '4'
        self.product_page.input_quantity(qty_product1)
        self.product_page.click_add_cart()
        qty_product1 = int(qty_product1)
        # test to the first product. the qty need to be equal to the edit change
        self.assertEqual(qty_product1, self.shopping_cart_page.qty_first_product_shipping_page())

        # edit the QTY of second product, from QTY: 3 TO QTY: 5
        qty_product2 = '5'
        self.home_page.click_cart_icon()
        self.shopping_cart_page.click_edit_product(2)
        self.product_page.input_quantity(qty_product2)
        self.product_page.click_add_cart()
        self.home_page.click_cart_icon()
        qty_product2 = int(qty_product2)

        # test to the second product. the qty need to be equal to the edit change.
        self.assertEqual(qty_product2, self.shopping_cart_page.qty_second_product_shipping_page())
        # end test to first product. the qty need to stay equal after changes in second product
        self.assertEqual(qty_product1, self.shopping_cart_page.qty_first_product_shipping_page())

    ######## have bug : When you edit the quantity of the second product, it changes the quantity for the first product  ######

    def test_7_back_from_TABLET(self):
        # add product to cart from tablet category
        self.home_page.click_tablets()
        self.category_page.choose_product(1)
        self.product_page.click_add_cart()
        # back to tablet category
        self.driver.back()
        # check if the category tablet was open
        self.assertEqual(self.category_page.name_category(), "TABLETS")
        # back to home page
        self.driver.back()
        # check if the home page was open
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[style='display: block; opacity: 1;']")))
        self.assertEqual(self.home_page.contact_us_text(), "CONTACT US")

    def test_8_orders_after_payment_safepay_registrtion(self):
        # add prodoucts to cart
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('2')
        self.product_page.click_add_cart()
        self.home_page.click_cart_icon()
        self.shopping_cart_page.click_checkout()
        # create new user
        self.checkout_page.click_registration()
        self.home_page.regist_un('Pofffo91122')
        self.home_page.regist_pass_word('Pofffo91322')
        self.home_page.confirm_password('Pofffo91322')
        self.home_page.send_email('thekinsck@gmail.com')
        self.checkout_page.scroll()
        self.home_page.create_radio_bottun()
        self.home_page.click_create_action()
        # go to acount orders to save the no orders prove
        self.home_page.user_icon_after_log_in_TG()
        self.checkout_page.user_my_orders_bottun_TG()
        self.checkout_page.user_my_acount_bottun_TG()
        list_product_before = self.checkout_page.list_table_order()
        # go to cheackout,and pay with safepay
        self.home_page.click_cart_icon()
        self.checkout_page.click_cahekout_in_cart()
        self.checkout_page.click_next()
        self.checkout_page.scroll()
        self.checkout_page.safepay_username_send_k("gol5ff6")
        self.checkout_page.safepay_password_send_k("'Took26'")
        self.checkout_page.pay_now_btn_SAFEPAY()
        # כנראה שיש בעיה שלא קשורה לקוד , יש סליפ למרות שיש גם וויט לייד הפקודות האלו
        sleep(5)
        self.home_page.user_icon_after_log_in_TG()
        # כנראה שיש בעיה שלא קשורה לקוד , יש סליפ למרות שיש גם וויט לייד הפקודות האלו
        sleep(5)

        # go to my orders page , take the prove of 1 order and compare with no orders
        self.checkout_page.user_my_orders_bottun_TG()
        self.assertNotEqual(self.checkout_page.no_orders_prove(), "- No orders -")
        # go to my cart , and prove the cart is empty
        self.home_page.wait_cart_icon()
        # כנראה שיש בעיה שלא קשורה לקוד , יש סליפ למרות שיש גם וויט לייד הפקודות האלו
        sleep(5)
        self.checkout_page.empty_cart_prove_txt()
        self.assertEqual(self.checkout_page.no_items_in_cart_prove(), "Your shopping cart is empty")
        self.home_page.click_website_logo()
        # כנראה שיש בעיה שלא קשורה לקוד , יש סליפ למרות שיש גם וויט לייד הפקודות האלו
        sleep(7)
        # delate the acount
        self.home_page.user_icon_after_log_in_TG()
        self.checkout_page.user_my_acount_bottun_TG()
        self.checkout_page.delete_my_account_tg()
        self.checkout_page.yes_delete_my_account_tg()


    def test_9_pay_with_credit_cart_new_orders_empty_cart(self):
        # add products to cart
        self.home_page.click_mice()
        self.category_page.choose_product(1)
        self.product_page.input_quantity('2')
        self.product_page.click_add_cart()
        self.home_page.click_cart_icon()
        self.shopping_cart_page.click_checkout()

        # create a new account
        self.checkout_page.click_registration()
        self.home_page.regist_un('hfcccT331512')
        self.home_page.regist_pass_word('hfcccT331512')
        self.home_page.confirm_password('hfcccT331512')
        self.home_page.send_email('thekinsck@gmail.com')
        self.checkout_page.scroll()
        self.home_page.create_radio_bottun()
        self.home_page.click_create_action()

        # going to my account , and edit payment deatils
        self.home_page.user_icon_after_log_in_TG()
        self.checkout_page.user_my_acount_bottun_TG()
        self.home_page.acount_edit_details()
        self.home_page.acount_edit_details_radio()
        self.home_page.send_cc_keys('456778888777')
        self.home_page.send_ccv_keys('455')
        self.home_page.send_c_holder_keys('tgf gold')
        self.home_page.send_mm()
        self.home_page.send_yyyy()
        self.home_page.save()

        sleep(5)

        # pay with credit card
        self.home_page.click_cart_icon()
        self.checkout_page.click_cahekout_in_cart()
        self.checkout_page.click_next()
        self.checkout_page.click_radio_creditcard()
        self.home_page.pay_now_master()
        sleep(3)

        # going to my orders and take the seantnce _no orders_
        self.home_page.user_icon_after_log_in_TG()
        self.checkout_page.user_my_orders_bottun_TG()

        # make sure that the - no orders - is no longer exsist
        self.assertNotEqual(self.checkout_page.no_orders_prove(), "- No orders -")
        self.home_page.click_website_logo()
        self.home_page.click_cart_icon()

        # take the "Your shopping cart is empty" from cart
        self.checkout_page.empty_cart_prove_txt()

        # cheack "Your shopping cart is empty" from cart is in the cart and true
        self.assertTrue(self.checkout_page.no_items_in_cart_prove(), "Your shopping cart is empty")

        # delate the acount
        self.home_page.click_website_logo()
        self.home_page.user_icon_after_log_in_TG()
        self.checkout_page.user_my_acount_bottun_TG()
        self.checkout_page.delete_my_account_tg()
        self.checkout_page.yes_delete_my_account_tg()

        # # //////////////////////////////////////////////////////////////////////////////////////////////////////////////
        # self.home_page.click_mice()
        # self.category_page.choose_product(1)
        # self.product_page.input_quantity('2')
        # self.product_page.click_add_cart()
        # self.home_page.click_cart_icon()
        # self.shopping_cart_page.click_checkout()
        # self.home_page.click_user_logo()
        # self.home_page.input_user_name('gold123')
        # self.home_page.input_password('Gold123')
        # self.home_page.click_sign_in()
        # self.home_page.user_icon_after_log_in_TG()
        # sleep(7)
        # self.checkout_page.user_my_orders_bottun_TG()
        # self.checkout_page.user_my_acount_bottun_TG()
        # list_product_before = self.checkout_page.list_table_order()
        # print(f"{list_product_before} the first len")
        # self.home_page.click_cart_icon()
        # self.checkout_page.click_cahekout_in_cart()
        # self.home_page.click_cart_icon()
        # self.checkout_page.click_cahekout_in_cart()
        # self.checkout_page.click_next()
        # self.checkout_page.click_radio_creditcard()
        # self.checkout_page.pay_now_btn_MasterCredit_01()
        # sleep(10)
        # self.home_page.user_icon_after_log_in_TG()
        # self.checkout_page.user_my_orders_bottun_TG()
        # list_product_after = self.checkout_page.list_table_order()
        # print(f"{list_product_after}the secound len")
        # self.assertTrue(list_product_before > list_product_after)
        # self.home_page.click_cart_icon()
        # self.checkout_page.empty_cart_prove_txt()
        # self.assertEqual(self.checkout_page.empty_cart_prove_len(), len(self.checkout_page.empty_cart_prove_txt()))

    def test_10_check_logOut_login(self):
        username = 'gold123'
        password = 'Gold123'

        # log in to acount
        self.home_page.click_user_logo()
        self.home_page.input_user_name(username)
        self.home_page.input_password(password)
        self.home_page.click_sign_in()

        # compare txt next to icon user to username
        self.assertEqual(self.home_page.name_next_to_icon(), username)
        self.home_page.user_icon_after_log_in_TG()
        self.home_page.user_log_out_bottun_TG()

        # make sure there is no name next to acount icon after log out
        self.assertNotEqual(self.home_page.name_next_to_icon(), "")


