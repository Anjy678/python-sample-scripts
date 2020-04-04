from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class igBot():

    def __init__(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\akase\AppData\Local\Mozilla\Firefox\geckodriver.exe')

    def login(self, usrname, psword):
        self.browser.get("https://www.instagram.com")

        time.sleep(2)

        username_field = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        psword_field = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')

        try:
            username_field.send_keys(usrname) #types in username
            psword_field.send_keys(psword) #types in password
            time.sleep(2)
            login_but = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
            login_but.click()
            time.sleep(8)

            if self.isElementPresent('js not-logged-in client-root js-focus-visible sDN5V'):
                raise Exception() #Still on login page

        except Exception: #Could not log in
            print('Username and/or password are incorrect')
            print('Please restart program and try again') 
            self.browser.quit()
            return

        if (self.isElementPresent('piCib')):
            notif_box = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
            notif_box.click()
            print("Successfully logged in")
            return
        else:
            print("Successfully logged in")
            return
    
    def isElementPresent(self, id):
        if len(self.browser.find_elements_by_class_name(id)) == 0:
            return False
        else:
            return True            

print("Welcome to the Instagram auto-login")
time.sleep(3)
usrname = input("Enter Username: ")
psword = input("Enter Password: ")
bot = igBot()
print("Logging you in...")
bot.login(usrname, psword)




