from datetime import date
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def calculate_age(cls,name, birth_year):
        # calculate the age and set it as the age
        #return new object
        age = date.today().year - birth_year
        return cls(name, age)
    
    def show(self):
        print(self.name, self.age)
    
    
    
praveen = Student("praveen",25)
praveen.show()
praveen = Student.calculate_age("praveen",1995)
praveen.show()