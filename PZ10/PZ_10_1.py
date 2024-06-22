#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар, печенье, сыр. Пятерочка – мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар, печенье. Лента – печенье, молоко, сыр. Определить:
# 1. в каких магазинах нельзя приобрести соль.
# 2. в каких магазинах можно приобрести одновременно молоко, печенье и сыр.
# 3. в каких магазинах можно приобрести мясо и молоко.

# Создаются данные о магазинах и товарах
magaziny = {'Магнит': {'молоко', 'соль', 'сахар', 'печенье', 'сыр'},
    'Пятерочка': {'мясо', 'молоко', 'сыр'},
    'Перекресток': {'молоко', 'творог', 'сыр', 'сахар', 'печенье'},
    'Лента': {'печенье', 'молоко', 'сыр'}}

# Извлекаются магазины, где нет товара соль
magaziny_bez_sol = {magazin for magazin, tovary in magaziny.items() if 'соль' not in tovary}
print(f'1. Нельзя приобрести соль в: {", ".join(magaziny_bez_sol)}.')

magaziny_s_molokom_pechenem_syrom = {magazin for magazin, tovary in magaziny.items() if {'молоко', 'печенье', 'сыр'}.issubset(tovary)}
print(f'2. Можно приобрести молоко, печенье и сыр в: {", ".join(magaziny_s_molokom_pechenem_syrom)}.')

magaziny_s_myasom_i_molokom = {magazin for magazin, tovary in magaziny.items() if {'мясо', 'молоко'}.issubset(tovary)}
print(f'3. Можно приобрести мясо и молоко в: {", ".join(magaziny_s_myasom_i_molokom)}.')
