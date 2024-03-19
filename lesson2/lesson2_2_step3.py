from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

def calc(num1, num2):
    return str(int(num1) + int(num2)) 

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, "num1").text
    num1 = x1.text
    x2 = browser.find_element(by.ID, "num2").text
    num2 = x2.text
    
    suma = calc(num1, num2)
    
    browser.find_element(By.TAG_NAME, "select").Click()
    browser.find_element(By.CSS_SELECTOR, "[value=suma]").Click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()        
    
#    input1 = browser.find_element(By.ID, "answer")
 #   input1.send_keys(y)
    
#    option1 = browser.find_element(By.ID, "robotCheckbox")
#    option1.click()
    
#    option2 = browser.find_element(By.ID, "robotsRule")
#    option2.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла