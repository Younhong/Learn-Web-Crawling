from selenium import webdriver
import time
from bs4 import BeautifulSoup

browser = webdriver.Chrome("C:/Users/21400/Desktop/chromedriver.exe")
browser.get("https://www.w3schools.com/colors/colors_rgb.asp")
time.sleep(2)
browser.find_element_by_css_selector('#r01').clear()
browser.find_element_by_css_selector('#r01').send_keys("255")
browser.find_element_by_css_selector("#g01").send_keys("255")
browser.find_element_by_css_selector('#b01').send_keys("255")
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
color = soup.find("div", {"id":"hex01"}).text
print(color)
time.sleep(10)
browser.quit()
