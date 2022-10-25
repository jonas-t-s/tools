# This script downloads the current workout of the day from the ASVZ-Homepage as a PNG and saves it to a folder of choice.

import datetime
from time import sleep

import selenium.webdriver
from selenium import webdriver
Folderlocation = "./"
options = selenium.webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(options=options)

browser.implicitly_wait(100)
browser.get("https://static.asvz.ch/ASVZ-Crossfit/CF-WOD.html")
browser.implicitly_wait(10000)
sleep(100)
browser.save_screenshot(Folderlocation + datetime.datetime.now().strftime("%Y-%m-%d") + ".png")
browser.close()
