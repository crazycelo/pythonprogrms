x=int(input("enter the number of books:"))
y=int(input("enter the total price of books:"))
z=x*y

#conditions

if x>=2 and x<=4:
    dis=z*10//100
    print(z-dis)
elif x==5:
    dis=z*20//100
    print(z-dis)
elif x>=5:
    dis=z*50//100
    print(z-dis)  
else:
    print(z)      

