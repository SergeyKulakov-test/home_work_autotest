import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = "https://demoqa.com/dynamic-properties" #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением


#Обработка иcключений
try:
    driver.find_element(By.XPATH, "//button[@id='visibleAfter']").click() #Нажатие на кнопку
    print("Кнопка нажата")
except NoSuchElementException:
    print("Получили NoSuchElementException")
    time.sleep(2) #Задержка исполнения кода
    driver.refresh() #Перезагрузка страницы
    time.sleep(5) #Задержка исполнения кода
    driver.find_element(By.XPATH, "//button[@id='visibleAfter']").click()  #Нажатие на кнопку
    print("Кнопка нажата")

time.sleep(3) #Задержка исполнения кода
driver.close()