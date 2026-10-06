list=[]
n =int(input("Enter the number of elements: "))
for i in range(0,n):
    num = int(input("Enter a number: "))
    list.append(num)
print("The Squares of the green numbers are:")
for i in range(0,n):
    print(list[i]**2)