import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_registration_form1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)

        input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input3.send_keys("test@test.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be a 'Congratulations! You have successfully registered!' message")

    def test_registration_form2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)

        input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block .first")
        input1.send_keys("Ivan")
        input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block .second")
        input2.send_keys("Petrov")
        input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block .third")
        input3.send_keys("test@test.ru")

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be a 'Congratulations! You have successfully registered!' message")

if __name__ == "__main__":
    unittest.main()



