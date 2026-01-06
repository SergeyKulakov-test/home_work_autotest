import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.support.select import Select
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

base_url = "https://lambdatest.com/selenium-playground/simple-form-demo"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']").click() #Закрываем куки

#Ввод и проверка отправки сообщения
message = "Hello World!" #Вводимое сообщение
input_message = driver.find_element(By.XPATH, "//input[@id='user-message']") #Поле для ввода сообщения
print("Поле ввода сообщений найдено")
input_message.send_keys(message) #Ввод сообщения
print("Сообщение введено")
driver.find_element(By.XPATH, "//button[@id='showInput']").click() #Отправка сообщения
print("Сообщение отправлено")

value_show_message = driver.find_element(By.XPATH, "//p[@id='message']").text #Текст отправленного сообщения
print(f"Текст отправленного сообщения {value_show_message}")
assert value_show_message == message, "Текст отправленного сообщения не соответствует введенному тексту" #Проверка сообщения
print("Текст отправленного сообщения соответствует введенному тексту")


#Проверка работы форм для сложения
number_1 = 101 #Первое вводимое число
number_2 = 102 #Второе вводимое число
summ = number_1 + number_2 #Сумма вводимых чисел

input_number_1 = driver.find_element(By.XPATH, "//input[@id='sum1']") #Поле для ввода первого числа
print("Поле ввода первого числа найдено")
input_number_1.send_keys(number_1) #Ввод первого числа
print("Второе число введено")

input_number_2 = driver.find_element(By.XPATH, "//input[@id='sum2']") #Поле для ввода второго числа
print("Поле ввода второго числа найдено")
input_number_2.send_keys(number_2) #Ввод первого числа
print("Второе число введено")

driver.find_element(By.XPATH, "//*[@id='gettotal']/button").click() #Нажатие кнопки для вычисления суммы
print("Кнопка суммы нажата")

result_summ = driver.find_element(By.XPATH, "//p[@id='addmessage']").text #Полученная сумма
print(f"Итоговая сумма {result_summ}")
assert float(result_summ) == summ, "Полученная сумма не совпадает ссуммой введеных чисел" #Проверка правильности вычислений
print("Сумма верна")


time.sleep(3) #Задержка исполнения кода
driver.close()
