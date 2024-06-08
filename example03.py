x=int(input("enter the number:"))
 
five=x//5
fiv=x-(five*5)
two=fiv//2
to=x-(two*2)-(five*5)
one=to

#conditions
if five!=0:
    print("count of Rs 5:",five)
    if two !=0:
        print("count of Rs 2:",two)
        if one !=0:
            print("count of Rs 1:",one)
