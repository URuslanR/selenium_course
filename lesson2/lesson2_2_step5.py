from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

browser.get(link)
browser.execute_script("return arguments[0].scrollIntoView(true);")
button = browser.find_element(By.TAG_NAME, "button")
button.click()