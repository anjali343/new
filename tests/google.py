
#Write a script to open google.com and verify that title is Google and also verify that it is
# redirected to google.co.in

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")
driver.maximize_window()

title = driver.title
url = driver.current_url

assert title == "Google"
assert url == "https://www.google.co.in/"

driver.close()

