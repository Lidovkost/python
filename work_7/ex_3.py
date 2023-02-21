"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': None, 'bonus': None}

class position(worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
       return int(self._income['bonus']) + int(self._income['wage'])
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.position}"

student = position('Kostya', 'La', 'student')
professor = position('Andrey', 'M', 'teacher')
student._income['wage'] = 1000 
student._income['bonus'] = 100
professor._income['wage'] = 2000 
professor._income['bonus'] = 200
print(student.surname)
print(student.get_full_name())
print(student.get_total_income())
print(professor.get_full_name())
print(professor.get_total_income())
print(professor)
print(student)



    
        
    