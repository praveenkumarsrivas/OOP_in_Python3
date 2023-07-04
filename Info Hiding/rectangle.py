'''
Implement a method, area(), in the Rectangle class that returns the product of length and width. See the formula below:
'''
class Rectangle:
    def __init__(self,length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2*(self.__length + self.__width)
    
    
r = Rectangle(10,20)
print("Area of the rectangel: ",r.area())
print("perimeter of the rectangel: ",r.perimeter())