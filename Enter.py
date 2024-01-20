class People:
    def __init__(self, head_center_x, head_center_y, head_radius, torso_x, torso_y, torso_width, torso_height, arm_length, leg_length):
        self._head_center_x = head_center_x
        self._head_center_y = head_center_y
        self._head_radius = head_radius
        self._torso_x = torso_x
        self._torso_y = torso_y
        self._torso_width = torso_width
        self._torso_height = torso_height
        self._arm_length = arm_length
        self._leg_length = leg_length

    # Геттеры
    def get_head_center(self):
        return (self._head_center_x, self._head_center_y)

    def get_head_radius(self):
        return self._head_radius

    def get_torso_dimensions(self):
        return (self._torso_x, self._torso_y, self._torso_width, self._torso_height)

    def get_arm_length(self):
        return self._arm_length

    def get_leg_length(self):
        return self._leg_length

    # Сеттеры с проведением контроля правильности значений
    def set_head_center(self, x, y):
        self._head_center_x = x
        self._head_center_y = y

    def set_head_radius(self, radius):
        if radius > 0:
            self._head_radius = radius
        else:
            print("Ошибка: Радиус должен быть положительным числом.")

    def set_torso_dimensions(self, x, y, width, height):
        if width > 0 and height > 0:
            self._torso_x = x
            self._torso_y = y
            self._torso_width = width
            self._torso_height = height
        else:
            print("Ошибка: Ширина и высота должны быть положительными числами.")

    def set_arm_length(self, length):
        if length > 0:
            self._arm_length = length
        else:
            print("Ошибка: Длина руки должна быть положительным числом.")

    def set_leg_length(self, length):
        if length > 0:
            self._leg_length = length
        else:
            print("Ошибка: Длина ноги должна быть положительным числом.")

    def calculate_height(self):
        # Рост = высота туловища + длина ноги
        return self._torso_height + self._leg_length + self._head_radius + self._head_radius

# Создаем экземпляры класса Person
person1 = People(head_center_x = int(input("x головы ")), head_center_y = int(input("y головы ")), head_radius = int(input("Радиус головы ")), torso_x = int(input("тело x ")), torso_y = int(input("тело y ")), torso_width = int(input("Длина тела ")), torso_height = int(input("Высота тела ")), arm_length = int(input("Длина рук ")), leg_length = int(input("Длина ног ")))
person2 = People(5, 5, -1, 2, 3, 12, 22, 17, 27)

# Выводим информацию о свойствах объектов
print("Чел1")
print("Цент головы:", person1.get_head_center())
print("Радиус головы", person1.get_head_radius())
print("Пропорции тела", person1.get_torso_dimensions())
print("Руки:", person1.get_arm_length())
print("Ноги:", person1.get_leg_length())
print("Рост:", person1.calculate_height())

print("\nЧел2:")
print("Центр Головы:", person2.get_head_center())
print("Радиус:", person2.get_head_radius())
print("Пророрции тела", person2.get_torso_dimensions())
print("Руки:", person2.get_arm_length())
print("Ноги:", person2.get_leg_length())
print("Рост:", person2.calculate_height())