from selenium import webdriver
import time

browser = webdriver.Chrome("C:/Users/21400/Desktop/chromedriver.exe")
browser.get("https://nid.naver.com/nidlogin.login")
id = browser.find_element_by_css_selector('#id').send_keys("naver id")
pw=browser.find_element_by_css_selector('#pw').send_keys("naver password")
time.sleep(5)
browser.find_element_by_css_selector("#frmNIDLogin > fieldset > input").click()
