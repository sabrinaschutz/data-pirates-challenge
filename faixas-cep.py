# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import json
import codecs

options = webdriver.FirefoxOptions()
options.add_argument('--headless')

browser = webdriver.Firefox(options=options)
browser.get("http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm")
browser.implicitly_wait(5)

def getUfs():
    select = Select(browser.find_element_by_name('UF'))
    optionsSelect = select.options
    ufs = []

    for i in range(1, len(optionsSelect)-1):
        ufs.append(optionsSelect[i].text)

    return ufs

def save(location, faixa):
    registry = {}
    registry['localidade'] = location
    registry['faixa-cep'] = faixa
    storage = codecs.open("faixas-cep.jsonl", "a", encoding='utf-8')
    json_data = json.dumps(registry, ensure_ascii=False)
    storage.write(json_data+"\n")
    storage.close()

def processLocations():
        while True:
            if len(browser.find_elements_by_xpath("//table")) > 1:
                rows = browser.find_elements_by_xpath("//table[2]/tbody/tr")
            else:
                rows = browser.find_elements_by_xpath("//table/tbody/tr")

            for row in range(2, len(rows)):
                location = rows[row].find_elements_by_tag_name('td')[0].text
                faixa = rows[row].find_elements_by_tag_name('td')[1].text
                print(location)
                save(location, faixa)
                
            try:
                nextLink = browser.find_element_by_link_text('[ Próxima ]')
            except NoSuchElementException:
                break

            nextLink.click()
            browser.implicitly_wait(5)

def processUf(uf):
    select = Select(browser.find_element_by_name('UF'))
    print("Iniciando processamento da UF: "+uf)
    select.select_by_value(uf)

    btn = browser.find_element_by_class_name('btnform').find_element_by_tag_name('input')
    btn.click()
    browser.implicitly_wait(5)

    processLocations()

print("Iniciando coleta de dados.")

open('faixas-cep.jsonl', 'w').close()

ufs = getUfs()
for index in range(0, len(ufs)-1):
    processUf(ufs[index])
    try:
        newSearch = browser.find_element_by_link_text('[ Nova Consulta ]')
    except NoSuchElementException:
        break 
    newSearch.click()
    browser.implicitly_wait(5)

print("Coleta de dados concluída com sucesso!")