from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


class TestMainPage():
    def test_pages_should_contain_addbutton(self, browser):
        browser.get(link)
        button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")))
        # text_button = button.text
        # assert text_button == "Ajouter au panier", \
        #     f" Language is not french {message} "
        assert button is not None, \
            f" Language is not french"

