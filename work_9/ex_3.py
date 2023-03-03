class Singleton(type):
    obj = None
    def __call__(self, *args, **kwargs):
        if self.obj == None:
            self.obj = type.__call__(self, *args)
            for name in kwargs:
                setattr(self.obj, name, kwargs[name])
                self.value = self.obj
            return self.obj
        return self.obj

class Person(metaclass=Singleton):
    def __init__(self, age, name):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"({self.name}, {self.age})"
        
frodo = Person(14, 'fred')
frodix = Person(16, 'kron')
frododo = Person(28, 'krin')
print(frodo, frodix, frododo)