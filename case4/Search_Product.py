import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

# configure logging settings
logging.basicConfig(filename="test_log.log", level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')

def capture_screenshot(driver,screenshot_name):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    file_path = f"screenshots/{screenshot_name}_{timestamp}.png"
    driver.get_screenshot_as_file(file_path)
    logging.info(f"Screeenshot saved to: {file_path}")

def Search_Product_valid():
    logging.info('Search_Product_valid Execution Start....')
    # step 1: Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 2: Open URL
    driver.get("https://automationexercise.com/")
    time.sleep(3)

    # step 3:  Click on Search Product button
    Search_Product_button = driver.find_element(By.CSS_SELECTOR, "[href='\/products']")
    Search_Product_button.click()
    logging.info('Search Product button clicked successful')

    # verify Search Product or not
    expected_url = "https://automationexercise.com/products"
    actual_url = driver.current_url

    if expected_url == actual_url:

        logging.info('Test passed. Search Product successful')

    else:
        logging.info('Test Failed. Search Product failed.')

    # step 4: Enter search product
    searchproduct_field = driver.find_element(By.NAME, "search")
    searchproduct_field.clear()
    searchproduct_field.send_keys("WOMEN")
    logging.info('Enter search product successful')

    # step 5:  Click on Search button
    Search_button = driver.find_element(By.CSS_SELECTOR, ".fa-search")
    Search_button.click()
    logging.info('Search button clicked successful')

    # verify Search button or not
    expected_url = "https://automationexercise.com/products?search=WOMEN"
    actual_url = driver.current_url

    if expected_url == actual_url:

        logging.info('Test passed. Search button successful')

    else:
        logging.info('Test Failed. Search button failed.')

    # Capture Screenshot
    driver.get_screenshot_as_file("H:\Python project\Selenium WebDriver\PythonProject\\Search_Product.png")

    time.sleep(5)
    driver.close()

Search_Product_valid()