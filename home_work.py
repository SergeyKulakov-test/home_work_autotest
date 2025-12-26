import time
import datetime

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

base_url = "https://www.saucedemo.com/"  #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

#Ввод не корректных данных
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #Поиск поля Username(input)
user_name.send_keys("standard") #Заполнение поля Username не корректными данными
print("Ввод некорректного логина (поле Username)")

user_password = driver.find_element(By.XPATH, "//input[@id='password']") #Поиск поля Password (input)
user_password.send_keys("secret") #Заполнение поля Password не корректными данными
print("Ввод некорректного пароля (поле Password)")

#Удаление заполненых полей
user_name.send_keys(Keys.CONTROL + 'a') #Выдиляем поле Username
user_name.send_keys(Keys.DELETE) #Очищаем поле Username
print("Очистка логина (поле Username)")

user_password.send_keys(Keys.CONTROL + 'a') #Выдиляем поле Password
user_password.send_keys(Keys.DELETE) #Очищаем поле Password
print("Очистка пароля (поле Password)")

#Ввод корректных данных
user_name.send_keys("standard_user") #Заполнение поля Username корректными данными
print("Ввод корректного логина (поле Username)")

user_password.send_keys("secret_sauce") #Заполнение поля Password не корректными данными
print("Ввод корректного пароля (поле Password)")

#Авторизация/вход
button_login = driver.find_element(By.ID, "login-button") #Поиск кнопки Login
button_login.send_keys(Keys.ENTER) #Нажатие кнопки Login
print("Нажатие на кнопку Login")

#Добавление товаров в корзину
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click() #Добавление в корзину первого товара
print("Первый товар добавлен в корзину")
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click() #Добавление в корзину второго товара
print("Второй товар добавлен в корзину")

#Сохранение в переменные названия товаров
name_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text #Название первого товара
print(name_product_1)
name_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text #Название второго товара
print(name_product_2)

#Подготока переменной для проверки суммы товаров
value_price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div").text.split("$")[1] #Цена первого товара
print(f'Цена первого товара {value_price_product_1}')
value_price_product_2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div").text.split("$")[1] #Цена второго товара
print(f'Цена второго товара {value_price_product_2}')
summ_price_products = float(value_price_product_1) + float(value_price_product_2) #Сумма товаров отправленных в корзину
print(f'Сумма цен двух товаров {summ_price_products}')

#Переход в корзину
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
print("Кнопка корзины нажата")

#Переход к оформлению
driver.find_element(By.XPATH, "//*[@id='checkout']").click() #Нажатие кнопки Checkout
print("Кнопка Checkout нажата")

#Заполнение данных
driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("Garry") #Заполнение поля First-name
print("Поле First-name заполнено")

driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("Potter") #Заполнение поля Last-name
print("Поле Last-name заполнено")

driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys(16798) #Заполнение поля Postal Code
print("Поле Postal Code заполнено")

#Подтверждение
driver.find_element(By.XPATH, "//*[@id='continue']").click() #Нажатие кнопки Continue
print("Кнопка Continue нажата")

#Проверка названия товааров на странице заказов
cart_name_product_1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").text #Название первого товара в корзине
print(cart_name_product_1)
assert cart_name_product_1 == name_product_1, "Название первого товара не совпадает с добавленным в корзину"
print("Название первого твара совпадает")

cart_name_product_2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text #Название второго товара в корзине
print(cart_name_product_2)
assert cart_name_product_2 == name_product_2, "Название второго товара не совпадает с добавленным в корзину"
print("Название второго твара совпадает")

#Проверка цен товааров
cart_value_price_product_1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text.split("$")[1] #Цена первого товара в корзине
print(f'Цена первого товара в корзине {cart_value_price_product_1}')
assert cart_value_price_product_1 == value_price_product_1, "Цена первого товара не совпадает с добавленным в корзину"
print("Цена первого твара совпадает")

cart_value_price_product_2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div").text.split("$")[1] #Цена первого товара в корзине
print(f'Цена второго товара в корзине {cart_value_price_product_2}')
assert cart_value_price_product_2 == value_price_product_2, "Цена второго товара не совпадает с добавленным в корзину"
print("Цена второго твара совпадает")

cart_summ_price_products = float(driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]").text.split("$")[1]) #Сумма товаров
print(f'Сумма цен двух товаров {cart_summ_price_products}')
assert cart_summ_price_products == (summ_price_products), "Сумма товаров не совпадает с суммой цен"
print("Сумма цен товаров совпадает с итоговой")

#Завершение оформления
driver.find_element(By.XPATH, "//*[@id='finish']").click() #Нажатие кнопки Finish
print("Кнопка Finish нажата")

value_checkout_complete = driver.find_element(By.XPATH, "//*[@id='checkout_complete_container']/h2").text #Поиск текста для проверки загрузки страницы
assert value_checkout_complete == "Thank you for your order!", "Текст на странице не найден, страница не загрузилась"
print("Страница загрузилась, заказ оформлен")

time.sleep(2) #Задержка исполнения кода
driver.close()
