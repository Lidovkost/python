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



    
        
    