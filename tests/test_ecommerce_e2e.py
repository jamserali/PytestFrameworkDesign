from page_objects.ecom_home_page import EcomHomePage
from utilities.base_class import BaseClass


class Test_EcommerceE2E(BaseClass):

    def test_ecom_e2e(self):
        item_name = "iphone X"
        ecom_home = EcomHomePage(self.driver)
        log = self.getLogger()
        try:
            items = ecom_home.add_to_cart(item_name)
            log.info(items)
        except Exception as e:
            log.error(e)
        log.info("This is add to cart - ecommerce project")
        # ecom_home.add_to_cart(item_name)


