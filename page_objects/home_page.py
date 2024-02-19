from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender_drp = (By.ID, "exampleFormControlSelect1")
    employed_radio = (By.XPATH, "//*[@class = 'form-group']/div[2]/input")
    dob_drp = (By.NAME, "bday")
    submit = (By.CSS_SELECTOR, "input[value='Submit']")


    def enter_name(self):
        return self.driver.find_element(*HomePage.name).send_keys("Jamser Ali")

    def enter_email(self):
        return self.driver.find_element(*HomePage.email).send_keys("way2sms@gmail.com")

    def enter_password(self):
        return self.driver.find_element(*HomePage.password).send_keys("JamserAli")

    def click_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox).click()

    def select_gender_dropdown(self):
        return self.driver.find_element(*HomePage.gender_drp)


    def click_employee_radio_btn(self):
        return self.driver.find_element(*HomePage.employed_radio).click()

    def select_dob_from_dropdown(self):
        return self.driver.find_element(*HomePage.dob_drp).send_keys("01/06/1995")


    def click_submit_button(self):
        return self.driver.find_element(*HomePage.submit).click()










