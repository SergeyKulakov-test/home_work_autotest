import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAddProductToCart:

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

    def authorization(self, username = "standard_user", password = "secret_sauce"):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).send_keys(username)  # Заполнение поля Username
        print(f"Ввод {username}")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys(password)  # Заполнение поля Password
        print(f"Ввод {password}")
        time.sleep(2)  # Задержка исполнения кода
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()  # Нажатие кнопки Login
        print("Нажатие на кнопку Login")

    def add_product_to_cart(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']"))).click()  # Добавление в корзину первого товара
        print("Товар добавлен в корзину")

    def open_cart(self):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a"))).click() # Открытие корзины
        print("Кнопка корзины нажата")


if __name__ == "__main__":
    add_product = TestAddProductToCart() #Создаем экземпляр класса
    add_product.set_window_size(1200, 900) #Устанавливаем размер окна
    add_product.open_url("https://www.saucedemo.com") #Открываем страницу
    time.sleep(2)

    add_product.authorization() #Авторизация

    value_text_page = add_product.driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").text
    assert value_text_page == "Products", "Текст на странице не найден"  # Проверка загрузки страницы
    print("Страница каталога загружена")
    time.sleep(2)

    add_product.add_product_to_cart() #Добавление товара в корзину
    time.sleep(2)

    add_product.open_cart() #Переход в корзину
    value_text_page = add_product.driver.find_element(By.XPATH, "//span[contains(text(), 'Your Cart')]").text
    assert value_text_page == "Your Cart", "Текст на странице не найден"  # Проверка загрузки страницы
    print("Страница корзины загружена")
    time.sleep(2)

    add_product.close_page()