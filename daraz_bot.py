from ast import Break, Return
from functools import total_ordering
from webbrowser import Chrome
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import numpy as np
from selenium.webdriver.common.action_chains import ActionChains 


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.daraz.pk/")

search = driver.find_element_by_class_name("search-box__input--O34g")


products_list = pd.read_csv("Keyword analysis.csv")
df = products_list.values
df.tolist()

price = []
product_name = []
total_items_found = []

driver.get("https://www.daraz.pk/")

driver.maximize_window()
driver.minimize_window()

for x in df:
    search = driver.find_element_by_id("q")
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(Keys.DELETE)
    search_item = x
    #search.send_keys(Keys.CLEAR)
    search.send_keys(search_item)
    search.send_keys(Keys.RETURN)
    count = 0
    while (count < 20):
        try:
            count = count + 1
            prices = driver.find_element_by_css_selector("div.c2prKC:nth-child({}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > span:nth-child(1)".format(count)).text
            total_items = driver.find_element_by_class_name("c1DXz4").text
            price.append(prices)
            product_name.append(search_item)
            total_items_found.append(total_items)
        except:
            Break
    

driver.close()
df_price = pd.DataFrame(price, columns=['Prices'])
df_price['Keyword'] = pd.DataFrame(product_name)
df_price['Total items found'] = pd.DataFrame(total_items_found)
#df_reviews = pd.DataFrame(review, columns=['Review'])
print(df_price)

df_price.to_csv("final output.csv")