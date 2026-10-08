list_1=[]
n = int(input("Enter the limit:"))
for i in range(0,n):
    num= int(input("Enter the number:"))
    list_1.append(num)
list_2=[]
n = int(input("Enter the limit:"))
for i in range(0,n):
    num = int(input("Enter the number:"))
    list_2.append(num)
print("List1:",list_1)
print("List2:",list_2)
if(len(list_1) == len(list_2)):
     print("Length of List1 and List2 are equal")
else:
     print("Length of List1 and List2 are not equal")
sum1 = 0
sum2 = 0
for i in list_1:
    sum1+=i
print("Sum of first list:",sum1)
for i in list_2:
    sum2+=i
print("Sum of second list:",sum2)
if(sum1 == sum2):
    print("Sum of both lists are equal")
else:
    print("Sum of both lists are not equal")
common = []
for i in list_1:
    if i in list_2 and i not in common:
        common.append(i)
if common:
    print("The same value occured in both lists are",common)
else:
    print("No common value")
