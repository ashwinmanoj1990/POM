from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
try:
    wait = WebDriverWait(driver,20)
    driver.get('https://admin-demo.nopcommerce.com/login')
    print('login success')
    driver.find_element(By.ID, 'Email').clear()
    print('clear success')
    driver.find_element(By.ID, 'Email').send_keys('admin@yourstore.com')
    print('id entered')
    driver.find_element(By.ID,"Password").clear()
    print('password cleared')
    driver.find_element(By.ID,"Password").send_keys('admin')
    print('pass entered')
    driver.find_element(By.XPATH,"//button[contains(text(),'Log in')]").click()
    print('login success')

    logout_btn = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT,'Logout')
    ))

    logout_btn.click()


    
    """form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))

    form_auth_link.click()
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')
    ))
    username.send_keys('tomsmith')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')
    )).click()

    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))

    assert 'logged out' in flash.text """

    

finally:
    driver.close()
