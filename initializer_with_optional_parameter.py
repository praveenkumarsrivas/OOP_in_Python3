class Employee:
    # define the properties and assigning them ith optional params
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department
        
        
# creating an object of the employee class with default param
praveen = Employee()
vipin = Employee(125,20000,"HR")

print("praveen")
print("ID: ",praveen.ID)
print("salary: ",praveen.salary)
print("Department: ", praveen.department)

print("Vipin")
print("ID: ",vipin.ID)
print("salary: ",vipin.salary)
print("Department: ",vipin.department)
