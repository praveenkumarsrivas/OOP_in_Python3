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
