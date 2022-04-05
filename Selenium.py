# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:07:58 2021

@author: victo
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

nav = webdriver.Chrome(r'C:\Users\victo\OneDrive\Área de Trabalho/chromedriver')
nav.get('https://www.google.com/search?q=a&sxsrf=ALeKk03x8Zva9tUIuo7PC7zlp3JaVcU6Wg:1622941106516&source=lnms&tbm=shop&sa=X&ved=2ahUKEwiqnZTh5oHxAhX3q5UCHd9KBK0Q_AUoAHoECAEQCg&biw=1366&bih=625')
print(nav)
itens ={'Arroz', 'Feijão', 'Tomate', 'TV', 'Computador'}
pageInfo = []
for iten in itens:

    a = nav.find_element_by_name('q')
    a.clear()
    a.send_keys(iten)
    a.submit()
    
    resultado = nav.find_elements_by_class_name('sh-dlr__list-result')
    
    titulo = (nav.find_elements_by_xpath("//div[@class='sh-dlr__list-result']/div[@class='sh-dlr__content xal5Id']/div[@class='ZGFjDb']/div[1]/div[1]"))
    
    descrição = (nav.find_elements_by_xpath("//div[@class='sh-dlr__list-result']/div[@class='sh-dlr__content xal5Id']/div[@class='ZGFjDb']/div[1]/div[2]"))
    
    
    preço = (nav.find_elements_by_xpath("//div[@class='sh-dlr__list-result']/div[@class='sh-dlr__content xal5Id']/div[@class='ZGFjDb']/div[@class='m31woc']/div[1]/div[1]/a/div[1]/div[2]"))
    local = (nav.find_elements_by_xpath("//div[@class='sh-dlr__list-result']/div[@class='sh-dlr__content xal5Id']/div[@class='ZGFjDb']/div[@class='m31woc']/div[1]/div[1]/a/div[1]/div[3]"))
    saida=0
    
    
    
    
    for result in resultado:
        element = result.find_element_by_css_selector('a') 
        link = element.get_attribute('href')
        
       
              
        pageInfo.append({ 'tipo': iten,
          'link' : link, 'título' : titulo[saida].text, 
          'descrição': descrição[saida].text, 
          'preço': preço[saida].text, 'local': local[saida].text
          
        })
        saida+=1

data = pd.DataFrame(pageInfo)
data.to_csv('dadosGoogle.csv', sep=',', index=None)