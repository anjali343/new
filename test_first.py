import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, "email").send_keys("Hello_test@gmail.com")
driver.find_element(By.ID, "pass").send_keys("abc")
driver.find_element(By.NAME, "login").click()
time.sleep(2)
msg = driver.find_element(By.CLASS_NAME, '_9ay7').text
print(msg)
assert "The email address you entered isn't connected to an account." in msg
