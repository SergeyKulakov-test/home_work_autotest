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

base_url = "https://demoqa.com/buttons"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Проверка кликов: двойной клик и клик правой кнопкой
actions = ActionChains(driver)
double_click_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']") #Поиск кнопки для двойного клика
actions.double_click(double_click_button).perform() #Выполнение двойного клика
print("Произведен двойной клик мыши")
assert driver.find_element(By.XPATH, "//p[@id='doubleClickMessage']").text == "You have done a double click", "Двойной клик не произведен" #Проверка, что двойной клик произведен
print("Двойной клик мыши выполнен")

right_click_button = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']") #Поиск кнопки для клика правой кнопкой
actions.context_click(right_click_button).perform() #Выполнение клика правой кнопкой
print("Произведен клик правой кнопкой мыши")
assert driver.find_element(By.XPATH, "//p[@id='rightClickMessage']").text == "You have done a right click", "Двойной клик не произведен" #Проверка, что клик правой кнопкой выполнен
print("Клик правой кнопкой мыши выполнен")

time.sleep(1) #Задержка исполнения кода
driver.close()
