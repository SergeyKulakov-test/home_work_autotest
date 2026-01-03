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

base_url = "https://the-internet.herokuapp.com/horizontal_slider"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Перемещение ползунка
actions = ActionChains(driver)

slider = driver.find_element(By.XPATH, "//input[@type='range']") #Поиск ползунка на странице
actions.click_and_hold(slider).move_by_offset(-20, 0).release().perform() #Передвижение ползунка на 800 пикселей в лево
print("Произведено перемещение ползунка в лево")

#Проверка значекний после перемещения ползунка
value_slider = slider.get_attribute('value') #Значение ползунка внутри инпута
print(f"Значение в инпуте {value_slider}")
text_value_slider = driver.find_element(By.XPATH, "//span[@id='range']").text #Значение ползунка отображемые на странице
print(f"Значение на странице {text_value_slider}")
assert value_slider == text_value_slider, "Значение ползука не совпадает со значением на странице"
print(f"Значения совпадают")

time.sleep(3) #Задержка исполнения кода
driver.close()
