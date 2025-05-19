class person():
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)


class employ(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post


        person.__init__(self,name,idnumber)

obj=employ("Abi",101,200000,"Manager")
obj.display()

    
        
