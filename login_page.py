import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, username = "standard_user", password = "secret_sauce"):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).send_keys(username)  # Заполнение поля Username
        print(f"Ввод {username}")
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys(password)  # Заполнение поля Password
        print(f"Ввод {password}")
        time.sleep(2)  # Задержка исполнения кода
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()  # Нажатие кнопки Login
        print("Нажатие на кнопку Login")