from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.wallashops.co.il/")

#click on some product
#wait for container to load
wait = WebDriverWait(driver, 5)
container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".container_items.gallery_items_inner")))

# Find the <a> tag inside the container and get the href attribute
link = container.find_element(By.CSS_SELECTOR, "a")
driver.get("https://www.wallashops.co.il" + link.get_dom_attribute("href"))

#click on add to cart
wait = WebDriverWait(driver, 5)
button = driver.find_element(By.CLASS_NAME, "add_to_cart")
button.click()
print("success")