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

base_url = "https://www.lambdatest.com/selenium-playground/upload-file-demo" #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением


#Загрузка файла
path_upload = "C:\\Users\\user\\PycharmProjects\\Auto-test-project\\files_upload\\one_file.jpg" #Путь к файлу
driver.find_element(By.XPATH, "//input[@id='file']").send_keys(path_upload) #Загрузка файла
print("Файл добавлен")
upload_file_text = driver.find_element(By.XPATH, "//div[@id='error']").text #Текст после загрузки файла
print(upload_file_text)
assert upload_file_text == "File Successfully Uploaded", "Файл не загружен"
print("Файл загружен успешно")

time.sleep(3) #Задержка исполнения кода
driver.close()