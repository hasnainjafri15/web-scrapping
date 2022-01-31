from ast import Break, Return
from functools import total_ordering
from webbrowser import Chrome
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
from selenium.webdriver import ActionChains


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.daraz.pk/")
driver.maximize_window()
driver.minimize_window()


search = driver.find_element_by_class_name("search-box__input--O34g")

#level 1 assortments

#Level_1_Category_No2 > a:nth-child(1) > span:nth-child(1)
##Level_1_Category_No3 > a:nth-child(1) > span:nth-child(1)

#level 2 assortments
#ul.lzd-site-menu-sub: nth-child(13) > li: nth-child(1) > a: nth-child(1) > span: nth-child(1)
#ul.lzd-site-menu-sub: nth-child(13) > li: nth-child(1) > a: nth-child(1) > span: nth-child(1)
#li.sub-item-remove-arrow: nth-child(2) > a: nth-child(1) > span: nth-child(1)
#li.sub-item-remove-arrow: nth-child(3) > a: nth-child(1) > span: nth-child(1)
#li.sub-item-remove-arrow:nth-child(4) > a:nth-child(1) > span:nth-child(1)


#deny = driver.find_element_by_xpath("")
#test = driver.find_element_by_id("topActionSell")

#test = driver.find_element_by_xpath(
    #"/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[3]/a")

#l1 = driver.find_elements_by_id("Level_1_Category_No1")

a = ActionChains(driver)
print("clear1")
print(".")
l1_category = driver.find_element_by_id("Level_1_Category_No1")
print("clear2")
a.move_to_element(l1_category).perform
time.sleep(3)
print(".")
#l2_category = driver.find_element_by_id("a2a0e.home.cate_1.1")
#a.move_to_element(l2_category).perform
print(".")
#a.move_to_element(l2_category).click()
print("clear3")
print(".")
print("clear4")
print(".")
driver.quit()
#a.move_to_element(deny).click().perform()

#a.move_to_element(l2_category).perform()
#a.move_to_element(test).click().perform()

#a.move_to_element(l2_category).click().perform()

#driver.quit()

