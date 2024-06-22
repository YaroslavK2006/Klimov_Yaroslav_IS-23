# Из исходного текстового файла (Dostoevsky.txt) выбрать блок информации за 1857 год и поместить ее в новый текстовый файл



import re

with open('Dostoevsky.txt', 'r') as file:
    text = file.read()


pattern = r'1857 год.*?(\n|$)'

pattern = re.compile(pattern, re.DOTALL)

matches = pattern.findall(text)

with open('1857_year.txt', 'w') as new_file:

    new_file.write('\n'.join(matches))







