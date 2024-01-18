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

def Test_Case_valid():
    logging.info('Test_Case_valid Execution Start....')
    # step 1: Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 2: Open URL
    driver.get("https://automationexercise.com/")
    time.sleep(3)

    # step 3:  Click on 'Test Cases' button
    TestCases_button = driver.find_element(By.CSS_SELECTOR, ".navbar-nav [href='\/test_cases']")
    TestCases_button.click()
    logging.info('Test Cases button clicked successful')

    # verify Test Cases or not
    expected_url = "https://automationexercise.com/test_cases"
    actual_url = driver.current_url

    if expected_url == actual_url:

        logging.info('Test passed. Test Cases successful')

    else:
        logging.info('Test Failed. Test Cases failed.')

    # Capture Screenshot
    driver.get_screenshot_as_file("H:\Python project\Selenium WebDriver\PythonProject\\Verify_Test_Pages.png")

    time.sleep(5)
    driver.close()

Test_Case_valid()