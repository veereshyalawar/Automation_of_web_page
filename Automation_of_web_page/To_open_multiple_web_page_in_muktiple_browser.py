import time
from Browers import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image

print("1:chrome")
print("2:Explorer")
choice = int(input("Enter your choice"))
if choice == 1:
    serv_obj = Service("Driver/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
if choice == 2:
    serv_obj1 = Service("Driver/chromedriver_win32/msedgedriver.exe")
    driver = webdriver.Edge(service=serv_obj1)
driver.get("https://www.facebook.com/")
driver.forward()
driver.get("https://www.amazon.in/")
driver.forward()
time.sleep(4)
driver.close()
