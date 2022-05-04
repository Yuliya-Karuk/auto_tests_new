import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en and etc")


options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': "language"})

# фикстура для запуска браузера
@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    # browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    user_language = request.config.getoption("language")

    yield browser
    print("\nquit browser..")
    browser.quit()






