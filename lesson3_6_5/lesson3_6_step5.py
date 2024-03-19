from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

answer = math.log(int(time.time()))

@pytest.mark.parametrize('Nomber', ["895","896"])
def test_time_link(browser, Nomber):
    link = f"https://stepik.org/lesson/236{Nomber}/step/1"
    browser.get(link)

    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit_submission"))
      )
    button.click()
    
    browser.find_element(By.CLASS_NAME, "button_with-loader").click()    
        
finally:
    time.sleep(15)
    browser.quit()
    
#,"896","896","896","896","896","896"