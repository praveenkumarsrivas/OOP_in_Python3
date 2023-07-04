class User:
    def __init__(self, username=None): # defininf initializer
        self.__username = username
        
    def setUsername(self, x):
        self.__username = x
        
    def getUsername(self):
        return (self.__username)
    
    
p1 = User('Praveen')
print("Before setting: ",p1.getUsername())
p1.setUsername("praveen Srivas")
print("After setting: ",p1.getUsername())
