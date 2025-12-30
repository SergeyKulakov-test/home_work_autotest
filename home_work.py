import time
import datetime
from tabnanny import check

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

base_url = "https://demoqa.com/radio-button"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Установка чекбокса и его проверка
radio_button = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/div[3]/label") #Поиск элемента label на странице для клика (второй)
print("Радиобатон найден на странице")
radio_button.click() #Установка чекбокса
assert driver.find_element(By.XPATH, "//*[@id='impressiveRadio']").is_selected(), "Радиобатон не установлен" #Проверка что радиобатон установлен
print("Радиобатон установлен")
assert driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div[2]/p").text == "You have selected Impressive" , "Установлен не второй радиобатон" #Проверка что радиобатон установлен правильно (выбран второй)
print("Радиобатон установлен правильно, выбран второй вариант")

time.sleep(1) #Задержка исполнения кода
driver.close()
