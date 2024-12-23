# 2. https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem



arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()
print(arr[-2])

# arr = list(map(int, input().split())) : We split the data received from the user by spaces, convert each element to an integer and convert it to a list.
# arr = list(set(arr))                  : We used set() to remove duplicate numbers in the list. Set keeps only unique elements.
# arr.sort()                            : We sorted the list, with the largest element coming last.
# arr[-2]                               : We get the second largest number, the element before the end of the list.