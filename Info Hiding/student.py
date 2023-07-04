'''
Implement the following properties as private:

name
rollNumber
Include the following methods to get and set the private properties above:

getName()
setName()
getRollNumber()
setRollNumber()
Implement this class according to the rules of encapsulation.
''''
class Student:
    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self,rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
    
    
s1 = Student()
s1.setName("Praveen")
s1.setRollNumber("123456")

print("Name: ",s1.getName())
print("Roll Number: ",s1.getRollNumber())