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

base_url = "https://www.lambdatest.com/selenium-playground/iframe-demo/"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']").click() #Закрываем куки

#Взаимодействие с iFrame
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']") #Поиск на странице iFrame
print("iFrame найден на странице")
driver.switch_to.frame(iframe) #Переход в iFrame
print("Перешли в iFrame")

input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]") #Поиск поля ввода
print("Поле для ввода найдено на странице")
input_pole.send_keys(Keys.CONTROL + "a") #Выделение текста
input_pole.send_keys(Keys.DELETE) #Удаление текста
print("Поле очищено")

new_value_input_pole = "Hello World!"
input_pole.send_keys(new_value_input_pole) #Ввод текста
print("Введен новый текст")
input_pole.send_keys(Keys.CONTROL + "a") #Выделение текста

driver.find_element(By.XPATH, "//button[@title='Bold']").click() #Делаем текст жирным
print("Текст сделан жирным")
driver.find_element(By.XPATH, "//button[@title='Italic']").click() #Делаем текст курсивом
print("Текст сделан курсивом")
current_value_input_pole = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/b/i").text #Получаем существующий текст в поле
print(current_value_input_pole)
assert current_value_input_pole == new_value_input_pole, "Введенный текст не совпадает с текстом в поле"
print("Текст совпадает")

time.sleep(3) #Задержка исполнения кода
driver.close()
