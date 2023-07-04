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