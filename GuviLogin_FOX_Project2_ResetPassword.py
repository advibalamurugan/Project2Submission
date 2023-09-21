import selenium.webdriver as webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Vani:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()

# usage of NAME & XPATH
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(20)
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"))).click()
        sleep(20)
        self.driver.find_element(by=By.NAME, value='username').send_keys('advibalamurugan@gmail.com') 
        sleep(20)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()=' Reset Password ']"))).click()
        


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
Vani(url).login()