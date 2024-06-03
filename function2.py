def add(a,b): return(a+b)
def sub(a,b): return(a-b)
def mul(a,b): return(a*b)
def div(a,b): return(a/b)
while True:
    choice=int(input("enter the number:"))
    if choice==1:
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(add(a,b))
    elif choice==2:
        a=int(input("a value:"))
        b=int(input("b value:"))  
        print(sub(a,b))
    elif choice==3:
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(mul(a,b))
    elif choice==4:
        a=int(input("a value:"))
        b=int(input("b value:"))
        print(div(a,b))
    elif choice == 0:
        break    
        
    else:
        print ("invalid number")