from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Chrome()
browser.get('https://www.chitai-gorod.ru/')

button=browser.find_element(by=By.CLASS_NAME, value='js__showPopupLogin')
button.click()

login=browser.find_element(by=By.NAME, value='login')
login.send_keys('<логин>')

password=browser.find_element(by=By.NAME, value='password')
password.send_keys('<пароль>')

button=browser.find_element(by=By.ID, value='authSubmit')
button.click()

browser.get('https://www.chitai-gorod.ru/profile/')

try:
    assert '<Имя пользователя>' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
browser.close()