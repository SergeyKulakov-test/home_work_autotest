from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#Драйвера браузера Chrome, настройки
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver_crome = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)


#Функция открытия браузера
def open_brauser(brouser_driver):
    driver = brouser_driver
    base_url = "https://www.saucedemo.com/"  #Открываемая страница
    driver.get(base_url)
    driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

    user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #Поиск поля Username(input)
    user_name.send_keys("standard_user") #Заполнение поля Username данными
    print("Ввод логина (поле Username)")

    user_password = driver.find_element(By.XPATH, "//input[@id='password']") #Поиск поля Password (input)
    user_password.send_keys("secret_sauce") #Заполнение поля Password данными
    print("Ввод пароля (поле Password)")

    button_login = driver.find_element(By.ID, "login-button") #Поиск кнопки Login
    button_login.click() #Нажатие кнопки Login
    print("Нажатие на кнопку Login")

    print(driver.current_url) #Вывод Url  страницы
    get_url = driver.current_url #Получение текущего Url страницы для сранения
    url = 'https://www.saucedemo.com/inventory.html' #Ожидаемый Url страницы
    assert url == get_url, "Полученный Url не совпадает с ожидаемым"
    print("Url корректен")

    text_product = driver.find_element(By.XPATH, '//span[@class="title"]') #Находим уникальный элемент страницы
    value_text_product = text_product.text #Получаем текст уникального элемента для сравнения
    assert value_text_product == "Products", "Текст уникального элемента должен совпадать"
    print("Текст элемента корректен")


#Открываем браузер Chrome
open_brauser(driver_crome)



