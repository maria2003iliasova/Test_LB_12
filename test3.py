from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('https://www.chitai-gorod.ru/')

q=browser.find_element(by=By.NAME, value='q')
q.send_keys('Дни нашей жизни')

button=browser.find_element(by=By.CLASS_NAME, value='search-form__btn')
button.click()

try:
    assert 'Результаты поиска «Дни нашей жизни»' in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
browser.close()