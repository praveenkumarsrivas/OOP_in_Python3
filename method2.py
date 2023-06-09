## Class Methods and Static Methods
'''Methods in a Python class
In Python classes, we have three types of methods: instance methods, class methods, and static methods.
'''
# Class methods
'''
Class methods work with class variables and are accessible using the class name rather than its object. Since all class objects share the class variables, class methods are used to access and modify class variables.

Note: Class methods are accessed using the class name and can be accessed without creating a class object.
'''
#Syntax
'''
To declare a method as a class method, we use the decorator @classmethod. cls is used to refer to the class just like self is used to refer to the object of the class. You can use any other name instead of cls, but cls is used as per convention, and we will continue to use this convention.

Note: Just like instance methods, all class methods have at least one argument, cls.
'''
print("Implementation of class method: ")

class Player:
    teamName = 'Globe'
    
    def __init__(self, name):
        self.name = name # creating instance variable
        
    @classmethod
    def getTeamName(cls):
        return cls.teamName
    
obj = Player("praveen")
print(obj.name)
print(Player.getTeamName())
print()

#Static methods
'''
Static methods are methods that are usually limited to class only and not their objects. They have no direct relation to class variables or instance variables. They are used as utility functions inside the class or when we do not want the inherited classes to modify a method definition.

Static methods can be accessed using the class name or the object name.
'''

#Syntax
'''
To declare a method as a static method, we use the decorator @staticmethod. It does not use a reference to the object or class, so we do not have to use self or cls. We can pass as many arguments as we want and use this method to perform any function without interfering with the instance or class variables.
'''

print("Implementation of static method:")

class Player1:
    teamName = 'Globe 1'
    
    @staticmethod
    def demo():
        print("I am a static method.")
        
p1 = Player1()
p1.demo()
Player1.demo()
print()
'''
Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. The purpose of a static method is to use its parameters and produce a useful result.

Suppose that there is a class, BodyInfo, containing information about the physical attributes of a person. We can make a static method for calculating the BMI of any given weight and height:
'''

class BodyInfo:
    @staticmethod
    def bmi(weight, height):
        return weight/(height**2)
    
weight = 75
height = 1.6
print(BodyInfo.bmi(weight,height))
print()

# implementation of the above code using init function
print("Static method with Init function code")
class BodyInfo1:
    #defining the properties and initializing them
    def __init__(self,height,weight):
        self.height=height
        self.weight =weight
    @staticmethod    
    def BMI():
        # return 0
        return (weight/height**2)

b = BodyInfo1(18,80)
print(b.BMI()) # using object
# print(BodyInfo1.BMI()) #using class name


    
