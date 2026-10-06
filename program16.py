n = int(input("Enter a number of terms: "))
a = 0
b = 1
print(a,end = " ")
for i in range(1,n):
  c = a+b
  a = b
  b = c
  print(a,end = " ")
