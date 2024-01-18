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

def login_valid():
    logging.info('login_valid Execution Start....')
    # step 1: Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 2: Open URL
    driver.get("https://apidog.com/?utm_source=google_search&utm_medium=d&utm_campaign=18544428894&utm_content=161306009430&utm_term=insomnia&gclid=Cj0KCQiAtaOtBhCwARIsAN_x-3JB3Anfqh0VPbo13ZcQgVZWhbqKlexj0wr9NfLS_V3LDym-JK9cmxYaAj85EALw_wcB")
    time.sleep(3)

    # step 3:  Click sign in button
    signin_button = driver.find_element(By.CSS_SELECTOR, "[class] li:nth-of-type(1) [target]")
    signin_button.click()
    logging.info('Sign in button clicked successful')
    time.sleep(5)

    # Capture Screenshot
    driver.get_screenshot_as_file("H:\Python project\Selenium WebDriver\PythonProject\\Login_valid.png")

    # step 4: Enter Email
    email_field = driver.find_element(By.NAME, "account")
    email_field.clear()
    email_field.send_keys("KanizFatima@gmail.com")
    logging.info('Enter Email successful')

    # step 5: Click continue with email
    continue_email_button = driver.find_element(By.CSS_SELECTOR,"[class='ui-btn ui-btn-primary ui-btn-lg ui-btn-block mb-2'] span")
    continue_email_button.click()
    logging.info('Continue email clicked successful')

    # step 6: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("123456789")
    logging.info('Enter Password successful')

    # step 7: Click continue with password
    continue_password_button = driver.find_element(By.CSS_SELECTOR,"[class='ui-btn ui-btn-primary ui-btn-lg ui-btn-block mb-2'] span")
    continue_password_button.click()
    logging.info('Continue password clicked successful')

    # Step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".apidog.com-login-button")
    login_button.click()
    time.sleep(5)
    logging.info('Login button clicked successful')
    # time.sleep(5)

    # verify login or not
    expected_url = "https://app.apidog.com/user/login"
    actual_url = driver.current_url

    if expected_url == actual_url:
        logging.info('Test passed. Login successful')
    else:
        logging.info('Test Failed. Login failed.')

    time.sleep(10)
    driver.close()
    logging.info('Login_valid Execution completed..')

def login_invalid():
    logging.info('login_invalid Execution Start....')
    # step 1: Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # step 2: Open URL
    driver.get("https://apidog.com/?utm_source=google_search&utm_medium=d&utm_campaign=18544428894&utm_content=161306009430&utm_term=insomnia&gclid=Cj0KCQiAtaOtBhCwARIsAN_x-3JB3Anfqh0VPbo13ZcQgVZWhbqKlexj0wr9NfLS_V3LDym-JK9cmxYaAj85EALw_wcB")
    time.sleep(3)

    # step 3:  Click sign in button
    signin_button = driver.find_element(By.CSS_SELECTOR, "[class] li:nth-of-type(1) [target]")
    signin_button.click()
    logging.info('Sign in button clicked successful')
    time.sleep(5)

    # Capture Screenshot
    driver.get_screenshot_as_file("H:\Python project\Selenium WebDriver\PythonProject\\Login_valid.png")

    # step 4: Enter Email
    email_field = driver.find_element(By.NAME, "account")
    email_field.clear()
    email_field.send_keys("KanizFatima@gmail123.com")
    logging.info('Enter Email successful')

    # step 5: Click continue with email
    continue_email_button = driver.find_element(By.CSS_SELECTOR,"[class='ui-btn ui-btn-primary ui-btn-lg ui-btn-block mb-2'] span")
    continue_email_button.click()
    logging.info('Continue email clicked successful')

    # step 6: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("123456789000")
    logging.info('Enter Password successful')

    # step 7: Click continue with password
    continue_password_button = driver.find_element(By.CSS_SELECTOR,"[class='ui-btn ui-btn-primary ui-btn-lg ui-btn-block mb-2'] span")
    continue_password_button.click()
    logging.info('Continue password clicked successful')

    # Step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, ".apidog.com-login-button")
    login_button.click()
    time.sleep(5)
    logging.info('Login button clicked Failed')
    # time.sleep(5)

    # verify login or not by check error message
    error_message = driver.find_element(By.CSS_SELECTOR, ".apidog-alert-content-text")
    actual_error_message_text = error_message.text

    expected_error_message = "Invalid credentials"

    if expected_error_message == actual_error_message_text:
        logging.info('Test Passed. Login failed.Error message: ' + expected_error_message)
    else:
        logging.info('Test Failed. Did not get expected error message: ' + expected_error_message)

    time.sleep(10)
    driver.close()
    logging.info('Login_invalid Execution completed..')


login_valid()
login_invalid()