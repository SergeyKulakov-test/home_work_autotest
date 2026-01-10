import glob
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

path_download = "C:\\Users\\user\\PycharmProjects\\Auto-test-project\\files_download\\"

#Драйвера браузера Chrome, настройки
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# Опции для отключения проверки утечки паролей, скачивания файлов
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,  # Отключаем обнаружение утечек
    'download.default_directory' : path_download
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--password-store=basic")

driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)

base_url = "https://www.lambdatest.com/selenium-playground/download-file-demo"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

driver.find_element(By.XPATH, "//button[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection']").click() #Закрываем куки

#Скачивание файлов
driver.find_element(By.XPATH, "//button[contains(text(), 'Download File')]").click() #Нажатие кнопки для скачивания файла
print("Кнопка скачивания файла нажата")
time.sleep(1) #Задержка исполнения кода

file_name = "LambdaTest.pdf" #Название файла
file_path = path_download + file_name #Путь к файлу
assert os.access(file_path, os.F_OK) == True, "Файл отсутствует в указанной директории"
print("Файл скачан")

files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    a = os.path.getsize(file)
    if a > 10:
        print("Файл не пуст")
    else:
        print("Файл пуст")
files = glob.glob(os.path.join(path_download, "*.*"))
for file in files:
    os.remove(file)
assert os.access(file_path, os.F_OK) == False, "Файл не удален"
print("Файл удален из дериктории")

time.sleep(3) #Задержка исполнения кода
driver.close()