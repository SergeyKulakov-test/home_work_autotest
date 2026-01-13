import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test_open_browser:

    def __init__(self):
        self.driver = None
        self.options = None

    def create_options(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return self.options

    def create_driver(self):
        self.driver = webdriver.Chrome(
            options=self.options,
            service=ChromeService(ChromeDriverManager().install())
        )
        return self.driver

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)
        print(f"Размер окна установлен: {width}x{height}")  #Открытие окна с заданным разрешением


    def open_url(self, base_url):
        self.driver.get(base_url)
        print("Страница открыта")

    def close_page(self):
         self.driver.close()
         print("Страница закрыта")


if __name__ == "__main__":
    open_browser = Test_open_browser() #Создаем экземпляр класса
    options = open_browser.create_options() #Получаем настройки браузера
    driver = open_browser.create_driver() #Создаем драйвер
    open_browser.set_window_size(1200, 900) #Устанавливаем размер окна
    open_browser.open_url("https://www.saucedemo.com") #Открываем страницу
    time.sleep(3)
    open_browser.close_page()


