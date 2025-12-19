import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#Драйвера браузера Chrome, настройки
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument('--headless') #Запуск в фоновом режиме (без открытия браузера)

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = "https://www.saucedemo.com/"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Ввод данных
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #Поиск поля Username(input)
user_name.send_keys("standard_user") #Заполнение поля Username корректными данными
print("Ввод логина (поле Username)")

user_password = driver.find_element(By.XPATH, "//input[@id='password']") #Поиск поля Password (input)
user_password.send_keys("secret") #Заполнение поля Password не корректными данными
print("Ввод пароля (поле Password)")

#Авторизация/вход
button_login = driver.find_element(By.ID, "login-button") #Поиск кнопки Login
button_login.click() #Нажатие кнопки Login
print("Нажатие на кнопку Login")

#Ошибка при вводе пароля
waring_text = driver.find_element(By.XPATH, "//h3[@data-test='error']") #Поиск сообщения об ошибке
value_warring_text = waring_text.text
assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service', "Текст сообщения об ошибке не совпадает" #Проверка соответствия текста ошибки
print("Сообщение об ошибке корректно")

#Закрытие сообщения об ошибке
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']") #Поиск кнопки закрытия сообщения
error_button.click() #Нажатие кнопки закрытия сообщения
print("Кнопка закрытия сообщения об ошибке нажата")

time.sleep(3) #Задержка исполнения кода
driver.refresh() #Обновление страницы