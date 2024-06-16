class user:
    def __init__(self,name,age):
        self.name="celine"
        self.age=20

    @property
    def msg(self):
        print(self.name ,"is",self.age,"years old")

o=user()
o.msg()           