class People: # Создаем класс Человек
    def __init__(self, head, tors, arms, legs): # Создаем поля для класса
        self._head = head
        self._tors = tors
        self._arms = arms
        self._legs = legs
    # Создаем методы получения значения полей
    def get_head(self):
        return self._head

    def get_tors(self):
        return self._tors

    def get_arms(self):
        return self._arms

    def get_legs(self):
        return self._legs
    # Создаем методы изменения значения полей
    def set_head(self, value):
        self._head = value

    def set_tors(self, value):
        self._tors = value

    def set_arms(self, value):
        self._arms = value

    def set_legs(self, value):
        self._legs = value

    def people_info(self):
        print("Head:", self._head)
        print("Torso:", self._tors)
        print("Legs:", self._arms)
        print("Legs:", self._legs)
# Создаем обьект класса
person = People(head = input("Введите голову"), tors = input("Введите Тело"), arms = input("Введите Руки"), legs = input("Введите ноги"))
# Выводим его
print("Свойства:")
print("Head:", person.get_head())
print("Torso:", person.get_tors())
print("Arms:", person.get_arms())
print("Legs:", person.get_legs())
# Изменяем значения
vp = input("Хотите изменить?")
if vp == "Да":
    person.set_head(value = input("Введите голову"))
    person.set_tors(value = input("Введите Тело"))
    person.set_arms(value = input("Введите Руки"))
    person.set_legs(value = input("Введите ноги"))
else:
   print("ясно")

#Выводи измененое
print("\nИзменено:")
person.people_info()