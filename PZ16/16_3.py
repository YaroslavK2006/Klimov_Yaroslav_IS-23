# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате.

import pickle

class Product:
    def __init__(self, name, price, quantity):
        self.name = name # Установка имени продукта
        self.price = price # Установка цены продукта
        self.quantity = quantity # Установка количества продукта

    def display_info(self):
        print(f"Название: {self.name},"
              f" Цена: {self.price},"
              f" Количество: {self.quantity}")

# Создание объектов класса Product
product1 = Product("Apple", 1500, 5)
product2 = Product("Banana", 1000, 10)
product3 = Product("Orange", 1200, 8)

def save_def(products, filename): # Функция для сохранения списка продуктов в файл
    with open(filename, 'wb') as file: # Открытие файла для записи
        pickle.dump(products, file)

def load_def(filename):  # Функция для загрузки списка продуктов из файла
    with open(filename, 'rb') as file:  # Открытие файла для чтения
        return pickle.load(file)

save_def([product1, product2, product3], 'products.pkl') # Сохранение списка продуктов в файл 'products.pkl'

loaded_products = load_def('products.pkl')

for product in loaded_products:
    product.display_info() # Вывод информации о загруженных продуктах