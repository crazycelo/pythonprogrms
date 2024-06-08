X=input("enter 3 items price:").split()
print(X)
x=int(X[0])
y=int(X[1])
z=int(X[2])
if x==y:
    discount=(x+y)*10/100
    print(discount)
elif y==z:
    discount=(y+z)*10/100
    print(discount)
elif z==x:
    discount=(z+x)*10/100
    print(discount)
else:
    print("notyet")
    discount=0
total= (x+y+z)-discount
print(total)           
    