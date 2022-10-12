from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = "https://cv.senla.eu/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys('anna_sidorova')
    input2 = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
    input2.send_keys('To3AhCh3vi')
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    
    # 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
  #  пустая строка в конце файла
