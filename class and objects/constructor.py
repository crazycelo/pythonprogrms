class user:
    def __init__(self,name):
        self.name=name
    def printall(self):
        print("Name:",self.name) 

o=user("celine")
o.printall()
print(o.__dict__)
o1=user("ambrose")
o1.printall()
print(o1.__dict__)
          

