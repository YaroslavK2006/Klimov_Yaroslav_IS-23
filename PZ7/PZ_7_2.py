#Дана строка, содержащая полное имя файла. Выделить из этой строки название первого каталога (без символов «\»). Если файл содержится в корневом каталоге, то вывести символ «\»
def extract_directory(filepath): #Объявляется функция с именем extract_directory с одним параметром filepath которая будет извлекать название первого каталога из пути файла
    if "\\" in filepath:
        directories = filepath.split("\\") #Если обратный слеш найден в filepath используется метод split("\") для разделения строки по обратному слешу и создания списка с отдельными каталогами
        return directories[0] #Возвращается первый элемент списка directories который представляет название первого каталога
    else:
        return "\\"


file_path = "C:\\Folder1\\Folder2\\file.txt"
directory_name = extract_directory(file_path) #Вызывается функция extract_directory с аргументом file_path и результат присваивается переменной directory_name
print(f"Название первого каталога: {directory_name}")

