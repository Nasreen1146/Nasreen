x=1
y= 1.0
z='1'
print("type of x is :",type(x),"type of y= is :", type(y),"type of z is :" ,type(z))

a=b=c=5
print("value of a:",a,"value of b:",b, "value of c:", c)


m=5;n=10
print("sum of M+N is",(m+n))

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("second fruit in the list is:",fruits[1], "fourth fruit in the list is:",fruits[3])


numbers = [10, 20, 30, 40, 50]
numbers[2]=35
print("new list:",numbers)

new_tuple=("red", "green", "blue")
print(new_tuple[2])


new_tuple = new_tuple[:1] + ('yellow',) + new_tuple[2:]


coordinates = (10, 20, 30)
x,y,z=coordinates
print(x,y,z)
for blue in new_tuple:
    if blue=="blue":
        print("true")
        break
    else:
        print(" Sorry")

tuple_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(len(tuple_days))

#dictionary

D={"Alice": 85, "Bob": 90, "Charlie": 78}

print(D['Bob'])
#Add and Remove Key-Value Pairs:
del D["Charlie"]
D['david']=90
print(D)

#Update Dictionary Values:
for update in D:
    if update=="Bob":
        D["Bob"]=95
        break

print(D)

#Check if Key Exists in a Dictionary:
for alice in D:
    if D["Alice"]=="Alice":
        print("yes its a key")
    else: print("not a key")

#Dictionary Length:
length_D=len(D)
print(length_D)
