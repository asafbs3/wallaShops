from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def close_popup(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            close_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/button/svg/path")))
            close_button.click()
        except:
            pass
        
    def open_product_page(self):
        #wait for page to load completley
        wait = WebDriverWait(self.driver,5)
        ProductPage.close_popup(self.driver)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container_items.gallery_items_inner")))
        #click on product
        link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container_items.gallery_items_inner a")))
        self.driver.get(link.get_attribute("href"))
        return True

    def add_to_cart(self):
        wait = WebDriverWait(self.driver,5)
        ProductPage.close_popup(self.driver)
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product_butts_pay .add_to_cart")))
        add_to_cart_button.click()
        return True

    def verify_product_added_to_cart(self):
        wait = WebDriverWait(self.driver, 5)
        ProductPage.close_popup(self.driver)
        #locate the cart element
        cart_items_span = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cart_main .cart_div .title span")))
        #retrive the dynamicly update text
        cart_text = cart_items_span.text.strip()

        #checked for updated cart content
        return "0 פריטים" not in cart_text #true if items not in cart