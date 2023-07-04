class Circle:
    # Insert your code here
    def __init__(self, radius):
        self.radius= radius
    def area(self):
        return 3.14*(self.radius*self.radius)
    
c = Circle(11)
print(c.area())