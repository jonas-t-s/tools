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
    basepath = Folderlocation + datetime.datetime.now().strftime("%d")
    imagepath =  basepath+ ".png"
    jsonpath = basepath + ".json"
else:
    basepath = Folderlocation + datetime.datetime.now().strftime("%Y-%m-%d")
    imagepath = basepath + ".png"
    jsonpath = basepath + ".json"
options = selenium.webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(options=options)
os.system("curl 'https://webwidgets.prod.btwb.com/webwidgets/wods?sections=main&track_ids=658590&activity_length=0&leaderboard_length=0&days=0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0' -H 'Accept: application/vnd.btwb.v1.webwidgets+json' -H 'Accept-Language: de,en-US;q=0.7,en;q=0.3' -H 'Accept-Encoding: gzip, deflate, br' -H 'Authorization: Bearer 3yns3r6sc1ytcaogxw7g6tfrr' -H 'Origin: https://static.asvz.ch' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://static.asvz.ch/' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: cross-site' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers' -o " + jsonpath)
browser.implicitly_wait(100)
browser.get("https://static.asvz.ch/ASVZ-Crossfit/CF-WOD.html")
browser.implicitly_wait(10000)
sleep(100)
browser.save_screenshot(imagepath)
browser.close()
