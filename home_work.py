from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test():
    def test_1(self):
        # Драйвера браузера Chrome, настройки
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(
            options=options,
           service=ChromeService(ChromeDriverManager().install())
        )

        base_url = "https://www.saucedemo.com/"  #Открываемая страница
        driver.get(base_url)
        driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

stat_test = Test()
stat_test.test_1()
