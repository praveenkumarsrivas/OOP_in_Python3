class Player:
    teamName="Globe" # class variable
    
    def __init__(self, name):
        self.name = name # instance variable
        
p1 = Player("praveen")
print("Name: {}\nTeam Name: {}".format(p1.name,p1.teamName))

p2 = Player("vipin")
print("Name: {}\nTeam Name: {}".format(p2.name,p2.teamName))

#-------------------------------------------------------------------------------------------
# Wrong usage of class variable
print("\n\nWrong usage of class variable:")
class Player1:
    formerTeams = []
    teamName = "Globe"
    def __init__(self, name):
        self.name = name
        
p1 = Player1("praveen")
p1.formerTeams.append("HuJ")
print("Name: {}\nTeam Name: {}".format(p1.name,p1.teamName))
print("Former teamName:",p1.formerTeams)

p2 = Player1("vipin")
p2.formerTeams.append("PuJ")
print("Name: {}\nTeam Name: {}".format(p2.name,p2.teamName))
print("Former teamName:",p2.formerTeams)

'''In the example above, while the instance variable name is unique for each and every object of the Player class, the class variable, formerTeams, can be accessed by any object of the class and is updated throughout. We are storing all players currently playing for the same team, but each player in the team may have played for different former teams.'''


#-------------------------------------------------------------------------------------------------
'''
To avoid this issue, the correct implementation of the example above will be the following:
'''
# Correct usage of class variable
print("\nCorrect usage of class variable:")

class Player2:
    teamName = 'Globe'
    def __init__(self,name):
        self.name = name
        self.formerTeams = []
        
p1 = Player2("praveen")
p1.formerTeams.append("HuJ")
print("Name: {}\nTeam Name: {}".format(p1.name,p1.teamName))
print("Former teamName:",p1.formerTeams)


p2 = Player2("vipin")
p2.formerTeams.append("PuJ")
print("Name: {}\nTeam Name: {}".format(p2.name,p2.teamName))
print("Former teamName:",p2.formerTeams)

'''
Now the property formerTeams is unique for each Player class object and can only be accessed by that unique object.
'''

# Using class variables smartly
print("\nUsing class variables smartly")
'''
Class variables are useful when implementing properties that should be common and accessible to all class objects. Let’s see an example of this:
'''
class Player3:
    teamName = 'Globe'
    teamMember = []
    
    def __init__(self,name):
        self.name = name
        self.formerTeams = []
        self.teamMember.append(self.name)
        
p1 = Player3("praveen")
p2 = Player3("vipin")
p1.formerTeams.append("form1")
print("Name: {}\nTeam Name: {}\nTeam Member: {}".format(p1.name,p1.teamName, p1.teamMember))
print("Former teamName:",p1.formerTeams)

p2.formerTeams.append("form2")     
print("Name: {}\nTeam Name: {}\nTeam Member: {}".format(p2.name,p2.teamName, p2.teamMember))
print("Former teamName:",p2.formerTeams)