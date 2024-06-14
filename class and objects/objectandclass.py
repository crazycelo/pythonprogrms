'''class student():
    name="celine"
    age=20

 # getattr method
print(getattr(student,'name'))
print(getattr(student,'age'))       

#dot notation
print(student.name)
print(student.age)

#setattr
setattr(student,'name','vasanth')
print(student.name)

setattr(student,'gender','male')
print(student.gender)

student.city="salem"
print(student.city)


print(student.__dict__)

#delattr 
delattr(student,'city')
print(student.__dict__)  
 
 # instance attributes in python
class user:
    course = "java"

o=user()         #creating object of the class
print(o.course)
print(o.__dict__)
o.course="c++"          #instance attributes of class
print(o.course)
print(o.__dict__)


#class methods in python
#it's a method calling a function using class name without creating a object
class student:
    name="celine"
    age=20
    
    def printall():
        print("name:",student.name)
        print("age:",student.age)
student.printall()
student.__dict__['printall']()       #another method to call a function
print(getattr(student,'printall'))   #getattr is user to print the binary space of the attributes


#instance method in python
class student:
    name="celine"
    age=20
    
    def printall(self,gender):
        print("name:",student.name)
        print("age:",student.age)
        print("genter:",gender)
o=student()        
student.printall(o,"male")#without creating object
o.printall("male")'''






