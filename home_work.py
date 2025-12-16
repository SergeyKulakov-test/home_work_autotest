import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


#Драйвера браузеров
driver_crome = webdriver.Chrome(
    options=webdriver.ChromeOptions().add_experimental_option("detach", True),
    service=ChromeService(ChromeDriverManager().install())
)
driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_edge = webdriver.Edge(options=Options().add_experimental_option("detach", True))


#Функция открытия браузера
def open_brauser(brouser_driver):
    driver = brouser_driver
    base_url = "https://www.saucedemo.com/"  #Открываемая страница
    driver.get(base_url)
    driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением
    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #Поиск поля Username(input)
    user_name.send_keys("standard_user") #Заполнение поля Username данными
    user_password = driver.find_element(By.XPATH, "//input[@id='password']") #Поиск поля Password (input)
    user_password.send_keys("secret_sauce") #Заполнение поля Password данными
    button_login = driver.find_element(By.ID, "login-button") #Поиск кнопки Login
    button_login.click() #Нажатие кнопки Login

#Открываем браузер Chrome
open_brauser(driver_crome)

#Открываем браузер Firefox
open_brauser(driver_firefox)

#Открываем браузер Edge
open_brauser(driver_edge)