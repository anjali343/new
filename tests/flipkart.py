from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://flipkart.com")
driver.maximize_window()

driver.implicitly_wait(5)
driver.get("https://www.flipkart.com")

ele = driver.find_elements(By.TAG_NAME, "a")
print(len(ele))
for i in ele:
    print(i.text)
    print(i.get_attribute("href"))
