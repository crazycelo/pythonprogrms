dictionary_value={
    "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}

sentence=input("enter:")
list=sentence.split(" ")
def ascii_value(word):
    sum=0
    for i in range(len(word)):
        if word[i] in dictionary_value:
            char=word[i]
            sum+=dictionary_value[char]
     
    return sum
def count(word):
    sum_of=len(word)
    return sum_of
a=0
c=0
for i in range(len(list)):
    if ascii_value(list[i])>count(list[i]):
        a+=1

    else:
        c+=1
if a>=5:
    print("you will get icecream")
else:
    print(" better luck next time")


