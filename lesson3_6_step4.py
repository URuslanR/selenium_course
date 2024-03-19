from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link_login = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember416"))
      )
    link_login.click()
    browser.find_element(By.ID, "id_login_email").send_keys("u.ruslan@bk.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("6xGPxL")
    
    browser.find_element(By.CLASS_NAME, "button_with-loader").click()    
        
finally:
    browser.quit()
    

    