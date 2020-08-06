from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

browser = webdriver.Firefox(options=options)
browser.get("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm")

select = Select(browser.find_element_by_name('UF'))
select.select_by_value('SC')

btn = browser.find_element_by_class_name('btnform').find_element_by_tag_name('input')
btn.click()

# time.sleep(5) 

test = browser.find_element_by_class_name('ctrlcontent')

print(test.text)