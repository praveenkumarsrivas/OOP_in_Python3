'''
Access modifiers are tags we can associate with each member to define which parts of the program can access it directly.

There are two types of access modifiers in Python. Let’s take a look at them one by one.
1. Public attributes: Public attributes are those that can be accessed inside the class and outside the class.
2. Private attributes: Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.


Technically in Python, all methods and properties in a class are publicly available by default. If we want to suggest that a method should not be used publicly, we have to declare it as private explicitly.
'''

class Employee:
    def __init__(self, ID, salary):
        #all properties are public
        self.ID = ID
        self.salary = salary
        
    def displayID(self):
        print("ID: ", self.ID)
        
praveen = Employee(159357, 2500)
praveen.displayID() 

print(praveen.salary) # class variables are publicly available

'''
Private attributes: The aim is to keep it hidden from the users and other classes. Unlike in many different languages, it is not a widespread practice in Python to keep the data members private since we do not want to create hindrances for the users. We can make members private using the double underscore __ prefix
'''
# print("==Implementing private access modifier:==\n")
# class Employee1:
#     comapny_name='Google'
#     def __init__(self,ID, salary):
#         self.ID = ID
#         self.__salary = salary # salary is private property
#     # @classmethod 
#     def get_info(cls):
#         print(cls.comapny_name)
#         print(cls.salary) # this info will not be available will through an error
        
    
# p1 = Employee1(58746, 50000)
# p1.get_info()

'''
Private methods:We can make method private using the double underscore __ prefix

Why private methods?
Consider a real-life example, a car engine, which is made up of many parts like spark plugs, valves, pistons, etc. No user uses these parts directly, rather they just know how to use the parts which use them. This is what private methods are used for. It is used to hide the inner functionality of any class from the outside world. Private methods are those methods that should neither be accessed outside the class nor by any base class. In Python, there is no existence of Private methods that cannot be accessed except inside a class. However, to define a private method prefix the member name with the double underscore “__”. Note: The __init__ method is a constructor and runs as soon as an object of a class is instantiated. 
'''

print("==Implementing private method modifier:==\n") 
class Employee2:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary # private property
        
    def displaySalary(self):
        print("salary: ", self.__salary) # can access salary
        
    def __displayID(self):
        print("ID: ", self.ID)
    
    def __getID(self):
        return self.ID
        
    def updateID(self):
        id = self.__getID()
        return id+500
        
p2 = Employee2(3758, 100000)
p2.displaySalary()
print("Updated ID: ",p2.updateID())
# p2.__displayID() # not allowed


'''
Accessing private attributes in the main code
As discussed above, it is not common to have private variables in Python.

Properties and methods with the __ prefix are usually present to make sure that the user does not carelessly access them. Python allows for free hand to the user to avoid any future complications in the code. If the user believes it is absolutely necessary to access a private property or a method, they can access it using the _<ClassName> prefix for the property or method.
'''
print("==Accessing private attributes in the main code==")

class Employee3:
    def __init__(self,ID, salary):
        self.ID = ID
        self.__salary = salary
        
p3 = Employee3(125698,55000)
print(p3._Employee3__salary)

'''
Not so protected:
Protected properties and methods in other languages can be accessed by classes and their subclasses. Python does not have a strict rule for accessing properties and methods, so it does not have the protected access modifier.
'''

