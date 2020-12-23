# Chapter 12: https://automatetheboringstuff.com/2e/chapter12/

# Module: webbrowser: to open a specific page
import webbrowser, requests, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# --------------------------------------------------------------------------------------------
# TODO: WEBBROWSER module

# TODO: Use webbrowser to open website
# webbrowser.open('https://automatetheboringstuff.com/2e/chapter12/')

# --------------------------------------------------------------------------------------------
# TODO: REQUESTS module

# TODO: Use requests to download web Content
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')  # romeo and juliet entire play
# if res.status_code == requests.codes.ok:  # check if the request is approved
#     print("Length of the text:", len(res.text))
#     print(res.text[:250])

# TODO: Checking errors
# res = requests.get('https://automatetheboringstuff.com/noFileFound')
# try:
#     res.raise_for_status()  # if no error found then nothing happened
# except Exception as exc:
#     print("There was a problem:", exc)

# TODO: write to Hardware
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('RomeoAndJuliet.txt', 'wb')  # write in binary
# for chunk in res.iter_content(10000):  # the file we read here is in binary
#     playFile.write(chunk)


# ---------------------------------------------------------------
# TODO: bs4 module (beautiful Soup)
# used to parse HTML

# TODO: get the HTML template
# res = requests.get("https://nostarch.com/automatestuff2/")
# res.raise_for_status()
# exampleFile = open("example.html", "wb")
# for chunk in res.iter_content():
#     exampleFile.write(chunk)

# TODO: Create BeautifulSoup Object from HTML
# exampleFile = open("example.html", "r", encoding="utf8")  # need encoding to avoid error
# exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

# TODO: Finding an element with the select() method
# can search for bs4.select and CSS selector in python
# elems = exampleSoup.select(".sr-only")
# for element in elems:
#     print(element.get("class"))


# ---------------------------------------------------------------------
# TODO: selenium module
# *** need to download a suitable driver for the browser
browser = webdriver.Chrome(executable_path="D:\Software\Chrome\chromedriver.exe")
# try:
#     browser.get('https://inventwithpython.com')
#     linkElem = browser.find_element_by_link_text("Read Online for Free")
#     print('Found <%s> element with that class name!' % (linkElem.tag_name))
#     linkElem.click()
# except:
#     print('Was not able to find an element with that name.')

# try:
#     browser.get('https://login.metafilter.com')
#     userElem = browser.find_element_by_id("user_name")
#     userElem.send_keys("truongductri01")
#
#     passwordElem = browser.find_element_by_id("user_pass")
#     passwordElem.send_keys("07112001")
#
#     passwordElem.submit()
# except:
#     print("Error")

try:
    browser.get('https://nostarch.com')
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END)  # scrolls to bottom
    htmlElem.send_keys(Keys.HOME)  # scrolls to top
except:
    print("Error")
