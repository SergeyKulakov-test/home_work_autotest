import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


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

base_url = "https://demoqa.com/browser-windows"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением


#Работа с вкладками и окнами
driver.find_element(By.XPATH, "//button[@id='tabButton']").click() #Нажатие кнопки открытия новой вкладки
print("Кнопка открытия вкладки нажата")
driver.switch_to.window(driver.window_handles[1]) #Переход на новую вкладку
time.sleep(1) #Задержка исполнения кода
new_tab_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text #Текст для проверки на новой вкладке
assert new_tab_text == "This is a sample page", "Текст на новой странице не совпадает с требуемым"
print("Переход на новую вкладку осуществлен")
driver.switch_to.window(driver.window_handles[0]) #Переход на первую страницу
time.sleep(1) #Задержка исполнения кода

driver.find_element(By.XPATH, "//button[@id='windowButton']").click() #Нажатие кнопки открытия нового окна
print("Кнопка открытия нового окна нажата")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.window(driver.window_handles[2]) #Переход в новое окно
new_window_text = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']").text #Текст для проверки в новом окне
assert new_window_text == "This is a sample page", "Текст на новой странице не совпадает с требуемым"
print("Переход в новое окно осуществлен")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.window(driver.window_handles[0]) #Переход на первую страницу

time.sleep(3) #Задержка исполнения кода
driver.close()