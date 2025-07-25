from Library import ConfigReader
from selenium.webdriver.common.by import By

class RegistrationClass:

    def __init__(self, obj):
        global driver
        driver = obj

    def enter_username(self, username, lastname):
        driver.find_element(By.ID,ConfigReader.fetchElementLocators("Registration","username_name")).send_keys(username)
        driver.find_element(By.ID, ConfigReader.fetchElementLocators("Registration", "username_lastname")).send_keys(lastname)

    def enter_email(self, email):
        driver.find_element(By.ID,ConfigReader.fetchElementLocators("Registration","email_name")).send_keys(email)

    def enter_button_male(self):
        gender_radio = driver.find_element(By.ID, "gender-radio-1")
        driver.execute_script("arguments[0].click();", gender_radio)
    
    def enter_phoneNumber(self, phoneNumber):
        driver.find_element(By.ID,ConfigReader.fetchElementLocators("Registration","phone_number")).send_keys(phoneNumber)

    def enter_uploadPicture(self, upload_picture):
        input_arquivo = driver.find_element(By.ID, ConfigReader.fetchElementLocators("Registration", "upload_picture"))
        input_arquivo.send_keys(upload_picture)

    def click_submmit(self):
        submit_btn = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        submit_btn.click()
