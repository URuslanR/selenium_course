from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import math

#def calc(answer):
#    return math.log(int(time.time()))

@pytest.mark.parametrize('Nomber', ["895"])
def test_time_link(browser, Nomber):
    link = f"https://stepik.org/lesson/236{Nomber}/step/1"
    browser.get(link)

    link_login = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.ID, "ember416"))
      )
    link_login.click()
    
    browser.find_element(By.ID, "id_login_email").send_keys("u.ruslan@bk.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("6xGPxL")
    
    browser.find_element(By.CLASS_NAME, "button_with-loader").click()    

    textarea = WebDriverWait(browser, 30).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'textarea'))
      )
    print("Privet")  
    textarea.send_keys(math.log(int(time.time())))
    time.sleep(1)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
      )
    button.click()
    
    fitbeck = WebDriverWait(browser, 40).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint'))
      )
      
    print(fitbeck.text)
    time.sleep(15)

    
#,"896","896","896","896","896","896"