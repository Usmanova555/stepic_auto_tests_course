import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestProductPage:
    def get_product_name(self, browser):
        """Извлекает название товара с основной страницы."""
        return browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self, browser):
        """Извлекает цену товара с основной страницы."""
        return browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    def test_guest_can_add_product_to_basket(self, browser):
        # Открываем страницу товара
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        browser.get(link)

        # Получаем название и цену товара
        product_name = self.get_product_name(browser)
        product_price = self.get_product_price(browser)

        # Добавляем товар в корзину
        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_to_basket_button.click()

        # Обработка промо-алерта, если он появляется
        browser.switch_to.alert.accept()

        # Проверка названия товара в сообщении о добавлении в корзину
        success_message = browser.find_element(By.CSS_SELECTOR, "#messages .alert-success .alertinner strong").text
        assert product_name == success_message, (
            f"Expected product name '{product_name}', but got '{success_message}'"
        )

        # Проверка цены товара в сообщении о стоимости корзины
        basket_total = browser.find_element(By.CSS_SELECTOR, ".alert-info .alertinner p strong").text
        assert product_price in basket_total, (
            f"Expected product price '{product_price}' to be in '{basket_total}'"
        )

# Пример запуска: pytest -v test_product_page.py
