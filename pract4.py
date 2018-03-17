num=int(input("enter a number of your choice:"))
x= list(range(2,50))
for y in x:
    if num%y==0:
       print(y)
    else:
       print("no number available")
