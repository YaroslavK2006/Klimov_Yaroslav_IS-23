class Note:
    def __init__(self,text):
        self.text = text
        self.count = 0

    def upcount(selfself):
        self.count += 10

note1= Note("Задача 1")
print(note1)
print(note1.__dict__)
print(dir(note1))
print(note1.text)

note1.upcount()
print(note1.count)
note1.upcount()
print(note1.count)

# Привязонные методы
print(note1.upcount)
print(Note.upcount)