dict = { }
n = int(input("Enter a number of elements: "))
for i in range(n):
    key = input("Enter a key: ")
    value = input("Enter  value: ")
    dict[key] = value
print("The dictionary is",dict)
disc_asc = sorted(dict.items())
print("Dictionary in ascending order:",disc_asc)
dict_desc = sorted(dict.items(),reverse = True)
print("Dictionary in descending order:",dict_desc)
