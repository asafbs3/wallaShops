from selenium import webdriver
from pages.product_page import ProductPage
import time

def test_wallaShops():
    #create a new chrome instance
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.wallashops.co.il/")

    #wait for 4 seconds for page to load
    time.sleep(4)

    #create a new productPage instance
    product_page = ProductPage(driver)

    #open the product_page
    assert product_page.open_product_page()
    print("open product page pass")

    #add pdoduct to cart
    assert product_page.add_to_cart()
    print("Add to cart Passed")

    #verify that the product is added to cart
    assert product_page.verify_product_added_to_cart()
    print("verify add to cart pass")

    #quit the browser
    driver.quit()
    print("ALL TESTS PASSED")

test_wallaShops()