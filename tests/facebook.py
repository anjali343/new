from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("http://www.facebook.com")
driver.maximize_window()

current_url = driver.current_url

driver.implicitly_wait(5)

assert current_url == "https://www.facebook.com/"

ele = driver.find_element(By.XPATH, "//a[text() = 'Create new account']")
ele.click()

# wait = WebDriverWait(driver, 5)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[text() = "Sign Up"]')))
#actions = ActionChains(driver)
driver.find_element(By.XPATH, '//input[@name = "firstname"]').send_keys("Anja")
driver.find_element(By.XPATH, '//input[@name ="lastname"]').send_keys("Solan")
driver.find_element(By.XPATH, '//input[@name ="lastname"]').send_keys(Keys.BACK_SPACE)
driver.find_element(By.XPATH, "//input[@aria-label='Mobile number or email address'] ").send_keys("anjalisolanke@gmail.com")
driver.find_element(By.ID, "password_step_input").send_keys("Abcxyz@5678")

select = Select(driver.find_element(By.NAME, "birthday_month"))
select.select_by_visible_text("May")
select = Select(driver.find_element(By.NAME, "birthday_day"))
select.select_by_visible_text("4")
select = Select(driver.find_element(By.NAME, "birthday_year"))
select.select_by_visible_text("2000")

driver.find_element(By.XPATH, "//span/label[text() = 'Female']").click()
driver.find_element(By.XPATH, '//button[@class = "_6j mvm _6wk _6wl _58mi _3ma _6o _6v" ]').click()

driver.close()
