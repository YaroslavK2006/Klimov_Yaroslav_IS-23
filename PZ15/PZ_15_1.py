import sqlite3

# Создание подключения к базе данных
conn = sqlite3.connect('командировочные_расходы.db')
cursor = conn.cursor()

# Создание таблицы "Статьи расходов"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS расходы (
        №_приказа INTEGER,
        Фамилия TEXT,
        Место_командировки TEXT,
        Оплата REAL,
        Аванс REAL,
        Вид_расходов TEXT,
        Сумма_расходов REAL
    )
''')

# Сохранение изменений и закрытие подключения
conn.commit()
conn.close()

print('Таблица "Статьи расходов" успешно создана в базе данных "командировочные_расходы.db"')