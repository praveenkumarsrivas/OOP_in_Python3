# Definition
**Inheritance** provides a way to create a new class from an existing class. The new class is a specialized version of the existing class such that it inherits all the non-private fields (variables) and methods of the existing class. The existing class is used as a starting point or as a base to create the new class.

## The IS A Relationship
After reading the above definition, the next question that comes to mind is this: **when do we use inheritance?** Wherever we come across an IS A relationship between objects, we can use inheritance.

### we can see the objects have a IS A relationship between them. We can write it as:
- Square IS A shape
- Python IS A programming language
- Car IS A vehicle

So, from the above descriptions of inheritance, we can conclude that we can build new classes by extending existing classes.


|Existing Class|Derived Class|
--------------:|------------:|
|Shape         |Square       |
|Programming Language|Python|
|Vehicle	|Car

# The Python Object class
The primary purpose of object-oriented programming is to enable a programmer to model the real-world objects using a programming language.

In Python, whenever we create a class, it is, by default, a subclass of the built-in Python object class. This makes it an excellent example of inheritance in Python. This class has very few properties and methods, but it does provide a strong basis for object-oriented programming in Python.

# The terminologies
In inheritance, in order to create a new class based on an existing class, we use the following terminology:

**Parent Class (Super Class or Base Class):** This class allows the reuse of its public properties in another class.

**Child Class (Sub Class or Derived Class):** This class inherits or extends the superclass.

>A child class has all public attributes of the parent class.

# Syntax
In Python, to implement inheritance, the syntax is quite similar to the basic class definition. The syntax is given below:
```python
class ParentClass:
    # attributes of the parent class


class ChildClass(ParentClass):
    # attributes of the child class
```
The name of the parent class is written in brackets after the name of the child class , which is followed by the body of the child class.

## Example
Let’s take an example of a Vehicle class as the parent class and implement a Car class that will extend from this Vehicle class. Because a Car IS A vehicle, the implementation of inheritance relation between these classes will stand valid.
```python
class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        # calling the constructor from parent class
        Vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()
```
