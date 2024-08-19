import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestRegistration:
    @pytest.mark.parametrize("link", [
        "http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"
    ])
    def test_registration_form(self, browser, link):
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@test.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text

        assert welcome_text == "Congratulations! You have successfully registered!", "Should be a 'Congratulations! You have successfully registered!' message"


if __name__ == "__main__":
    pytest.main()