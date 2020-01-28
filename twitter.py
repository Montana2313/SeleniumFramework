from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

url = "https://twitter.com/"

browser.get(url)

time.sleep(1)

loginButton = browser.find_element_by_xpath("//*[@id='doc']/div/div[1]/div[1]/div[2]/div[2]/div/a[2]")

loginButton.click()

time.sleep(1)

usernameTextField = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")

passwordTextField = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
#send
usernameTextField.send_keys("")
passwordTextField.send_keys("")

loginButton2 = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")

loginButton2.click()

time.sleep(2)

searchButton = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/header/div/div/div/div/div[2]/nav/a[2]")

searchButton.click()

time.sleep(2)

searchBar = browser.find_element_by_xpath(
    "//*[@id='react-root']/div/div/div/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input")

searchBar.send_keys("alyssumliveo")

searchBar.send_keys(Keys.ENTER)
time.sleep(5)

# Scroll codes starting her
lenOfPage = browser.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
s = 0
while s != 4:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    s += 1
    if lastCount == lenOfPage:
        match = True
time.sleep(1)
# end of scroll

time.sleep(1)

twField = browser.find_elements_by_css_selector("css-18t94o4.css-1dbjc4n.r-1777fci.r-11cpok1.r-1ny4l3l.r-bztko3.r-lrvibr")

for item in twField:
    try:
        if item.get_attribute('data-testid') == 'like':
            item.click()
    except Exception:
        print("Hata")



# cont//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div/svg/g/pathents = browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0")

# for item in contents:
# print(item.text)

browser.close()
