from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = "YOUR USERNAME"
password = "YOUR PASSWORD"
count = 20 #how many messages you want to delete

driver_path = "D:\chromedriver.exe"


class instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(driver_path)

    def girisyap(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)
        if self.browser.find_element_by_class_name("cmbtv"):
            el = self.browser.find_element_by_class_name("cmbtv")
            el.find_element_by_tag_name("button").click()
        time.sleep(6)
        if self.browser.find_element_by_class_name("mt3GC"):
            self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm").click()
        time.sleep(5)
    def mesajsil(self):
        self.browser.get("https://www.instagram.com/direct/inbox/")
        time.sleep(3)
        self.browser.find_element_by_class_name("FrP6F").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector("#react-root > section > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.DPiy6.qF0y9.Igw0E.IwRSH.eGOV_.acqo5.vwCYk > div.CpMFL > div > div > div._2NzhO.EQ1Mr > button > div > svg").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector("#react-root > section > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm > div > div > div.DPiy6.qF0y9.Igw0E.IwRSH.eGOV_.acqo5.vwCYk > div > div._9XapR > div:nth-child(4) > div:nth-child(1) > button > div").click()
        time.sleep(1)
        self.browser.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.-Cab_").click()


app = instagram(username, password)
app.girisyap()
for i in range (count):
    app.mesajsil()
