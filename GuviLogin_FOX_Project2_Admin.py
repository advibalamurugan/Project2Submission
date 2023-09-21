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
        self.username = 'Admin'
        self.password = 'admin123'
     
# usage of NAME & XPATH
    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(20)
        self.driver.find_element(by=By.NAME, value='username').send_keys(self.username)
        self.driver.find_element(by=By.NAME, value='password').send_keys(self.password)
        self.driver.find_element(by=By.XPATH,
value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        sleep(20)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()
        sleep(20)

url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
Vani(url).login()