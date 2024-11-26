from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.product_page import ProductPage
import time

chrome_options = Options()
chrome_options.add_experimental_option('detach', True) #leave the browser open after the process ended
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.wallashops.co.il/")

#Initialize Page Objects
product_page = ProductPage(driver)

#Navigate to product page
product_page.open_product_page()
time.sleep(10)

#Add the product to the cart
product_page.add_to_cart()

#verify that the product is added to cart
product_page.verify_product_added_to_cart()

print("automation Passed")

