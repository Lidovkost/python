class StringValue:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]
       
    def __set__(self, instance, value):
        try:
            if type(value) != str:
                raise ValueError   
            instance.__dict__[self.my_attr] = value
        except ValueError:
            print(f"нельзя присвоить не строку")

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr
class Worker:
    name = StringValue()
    surname = StringValue()
    position = StringValue()
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': None, 'bonus': None}

class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        
    def get_full_name(self):
        """Return worker fullname."""
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        """Return total income of worker.""" 
        return int(self._income['bonus']) + int(self._income['wage'])
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.position}"

student = Position('kostya', 'La', 'student')
professor = Position('Andrey', 'M', 'teacher')
student.name = 1
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
