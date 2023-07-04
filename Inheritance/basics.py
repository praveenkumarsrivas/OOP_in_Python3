class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print("manufacturer: ",self.make)
        print("color: ", self.color)
        print("Model: ",self.model)
        
class Car(Vehicle):
    def __init__(self,make,color, model, doors):
        Vehicle.__init__(self,make,color,model)
        self.doors=doors
        
    def printCarDetails(self):
        self.printDetails()
        print("Doors: ",self.doors)
        
obj1 = Car("Suzuki", "Grey","2020",4)
obj1.printCarDetails()