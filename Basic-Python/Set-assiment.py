# 1. Create a set of numbers from 1 to 5 and print it.
sets = {1, 2, 3, 4, 5}
print("set printing:- ",sets)
# 2. Add an element to an existing set.
sets.add(6)
print("set add element :- ",sets)   
# 3. Remove an element using remove() and observe what happens if the element does not exist.
sets.remove(3)
print("Set element remove :- ",sets)
try:
    sets.remove(10)
except KeyError:
    print("Element not found in the set.")
# 4. Remove an element using discard() and compare the behavior with remove().
sets.discard(4)
print("Set discard function _- ",sets)
# 5. Find the length of a set.
print("Length of set :- ",len(sets))
# 6. Check if a specific element exists in a set.
print("Element exist in set or not :-",2 in sets) 
# 7. Clear all elements from a set.
sets.clear()
print("Set clear function :- ",sets)
# 8. Convert a list with duplicate values into a set to remove duplicates.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("Unique element in list :- ",unique_set)
# 9. Create an empty set correctly (without using {}).
empty_set = set()
print("Set function :- ",empty_set)

# 10. Iterate through a set and print each element.
sets = {1, 2, 3, 4, 5}
for element in sets:
    print("for loop",element)
    
# 11. Given two sets, find their union.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union :- ",union_set)
# 12. Given two sets, find their intersection.
intersection_set = set1.intersection(set2)
print("intersection :- ",intersection_set)

# 13. Find the difference between two sets.
difference_set = set1.difference(set2)
print("Set Difference :- ",difference_set)

# 14. Find the symmetric difference between two sets.
symmetric_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference :- ", symmetric_diff_set)

# 15. Check whether one set is a subset of another.
print("Check for subset :- ",set1.issubset(set2))

# 16. Check whether one set is a superset of another.
print("Check for superset :- ",set1.issuperset(set2))

# 17. Check whether two sets are disjoint.
print("Check for disjoint set :- ",set1.isdisjoint(set2))

# 18. Update one set with another set.
set1.update(set2)
print("Check for update :- ",set1)

# 19. Remove a random element from a set.
set3 = {1, 2, 3, 4, 5}
random_element = set3.pop()
print("Remove random element from set :- ",sets)

# 20. Find common elements between three sets.
set4 = {4, 5, 6}
common_elements = set1.intersection(set2, set4)
print("intersection of 3 sets :- ",common_elements)

# 21. Given a sentence, find all unique characters using a set.
sentence = "hello world"
unique_chars = set(sentence)
print("All unique character in sentence :- ",unique_chars)

# 22. Count the number of unique words in a paragraph using a set.
para = "This is a sample paragraph. This paragraph contains sample text."
unique_words = set(para.split())
print(len(unique_words))
# 23. Given two lists, return a list of common unique elements using sets.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_unique_elements = list(set(list1).intersection(set(list2)))
print("common unique element in list :- ",common_unique_elements)
# 24. Find elements that appear in either of the two sets but not in both.
symmetric_difference = set(list1).symmetric_difference(set(list2))
print("Symmetric difference set :- ",symmetric_difference)
# 25. Given a list of numbers, find all duplicate elements using sets.
numbers = [1, 2, 2, 3, 4, 4, 5]
duplicates = set([x for x in numbers if numbers.count(x) > 1])
print("duplicate element in list :- ",duplicates)
# 26. Write a program to check if two strings are anagrams using sets.
str1 = "listen"
str2 = "silent"
is_anagram = set(str1) == set(str2)
print("Check for anagram :- ",is_anagram)
# 27. Given a set of numbers, remove all even numbers.
set5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set5 = {x for x in set5 if x % 2 != 0}
print("Set comprehensions for odd/even :- ",set5)
# 28. Create a set comprehension to generate squares of numbers from 1 to 10.
set6 = {x**2 for x in range(1, 11)}
print("Set comprehensions for squares :- ",set6)
# 29. From a given set, create a new set containing only numbers greater than 10.
set7 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
set7 = {x for x in set7 if x > 10}
print("Set comprehensions for more than 10 :- ",set7)
# 30. Given multiple sets in a list, find the intersection of all sets.
set8 = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
intersection = set.intersection(*set8)
print(intersection)
