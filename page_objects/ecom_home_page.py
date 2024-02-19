from selenium.webdriver.common.by import By


class EcomHomePage:
    def __init__(self, driver):
        self.driver = driver

    item_price = (By.XPATH, "//*[@class='card-body']/h5")
    # "(//button[@class='btn btn-info'][normalize-space()='Add']"
    add_button = (By.XPATH, "//*[@class = 'card-footer']/button")
    "//h4[@class = 'card-title']//a[contains(text(),'iphone X')]"
    item = (By.XPATH, f"//h4[@class = 'card-title']//a[contains(text(),'iphone X')]")

    def add_to_cart(self, item_name):
        # item_name = "iphone X"
        actual_item_name = self.driver.find_element(EcomHomePage.item)
        if actual_item_name.text == item_name:
            print(actual_item_name.text)
            get_item_price = self.driver.find_element(EcomHomePage.item_price)
            print(get_item_price)
            self.driver.find_element(EcomHomePage.add_button).click()
        return actual_item_name.text
