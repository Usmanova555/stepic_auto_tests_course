import pytest
from selenium.webdriver.common.by import By

class TestProductPage:
    def get_product_name(self, browser):
        return browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self, browser):
        return browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
    def test_guest_can_add_product_to_basket(self, browser, link):
        browser.get(link)

        product_name = self.get_product_name(browser)
        product_price = self.get_product_price(browser)

        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_basket_button.click()

        browser.switch_to.alert.accept()

        success_message = browser.find_element(By.CSS_SELECTOR, "#messages .alert-success .alertinner strong").text
        assert product_name == success_message, (
            f"Expected product name '{product_name}', but got '{success_message}'"
        )

        basket_total = browser.find_element(By.CSS_SELECTOR, ".alert-info .alertinner p strong").text
        assert product_price in basket_total, (
            f"Expected product price '{product_price}' to be in '{basket_total}'"
        )

    @pytest.mark.parametrize('link', [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
    def test_guest_can_add_product_to_basket_with_xfail(self, browser, link):
        browser.get(link)

        product_name = self.get_product_name(browser)
        product_price = self.get_product_price(browser)

        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_basket_button.click()

        browser.switch_to.alert.accept()

        success_message = browser.find_element(By.CSS_SELECTOR, "#messages .alert-success .alertinner strong").text
        assert product_name == success_message, (
            f"Expected product name '{product_name}', but got '{success_message}'"
        )

        basket_total = browser.find_element(By.CSS_SELECTOR, ".alert-info .alertinner p strong").text
        assert product_price in basket_total, (
            f"Expected product price '{product_price}' to be in '{basket_total}'"
        )
