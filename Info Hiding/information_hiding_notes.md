# Information hiding:
 refers to the concept of hiding the inner workings of a class and simply providing an interface through which the outside world can interact with the class without knowing what’s going on inside.

# A real life example:
Let’s apply this to a real-world scenario. Take the doctor-patient model. In the case of an illness, the patient consults the doctor, after which he or she is prescribed an appropriate medicine.

The patient only knows the process of going to the doctor. The logic and reasoning behind the doctor’s prescription are unknown to the patient. A patient will not understand the medical details the doctor uses to reach his/her decision on the treatment.

This is a classic example of the patient class interacting with the doctor class without knowing the inner workings of the doctor class.
The transaction shown above seems relatively straightforward. Data hiding is useful because it can apply the same simplicity to transactions between objects of different classes.

# Encapsulation:
Encapsulation is a fundamental programming technique used to achieve data hiding in OOP.
>In OOP refers to binding data and the methods to manipulate that data together in a single unit, that is, class.

When encapsulating classes, a good convention is to declare all variables of a class private. This will restrict direct access by the code outside that class.

At this point, a question can be raised: If the methods and variables are encapsulated in a class, then how can they be used outside of that class?

The answer to this is simple. One has to implement **public** methods to let the outside world communicate with this class. These methods are called getters and setters. We can also implement other custom methods.

# Advantages of encapsulation
- Classes make the code easy to change and maintain.
- Properties to be hidden can be specified easily.
- We decide which outside classes or functions can access the class properties.

# Get and set
In order to allow controlled access to properties from outside the class, getter and setter methods are used.

>A getter method allows reading a property’s value.

>A setter method allows modifying a property’s value.

It is a common convention to write the name of the corresponding member fields with the get or set command.

```python
class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def setUsername(self, x):
        self.__username = x

    def getUsername(self):
        return (self.__username)


Steve = User('steve1')
print('Before setting:', Steve.getUsername())
Steve.setUsername('steve2')
print('After setting:', Steve.getUsername())
```
In the above class, User, we have defined a private property named __username, which the main code cannot access. Also note that we have started the name of this private property with __.

For this property to interact with any external environment, we have to use the get and set functions. The get function, getUsername(), returns the value of __username, and the setUsername(x) sets the value of __username equal to the parameter x passed.

# Understanding Encapsulation Using Examples
>Encapsulation refers to the concept of binding data and the methods operating on that data in a single unit, which is also called a class.
Consider that we are up for designing an application and are working on modeling the log in part of that application. We know that a user needs a username and a password to log into the application.

An elementary User class will be modeled as:

- Having a property userName
- Having a property password
- A method named login() to grant access

Whenever a new user comes, a new object can be created by passing the userName and password to the constructor of this class.

## A bad example
Now, it is time to implement the above discussed User class

```python
class User:
    def __init__(self, userName = None, password = None):
        self.userName = userName
        self.password = password
        
    def login(self, userName, password):
        if ((self.userName.lower()==userName.lower()) and (self.password == password)):
            print("Access granted")
        else:
            print("Invalid Credentials!")
            
p1 = User("Praveen","123Abc")
p1.login("Praveen","123Abc")

p1.login("Praveen","123789") # login failed
p1.password = "123789" # will change password from outside world
p1.login("Praveen","123789") # login success

# # output:
# Access granted
# Invalid Credentials!
# Access granted
```

In the above coding example, we can observe that anyone can access, change, or print the password and userName fields directly from the main code. This is dangerous in the case of this User class because there is no encapsulation of the credentials of a user, which means anyone can access their account by manipulating the stored data. So, the above code does not follow good coding practices.

## A good example
Let’s move on to a better implementation of the **User** class.

In the code below, an AttributeError will be thrown because the code outside the User class has tried to access a private property.

```python
class User:
    def __init__(self, userName=None, password=None):
        self.__userName = userName
        self.__password = password
        
    def login(self, userName,password):
        if ((self.__userName.lower() == userName.lower()) and (self.__password == password)):
            print("Access granted against username:", self.__userName.lower(),"and password: ",self.__password)

        else:
            print("Invalid credentials!")
            
p1 = User("Praveen","12345")
p1.login("Praveen","12345")

p1.login("Praveen","789456")
p1.__password #AttributeError: 'User' object has no attribute '__password'
```
# Explanation
In the above example, the fields __userName and __password are declared privately using the __ prefix.

We can observe that no one can access, change, or print the __password and __userName fields directly from the main code. This is a proper implementation of encapsulation.

>Note: For encapsulating a class, all the properties should be private and any access to the properties should be through methods such as getters and setters.

This is the concept of encapsulation. All the properties containing data are private, and the methods provide an interface to access those private properties.