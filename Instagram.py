from selenium import webdriver
import time


browser = webdriver.Chrome()

url = "https://www.instagram.com"

browser.get(url)

time.sleep(1)

loginButtonFirst = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")

loginButtonFirst.click()

time.sleep(4)

userNameTxtField = browser.find_element_by_name("username")
passwordTxtField = browser.find_element_by_name("password")
print(userNameTxtField)
print(passwordTxtField)
userNameTxtField.send_keys("")
passwordTxtField.send_keys("")

loginButtonSecond = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button")

loginButtonSecond.click()

time.sleep(5)

dismissButton = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")

dismissButton.click()

time.sleep(3)

# Reach Main Page of Instagram

myProfileButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a")

myProfileButton.click()

time.sleep(3)

followersButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")

followersButton.click()

time.sleep(3)
# js command for scroll
jsCommand = """
    var followers = document.querySelector(".isgrP");
    followers.scrollTo(0,followers.scrollHeight);
    return followers.scrollHeight;
    
"""
lenOfPage = browser.execute_script(jsCommand)
match = False
i = 0
while i != 4: # match == False:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jsCommand)
    i += 1
    if lastCount == lenOfPage:
        match = True

time.sleep(3)

# take folloersName

fs = browser.find_elements_by_css_selector("a.FPmhX.notranslate._0imsa")
for peep in fs:
    print(peep.text)

time.sleep(10)

browser.close()