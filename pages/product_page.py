from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select 

import time #sleep

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        
    def open_product_page(self):
        #wait for page to load completley
        wait = WebDriverWait(self.driver,5)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container_items.gallery_items_inner")))
        #click on product
        link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container_items.gallery_items_inner a")))
        self.driver.get(link.get_attribute("href"))
        return True

    def choose_option(self): 
        wait = WebDriverWait(self.driver, 2)
        try:
            select_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product_select_wrapper select[name=product_select]")))
            select = Select(select_element)
            select.select_by_index(1)
            return True
        except TimeoutError:
            return False
    
    def add_to_cart(self):
        wait = WebDriverWait(self.driver,5)
        #choose options if exist
        self.choose_option()
    
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product_butts_pay .add_to_cart")))
        add_to_cart_button.click()
        return True

    def verify_product_added_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        time.sleep(2)
        #locate the cart element
        cart_title_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cart_main .cart_div .title")))
        #retrive the dynamicly update text
        cart_text = self.driver.execute_script(
        "return document.querySelector('#cart_main .cart_div .title').innerText;"
    )
        return "0 פריטים" not in cart_text # true if items in cart