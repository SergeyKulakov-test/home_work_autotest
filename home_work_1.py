import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

base_url = "https://www.saucedemo.com/" #Открываемая страница
driver.get(base_url)
driver.set_window_size(1200, 900)  #Открытие окна с заданным разрешением

fake = Faker("en_US") #Определяем язык генерации данных

#Работа с явным и неявным ожиданием
#Переменные
username = "standard_user" #Имя для входа
password = "secret_sauce" #Пароль для входа
value_first_name = fake.first_name() #Генерируем имя для оформления заказа
value_last_name = fake.last_name()  #Генерируем фамилию для оформления заказа
value_postal_сode = fake.postcode() #Генерируем код для оформления заказа

products = {
      1 : 'Sauce Labs Backpack',
      2 : 'Sauce Labs Bike Light',
      3 : 'Sauce Labs Bolt T-Shirt',
      4 : 'Sauce Labs Fleece Jacket',
      5 : 'Sauce Labs Onesie',
      6 : 'Test.allTheThings() T-Shirt (Red)'
            }

def enter_to_product_page(str):
    driver.find_element(By.XPATH, f"//div[contains(text(), '{str}')]").click() #Переход на страницу продукта


#Вход в магазин
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") #Поиск поля Username(input)
user_name.send_keys(username) #Заполнение поля Username
print("Ввод  Username")
user_password = driver.find_element(By.XPATH, "//input[@id='password']") #Поиск поля Password (input)
user_password.send_keys(password) #Заполнение поля Password
print("Ввод Password")
time.sleep(2) #Задержка исполнения кода
driver.find_element(By.ID, "login-button").click() #Нажатие кнопки Login
print("Нажатие на кнопку Login")
driver.implicitly_wait(2)
value_text_page = driver.find_element(By.XPATH, "//span[contains(text(), 'Products')]").text
assert value_text_page == "Products", "Текст на странице не найден" #Проверка загрузки страницы
print("Приветствую тебя в нашем интернет - магазине")

#Выбор товара
print("""
      Выбери один из следующих товаров и укажи его номер:
      1 - Sauce Labs Backpack, 
      2 - Sauce Labs Bike Light, 
      3 - Sauce Labs Bolt T-Shirt, 
      4 - Sauce Labs Fleece Jacket, 
      5 - Sauce Labs Onesie, 
      6 - Test.allTheThings() T-Shirt (Red)
      """)
while True:
    try:
        user_input = input()
        number = int(user_input)
        if 0 < number and number <= 6:
            selected_product = products[number]
            print(products[number])
            break # Если успешно, выходим из цикла
        else: print("Введите число от 1 до 6.")
    except ValueError:
        print("Ошибка: Введено не число. Пожалуйста, введите целое число.")

#Добавление товара в корзину
enter_to_product_page(selected_product) #Переход на страницу продукта
value_text_page = driver.find_element(By.XPATH, "//button[contains(text(), 'Back to products')]").text
assert value_text_page == "Back to products", "Текст на странице не найден"  # Проверка загрузки страницы
print("Страница продукта")
value_price_product = float(driver.find_element(By.XPATH, "//div[@data-test='inventory-item-price']").text.replace("$", "")) #Значение цены товара
print(value_price_product)
driver.find_element(By.XPATH, "//button[@id='add-to-cart']").click() #Добавление в корзину
print("Товар в корзине")
time.sleep(2) #Задержка исполнения кода
driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click() #Переход в корзину
print("Переход в корзину")

#Оформление товара
value_text_page = driver.find_element(By.XPATH, "//span[contains(text(), 'Your Cart')]").text
assert value_text_page == "Your Cart", "Текст на странице не найден"  # Проверка загрузки страницы
print("Страница корзины")
time.sleep(2) #Задержка исполнения кода

driver.find_element(By.XPATH, "//button[@id='checkout']").click() #Переход к оформлению
print("Переход к оформлению")

value_text_page = driver.find_element(By.XPATH, "//span[contains(text(), 'Checkout: Your Information')]").text
assert value_text_page == "Checkout: Your Information", "Текст на странице не найден"  # Проверка загрузки страницы
print("Страница заполнения данных")

#Заполнение данных
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']") #Поле имени
first_name.send_keys(value_first_name) #Ввод имени
print(value_first_name)

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']") #Поле фамилии
last_name.send_keys(value_last_name) #Ввод фамилии
print(value_last_name)

postal_сode = driver.find_element(By.XPATH, "//input[@id='postal-code']") #Поле postal-code
postal_сode.send_keys(value_postal_сode) #Ввоод postal-code
print(value_postal_сode)
time.sleep(2) #Задержка исполнения кода

driver.find_element(By.XPATH, "//input[@id='continue']").click() #Переход к оплате
print("Переход к оплате")

value_text_page = driver.find_element(By.XPATH, "//span[contains(text(), 'Checkout: Overview')]").text
assert value_text_page == "Checkout: Overview", "Текст на странице не найден"  # Проверка загрузки страницы
print("Страница оплаты")

#Проверки на странице оплаты
product_name = driver.find_element(By.XPATH, "//div[@class='cart_item_label']/a/div").text #Название товара на странице
assert product_name == selected_product, "Название товара не совпадает"  # Проверка названия товара
print(product_name)

price_product = float(driver.find_element(By.XPATH, "//div[@data-test='subtotal-label']").text.split("$")[1]) #Стоимость товара на странице
assert price_product == value_price_product, "Название товара не совпадает"  # Проверка стоимости товара
print(price_product)

time.sleep(3) #Задержка исполнения кода
driver.close()