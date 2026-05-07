# 1 Create a tuple containing five different numbers and display it.
t=(1,2,3,4,5)
print(t)
# 2 Access the first and last element of a tuple.
print("printing the 1 and last index of tuple :-",t[0],end=' ')
print(t[-1])
# 3 Find the total number of elements present in a tuple.
print("Total number of element in tuple is :-",len(t))
# 4 Check whether a given value exists inside a tuple.
target=3
print("It target is present or not:- ",target in t)
# 5 Concatenate two tuples and print the new tuple.
t2=(6,7,8,9)
t3=t+t2
print("Concatinating the tuple",t3)
# 6 Repeat a tuple two times using an operator.
print(f"Repeting the tuple 2 times :-{t*2}")
# 7 Find the index of a specific element in a tuple.
target=4
for i in range(len(t)):
    if target==t[i]:
        print(f"index of the target is {i}")
# 8 Count how many times a particular value appears in a tuple.
t4=(1,2,2,3,5,2)
target=2
count=0
for i in t4:
    if(i==target):
        count=count+1
print(f"Target is {target} and it appear {count} times")
# 9 Slice a tuple to display elements from index 1 to 4.
print(f"Sliced list from index 1 to 4 is {t[1:4]}")
# 10 Iterate through all elements of a tuple using a loop.
print("Iterating all the elements from the list using loop :-")
for i in t:
    print(i)