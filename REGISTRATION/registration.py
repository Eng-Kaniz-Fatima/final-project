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


def registration_valid():
    logging.info('Registration_valid Execution Start....')
    # step 1: Launch Browser
    driver = webdriver.Chrome()
    logging.info('Chrome Launch successful')
    driver.maximize_window()

    # step 2: Open URL
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    time.sleep(3)
    logging.info('Registration page open successful')

    # step 3: Enter First Name
    firstname_field = driver.find_element(By.NAME, "firstname")
    firstname_field.clear()
    firstname_field.send_keys("Kaniz")
    logging.info('Enter First Name successful')

    # step 4: Enter Last Name
    lastname_field = driver.find_element(By.NAME, "lastname")
    lastname_field.clear()
    lastname_field.send_keys("Fatima")
    logging.info('Enter Last Name successful')

    # step 5: Enter Email
    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys("KanizFatima@gmail.com")
    logging.info('Enter Email successful')

    # step 6: Enter Telephone
    telephone_field = driver.find_element(By.NAME, "telephone")
    telephone_field.clear()
    telephone_field.send_keys("0123456789")
    logging.info('Enter Telephone successful')

    # step 7: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("KanizFatima")
    logging.info('Enter Password successful')

    # step 8: Enter Password Confirm
    password_confirm_field = driver.find_element(By.NAME, "confirm")
    password_confirm_field.clear()
    password_confirm_field.send_keys("KanizFatima")
    logging.info('Enter Password Confirm successful')

    #step 9: Click Privacy Policy
    privacy_policy = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    privacy_policy.click()
    logging.info('Privacy Policy clicked successful')

    # step 10: Click Continue Button
    continue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    continue_button.click()
    logging.info('Continue button clicked successful')
    time.sleep(5)

    # Capture Screenshot
    driver.get_screenshot_as_file("H:\Python project\Selenium WebDriver\PythonProject\\registrationTest.png")

    driver.close()
    logging.info('registration_valid Execution completed..')


def registration_invalid():
    logging.info('Registration_invalid Execution Start....')
    # step 1: Launch Browser
    driver = webdriver.Chrome()
    logging.info('Chrome Launch successful')
    driver.maximize_window()

    # step 2: Open URL
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    time.sleep(3)
    logging.info('Registration page open successful')

    # step 3: Enter First Name
    firstname_field = driver.find_element(By.NAME, "firstname")
    firstname_field.clear()
    firstname_field.send_keys("Kaniz123")
    logging.info('Enter First Name successful')

    # step 4: Enter Last Name
    lastname_field = driver.find_element(By.NAME, "lastname")
    lastname_field.clear()
    lastname_field.send_keys("Fatima123")
    logging.info('Enter Last Name successful')

    # step 5: Enter Email
    email_field = driver.find_element(By.NAME, "email")
    email_field.clear()
    email_field.send_keys("KanizFatima123@gmail.com")
    logging.info('Enter Email successful')

    # step 6: Enter Telephone
    telephone_field = driver.find_element(By.NAME, "telephone")
    telephone_field.clear()
    telephone_field.send_keys("0123456789000")
    logging.info('Enter Telephone successful')

    # step 7: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("KanizFatima123")
    logging.info('Enter Password successful')

    # step 8: Enter Password Confirm
    password_confirm_field = driver.find_element(By.NAME, "confirm")
    password_confirm_field.clear()
    password_confirm_field.send_keys("KanizFatima123")
    logging.info('Enter Password Confirm successful')

    # step 9: Click Privacy Policy
    privacy_policy = driver.find_element(By.CSS_SELECTOR, "[type='checkbox']")
    privacy_policy.click()
    logging.info('Privacy Policy clicked successful')

    # step 10: Click Continue Button
    continue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    continue_button.click()
    time.sleep(5)
    logging.info('Continue button clicked successful')

    # verify registration or not by check error message
    error_message = driver.find_element(By.CSS_SELECTOR,".alert-dismissible")
    actual_error_message_text = error_message.text

    expected_error_message = "Warning: E-Mail Address is already registered!"

    if expected_error_message == actual_error_message_text:
        logging.info("Test passed. Registration failed.Error message: " + expected_error_message)
    else:
        logging.info("Test Failed. Did not get expected error message: " + expected_error_message)

    driver.close()
    logging.info('registration_invalid Execution completed..')

registration_valid()
registration_invalid()
