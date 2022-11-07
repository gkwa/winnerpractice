import os
import time

import selenium
import selenium.webdriver.common.by

USERNAME = os.getenv("USERNAME", None)
PASSWORD = os.getenv("PASSWORD", None)

if not USERNAME:
    raise ValueError("USERNAME not set")

if not PASSWORD:
    raise ValueError("PASSWORD not set")

chrome_options = selenium.webdriver.ChromeOptions()

driver = selenium.webdriver.Remote(
    command_executor="http://localhost:4444", options=chrome_options
)

driver.get("https://my.ultramobile.com/account/summary")

xpath = "//input[@placeholder='Username or Phone Number']"
element = driver.find_element(selenium.webdriver.common.by.By.XPATH, xpath)
element.send_keys(USERNAME)

xpath = "//input[@placeholder='Password']"
element = driver.find_element(selenium.webdriver.common.by.By.XPATH, xpath)
element.send_keys(PASSWORD)

xpath = "//button[text()='Sign in']"
element = driver.find_element(selenium.webdriver.common.by.By.XPATH, xpath)

element.click()

# wait for data to load
time.sleep(10)

xpath = "//div[contains(text(), 'Remaining Data')]"
element = driver.find_element(selenium.webdriver.common.by.By.XPATH, xpath)

xpath = ".."
element = element.find_element(selenium.webdriver.common.by.By.XPATH, xpath)
print(element.text)

time.sleep(10)
driver.quit()
