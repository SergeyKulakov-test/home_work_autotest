import time
from datetime import datetime, timedelta

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

base_url = "https://demoqa.com/date-picker"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Ввод даты
date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']") #Поиск поля для ввода даты
date_input.send_keys(Keys.CONTROL + "a") #Выделение содержимого поля
date_input.send_keys(Keys.DELETE)  #Очистка поля даты
print("Произведена очистка поля для ввода даты")

current_date = (datetime.now() + timedelta(days=10)).strftime("%m/%d/%Y") #Определяем текущую дату и смещаем её на 10 дней
date_input.send_keys(current_date) #Ввод нужной даты
print("Требуемая дата введена")

time.sleep(3) #Задержка исполнения кода
driver.close()
