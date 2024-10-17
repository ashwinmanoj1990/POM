#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login_page:
    username_input = (By.CSS_SELECTOR,"#username")
    password_input = (By.CSS_SELECTOR, '#password')
    button_login_css_selector = (By.CSS_SELECTOR,"button[type=submit]")
    button_logout_xpath = (By.XPATH, "//i[contains(text(),'Logout')]")
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def setUsername(self,username):
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(username)

    def setPassword(self, password):
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        loginbtn = self.wait.until(EC.presence_of_element_located(self.button_login_css_selector))
        loginbtn.click()

    def click_logout(self):
        logoutbtn = self.wait.until(EC.presence_of_element_located(self.button_logout_xpath))
        logoutbtn.click()