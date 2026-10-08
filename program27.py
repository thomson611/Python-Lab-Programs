names = input("Enter the names seperated by space:").split()
count = 0
for name in names:
    count+=name.count("a")
print("names :",names)
print("occurences of 'a':",count)


