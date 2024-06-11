class NoteTwo:
    count = 0

    def init(self, content, is_completed=False):
        self.content = content
        self.is_completed = is_completed
        NoteTwo.count += 1

    @classmethod
    def reset_count(cls):
        cls.count = 0


# Создание экземпляра с новым атрибутом
note = NoteTwo("Sample content", is_completed=True)

# Вывод значений собственных атрибутов экземпляра
print(note.dict)

# Увеличение счетчика на величину, передаваемую в качестве аргумента
increment_amount = 5
NoteTwo.count += increment_amount

# Проверка содержимого магической переменной dict
print(NoteTwo.dict)