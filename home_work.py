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

base_url = "https://lambdatest.com/selenium-playground/jquery-dropdown-search-demo"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']").click() #Закрываем куки

#Выбор Dropdown
click_drop = driver.find_element(By.XPATH, "(//span[@aria-labelledby='select2-country-container'])") #Поиск выпадающего списка на странице
print("Выподающий список найден")
click_drop.click() #Раскрытие выпадающего списка
print("Клик на выподающий список выполнен")

select_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[7]") #Поиск элемента для выбора внутри выпадающего списка
print("Выбраны Netherlands")
select_country_name = select_country.text #Выбранное название
select_country.click() #Подтверждение выбора (клик)
print("Выбор подтвержден")

assert click_drop.text == select_country_name, "Выбранная страна совпадает с установленной в списке" #Проверка соответствия выбранного названия и записанного после выбора
print("Выбор верен")

time.sleep(3) #Задержка исполнения кода
driver.close()
