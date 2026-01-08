import time


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

base_url = "https://demoqa.com/browser-windows"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']").click() #Закрываем куки

#Работа с вкладками и окнами
new_tab = driver.find_element(By.XPATH, "//button[@id='tabButton']") #Поиск кнопки открытия новой вкладки
print("Кнопка открытия вкладки на странице")
new_tab.click() #Нажатие кнопки
print("Кнопка открытия вкладки нажата")
driver.switch_to.window(driver.window_handles[1]) #Переход на новую вкладку
time.sleep(1) #Задержка исполнения кода
assert driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text == "This is a sample page", "Текст на новой странице не совпадает с требуемым"
print("Переход на новую вкладку осуществлен")
driver.switch_to.window(driver.window_handles[0]) #Переход на первую страницу
time.sleep(1) #Задержка исполнения кода

new_window = driver.find_element(By.XPATH, "//button[@id='windowButton']") #Поиск кнопки открытия нового окна
print("Кнопка открытия вкладки на странице")
new_window.click() #Нажатие кнопки
print("Кнопка открытия нового окна нажата")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.window(driver.window_handles[2]) #Переход на новую вкладку
assert driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text == "This is a sample page", "Текст на новой странице не совпадает с требуемым"
print("Переход в новое окно осуществлен")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.window(driver.window_handles[0]) #Переход на первую страницу

time.sleep(3) #Задержка исполнения кода
driver.close()