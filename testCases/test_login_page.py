from pageObjects.login_page import login_page
#import pytest
#from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_login_001:
    form_authentication_page = ReadConfig.getappurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_checkTitle(self,setup):
        self.logger.info('Test-001')
        self.logger.info('TEST TITLE')
        self.driver = setup
        self.driver.get(self.form_authentication_page)
        act_title = self.driver.title
        
        if act_title == "The Internet":
            assert True
            self.logger.info('Title test passed!!')
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            assert False

    def test_login(self,setup):
        self.logger.info('test Login!!')
        self.driver = setup
        self.driver.get(self.form_authentication_page)

        self.lp = login_page(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        self.lp.click_logout()
        
        if act_title == "The Internet":
            assert True
            self.logger.info('Login test passed!!')
            self.driver.close()
        else:
            self.logger.error('test Login!!')
            self.driver.close()
            assert False
    