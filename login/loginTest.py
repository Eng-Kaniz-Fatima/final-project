from selenium import webdriver

# jaunch browser

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

#open url
driver.get("https://www.google.com")

driver.close()