from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestUnittest(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CLASS_NAME, 'first[required]')
        input1.send_keys("Ruslan")
        input2 = browser.find_element(By.CLASS_NAME, 'second[required]')
        input2.send_keys("Yusupov")
        input3 = browser.find_element(By.CLASS_NAME, "third[required]")
        input3.send_keys("myemail@mail.ru")
    
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        # self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        input1 = browser.find_element(By.CLASS_NAME, 'first[required]')
        input1.send_keys("Ruslan")
        input2 = browser.find_element(By.CLASS_NAME, 'second[required]')
        input2.send_keys("Yusupov")
        input3 = browser.find_element(By.CLASS_NAME, "third[required]")
        input3.send_keys("myemail@mail.ru")
    
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)
        #self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла