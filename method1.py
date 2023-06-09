'''
There are 3 types of methods in python:
======================================
1. Instance methods
2. Class methods
3. Static methods

Note: We will be discussing instance methods in this lesson since they are used the most in Python OOP. We will be using the term methods for instance methods since they are most commonly used. Class methods and static methods will be named explicitly as they are.

Definition:
A method is a group of statements that performs some operations and may or may not return a result.

Method parameters:
Method parameters make it possible to pass values to the method. In Python, the first parameter of the method should ALWAYS be self

Return statement:
The return statement makes it possible to get the value from the method.

Note: There is no need to specify the return type since data types are not specified in Python.

The self argument:
One of the major differences between functions and methods in Python is the first argument in the method definition. Conventionally, this is named self. The user can use different names as well, but self is used by almost all the developers working in Python. We will also be using this convention for ease of understanding.
This pseudo-variable provides a reference to the calling object, that is the object to which the method or property belongs to. If the user does not mention the self as the first argument, the first parameter will be treated for reference to the object.

Note: The self argument only needs to be passed in the method definition and not when the method is called.
'''
print("Given below is an example of implementing methods in a class:")
class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department
        
    def tax(self):
        tax = self.salary*0.2
        return tax
    
    def salaryPerDay(self):
        per_day_sal = self.salary/30
        return per_day_sal
    
# initialize an object of the Employee class
praveen = Employee(3789, 2500, "HR")

#printing properties
print("ID: ", praveen.ID)
print("salary:", praveen.salary)
print("Departmnt: ",praveen.department) # class instance
print("tax pay by praveen: ",praveen.tax()) # method call
print("salary per day of praveen: ", praveen.salaryPerDay()) 

'''
# Method Overloading
>Overloading refers to making a method perform different operations based on the nature of its arguments.

Unlike in other programming languages, methods cannot be explicitly overloaded in Python but can be implicitly overloaded.

'''
print("\n\nMethod Overloading:\n")
class Employee1:
    # defining the proprties and asigning them None
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department
        
    #method overloading
    def demo(self, a,b,c,d=5,e=None):
        print("a =",a)
        print("b =",b)
        print("c =",c)
        print("d =",d)
        print("e =",e)
        
    def tax(self, title=None):
        return (self.salary*0.2)
    
    def salaryPerDay(self):
        return (self.salary/30)
    
praveen = Employee1()

#printing properties of the Employee class
print("Demo 1:")
praveen.demo(1,2,3)
print("\n")

print("Demo 2")
praveen.demo(1,2,3,4)
print("\n")

print("Demo 3")
praveen.demo(1,2,3,4,5)

'''
# Advantages of method overloading
One might wonder that we could simply create new methods to perform different jobs rather than overloading the same method. However, under the hood, overloading saves us memory in the system. Creating new methods is costlier compared to overloading a single one.

Since they are memory-efficient, overloaded methods are compiled faster compared to different methods, especially if the list of methods is long.

An obvious benefit is that the code becomes simple and clean. We don’t have to keep track of different methods.

Polymorphism is a very important concept in object-oriented programming. Method overloading plays a vital role in its implementation.
'''
