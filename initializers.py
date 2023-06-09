class Employee:
    # define the properties and assigning them
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department
        
        
#cretee the object of Employee class with default parameters
praveen = Employee(121,20000,"Software Engineer")

# printing the properties of the praveen
print("ID: ", praveen.ID)
print("Salary: ", praveen.salary)
print("Department: ", praveen.department)
 