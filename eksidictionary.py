from selenium import webdriver
import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <= 10:
    randomNumber = random.randint(1, 1915)
    newURL = url + str(randomNumber)
    browser.get(newURL)
    elements = browser.find_elements_by_css_selector("div.content")
    for item in elements:
        entries.append(item.text)
    time.sleep(3)
    pageCount += 1

for item in entries:
    print("------------------")
    print(item)
    print("------------------")

print(len(entries) + "items have been found ... ")

browser.close()
