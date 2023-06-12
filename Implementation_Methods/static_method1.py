class Dates:
    def __init__(self,date):
        self.date = date
        
    def getDate(self):
        return self.date
    
    @staticmethod #optional for static method
    def change_format(date):
        return date.replace("/","-")
    
    
date = Dates("10-12-1995")
print(date.getDate())

db_date = "10/12/1995"
dateWithDash = Dates.change_format(db_date)
print(dateWithDash)