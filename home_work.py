import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys
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
user_password.send_keys("secret_sauce") #Заполнение поля Password не корректными данными
print("Ввод пароля (поле Password)")

#Авторизация/вход
button_login = driver.find_element(By.ID, "login-button") #Поиск кнопки Login
button_login.send_keys(Keys.ENTER) #Нажатие кнопки Login
print("Нажатие на кнопку Login")
time.sleep(3) #Задержка исполнения кода

#Создание скриншотов
now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S") #Создание переменной с текущем временем
name_screenshot = 'screenshot' + now_date + '.png' #Создание уникального иени скиншота
driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\Auto-test-project\\screen\\' + name_screenshot) #Сохраниение скриншота
print("Скриншот сохранен")
driver.close()
