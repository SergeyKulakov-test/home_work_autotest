import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Test_Open_Browser:

    def __init__(self):
        self.driver = None
        self.options = None

    def __create_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        return self.options

    def __create_driver(self):
        self.driver = webdriver.Chrome(
            options=self.__create_options(),
            service=ChromeService(ChromeDriverManager().install())
        )
        return self.driver

    def set_window_size(self, width, height):
        self.__create_driver().set_window_size(width, height)
        print(f"Размер окна установлен: {width}x{height}")  #Открытие окна с заданным разрешением

    def open_url(self, base_url):
        self.driver.get(base_url)
        print("Страница открыта")

    def close_page(self):
         self.driver.close()
         print("Страница закрыта")


if __name__ == "__main__":
    open_browser = Test_Open_Browser() #Создаем экземпляр класса
    open_browser.set_window_size(1200, 900) #Устанавливаем размер окна
    open_browser.open_url("https://www.saucedemo.com") #Открываем страницу
    time.sleep(3)
    open_browser.close_page()


