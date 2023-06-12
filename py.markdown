# There are 3 types of methods in python:
1. Instance methods
2. Class methods
3. Static methods

**Note:** We will be discussing instance methods in this lesson since they are used the most in Python OOP. We will be using the term methods for instance methods since they are most commonly used. Class methods and static methods will be named explicitly as they are.

**Definition:**
A method is a group of statements that performs some operations and may or may not return a result.

**Method parameters:**
Method parameters make it possible to pass values to the method. In Python, the first parameter of the method should ALWAYS be self

**Return statement:**
The return statement makes it possible to get the value from the method.

**Note:** There is no need to specify the return type since data types are not specified in Python.

**The self argument:**
One of the major differences between functions and methods in Python is the first argument in the method definition. Conventionally, this is named self. The user can use different names as well, but self is used by almost all the developers working in Python. We will also be using this convention for ease of understanding.
This pseudo-variable provides a reference to the calling object, that is the object to which the method or property belongs to. If the user does not mention the self as the first argument, the first parameter will be treated for reference to the object.

**Note:** The self argument only needs to be passed in the method definition and not when the method is called.
'''
```python
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
```

# Method Overloading
demo