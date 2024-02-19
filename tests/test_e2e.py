import time
from page_objects.home_page import HomePage
from utilities.base_class import BaseClass

class Test_End2End(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)
        homepage.enter_name()
        homepage.enter_email()
        homepage.enter_password()
        homepage.click_checkbox()
        gender = homepage.select_gender_dropdown()
        self.select_option_by_visible_text(gender, "Male")
        homepage.click_employee_radio_btn()
        homepage.select_dob_from_dropdown()
        homepage.click_submit_button()
        time.sleep(5)
