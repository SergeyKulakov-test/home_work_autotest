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

base_url = "https://the-internet.herokuapp.com/javascript_alerts"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением


#Работа с Alert
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click() #Нажатие кнопки для вызова Alert
print("Кнопка вызова Alert нажата")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.alert.accept() #Закрытие окна Alert
print("Alert закрыт")
value_accept_alert = driver.find_element(By.XPATH, "//p[@id='result']").text
assert value_accept_alert == "You successfully clicked an alert", "Текст после закрытия Alert не совпадает"
print("Alert закрыт успешно")

driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click() #Нажатие кнопки для вызова Confirm
print("Кнопка вызова Confirm нажата")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.alert.dismiss() #Закрытие окна Confirm
print("Confirm закрыт")
value_dismiss_confirm = driver.find_element(By.XPATH, "//p[@id='result']").text
assert value_dismiss_confirm == "You clicked: Cancel", "Текст после закрытия Confirm не совпадает"
print("Confirm отменен успешно")

text_promt = "Hellow" #Текст для ввода в окно Prompt
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click() #Нажатие кнопки для вызова Prompt
print("Кнопка вызова Prompt нажата")
time.sleep(1) #Задержка исполнения кода
driver.switch_to.alert.send_keys(text_promt) #ввод текста
print(text_promt)
driver.switch_to.alert.accept() #Закрытие окна Prompt
print("Prompt закрыт")
value_accept_prompt = driver.find_element(By.XPATH, "//p[@id='result']").text
assert value_accept_prompt == f"You entered: {text_promt}", "Текст после закрытия Prompt не совпадает"
print("Prompt закрыт успешно")

time.sleep(3) #Задержка исполнения кода
driver.close()