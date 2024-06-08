x=int(input("enter a number:"))
if (x%2) != 0:
    print("weird")
elif x>=2 and x<=5:
    print("not weird")
elif x>=6 and x<=20:
    print("weird")
elif x>=20:
    print("not weird")
else:
    print()               