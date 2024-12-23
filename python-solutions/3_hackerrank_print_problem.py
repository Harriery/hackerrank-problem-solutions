# 3- https://www.hackerrank.com/challenges/python-print/problem
list_number =[]
n = int(input("enter a number"))

for i in range(1, n+1):
    list_number.append(i)
    

str_number ="".join(map(str, list_number))
print(str_number)


# input(): Takes an integer n from the user.
# range(): Generates numbers from 1 to n.
# append(): Adds each number to the list (list_number).
# map(): Converts all list elements to strings.
# join(): Combines the string elements into a single string without spaces.