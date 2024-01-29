str=input("enter the string:")
result=""
for j in range(len(str)):
    result+=str[j].upper()+str[j]*j+'-'
print(result)
        
