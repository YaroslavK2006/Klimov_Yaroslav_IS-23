# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во"


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Название: {self.name},"
              f" Цена: {self.price},"
              f" Количество: {self.quantity}")


# Создаем объект класса "Товар"
product = Product("Apple", 10.99, 5)

# Выводим информацию о товаре
product.display_info()