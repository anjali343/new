from selenium import webdriver



global driver
browser_name = input("Enter Browser name as 'chrome', 'medge', 'firefox'")
if browser_name == "chrome":
    driver = webdriver.Chrome()
elif browser_name == "firefox":
    driver = webdriver.Firefox()
elif browser_name == "IE":
    print("IE driver")

driver.get("https://in.ebay.com")
driver.maximize_window()
driver.implicitly_wait(5)




