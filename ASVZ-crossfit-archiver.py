# This script downloads the current workout of the day from the ASVZ-Homepage as a PNG and saves it to a folder of choice.

import datetime
import os.path
from time import sleep

import selenium.webdriver
from selenium import webdriver
Folderlocation = "./"
create_monthly_folder = True
create_yearly_folder = True
YEAR = datetime.datetime.now().strftime("%Y")
MONTH = datetime.datetime.now().strftime("%m")
onlyday = False
if create_yearly_folder:
    Folderlocation = Folderlocation + YEAR + "/"
    if not os.path.exists(Folderlocation):
        os.makedirs(Folderlocation)
if create_monthly_folder:
    Folderlocation = Folderlocation + MONTH + "/"
    if not os.path.exists(Folderlocation):
        os.makedirs(Folderlocation)
if onlyday:
    imagepath = Folderlocation + datetime.datetime.now().strftime("%d") + ".png"
else:
    imagepath = Folderlocation + datetime.datetime.now().strftime("%Y-%m-%d") + ".png"
options = selenium.webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.implicitly_wait(100)
browser.get("https://static.asvz.ch/ASVZ-Crossfit/CF-WOD.html")
browser.implicitly_wait(10000)
sleep(100)
browser.save_screenshot(imagepath)
browser.close()
