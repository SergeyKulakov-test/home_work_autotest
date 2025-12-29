import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


#Драйвера браузера Chrome, настройки
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# Опции для отключения проверки утечки паролей
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False  # Отключаем обнаружение утечек
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--password-store=basic")
#options.add_argument('--headless') #Запуск в фоновом режиме (без открытия браузера)

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = "https://www.saucedemo.com/"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Ввод не корректных данных
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #Поиск поля Username(input)
user_name.send_keys("standard") #Заполнение поля Username не корректными данными
print("Ввод некорректного логина (поле Username)")

user_password = driver.find_element(By.XPATH, "//input[@id='password']") #Поиск поля Password (input)
user_password.send_keys("secret") #Заполнение поля Password не корректными данными
print("Ввод некорректного пароля (поле Password)")

#Удаление заполненых полей
user_name.send_keys(Keys.CONTROL + 'a') #Выдиляем поле Username
user_name.send_keys(Keys.DELETE) #Очищаем поле Username
print("Очистка логина (поле Username)")

user_password.send_keys(Keys.CONTROL + 'a') #Выдиляем поле Password
user_password.send_keys(Keys.DELETE) #Очищаем поле Password
print("Очистка пароля (поле Password)")

#Ввод корректных данных
user_name.send_keys("standard_user") #Заполнение поля Username корректными данными
print("Ввод корректного логина (поле Username)")

user_password.send_keys("secret_sauce") #Заполнение поля Password не корректными данными
print("Ввод корректного пароля (поле Password)")

#Авторизация/вход
button_login = driver.find_element(By.ID, "login-button") #Поиск кнопки Login
button_login.send_keys(Keys.ENTER) #Нажатие кнопки Login
print("Нажатие на кнопку Login")

#Добавление товаров в корзину
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click() #Добавление в корзину первого товара
print("Первый товар добавлен в корзину")
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click() #Добавление в корзину второго товара
print("Второй товар добавлен в корзину")

#Переход в корзину
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
print("Кнопка корзины нажата")
time.sleep(1) #Задержка исполнения кода

#Возвращение на страницу каталога и обратно  вкорзину
driver.back() #Возврат на страницу каталога
print("Вернулись на страницу каталога")
time.sleep(1) #Задержка исполнения кода

driver.forward() #Переход обратно в корзину
print("Перешли обратно в корзину")

time.sleep(1) #Задержка исполнения кода
driver.close()
