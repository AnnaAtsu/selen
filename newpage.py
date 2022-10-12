from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    first_window = browser.window_handles[0]
    browser.get('http://suninjuly.github.io/redirect_page.html?')
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window) 
       
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()

finally:
    
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
  # не забываем оставить пустую строку в конце файла