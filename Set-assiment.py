# 1. Create a set of numbers from 1 to 5 and print it.
my_set = {1, 2, 3, 4, 5}
print(my_set)
# 2. Add an element to an existing set.
my_set.add(6)
print(my_set)   
# 3. Remove an element using remove() and observe what happens if the element does not exist.
my_set.remove(3)
print(my_set)
try:
    my_set.remove(10)  # This will raise a KeyError since 10 is not in the set.
except KeyError:
    print("Element not found in the set.")
# 4. Remove an element using discard() and compare the behavior with remove().
my_set.discard(4)  # This will remove 4 from the set.
print(my_set)
# 5. Find the length of a set.
print(len(my_set))
# 6. Check if a specific element exists in a set.
print(2 in my_set)  # This will return True since 2 is in the set.
# 7. Clear all elements from a set.
my_set.clear()
print(my_set)
# 8. Convert a list with duplicate values into a set to remove duplicates.
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)
# 9. Create an empty set correctly (without using {}).
empty_set = set()
print(empty_set)

# 10. Iterate through a set and print each element.
my_set = {1, 2, 3, 4, 5}
for element in my_set:
    print(element)
# 11. Given two sets, find their union.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print(union_set)
# 12. Given two sets, find their intersection.
intersection_set = set_a.intersection(set_b)
print(intersection_set)

# 13. Find the difference between two sets.
difference_set = set_a.difference(set_b)
print(difference_set)

# 14. Find the symmetric difference between two sets.
symmetric_diff_set = set_a.symmetric_difference(set_b)
print(symmetric_diff_set)

# 15. Check whether one set is a subset of another.
print(set_a.issubset(set_b))

# 16. Check whether one set is a superset of another.
print(set_a.issuperset(set_b))

# 17. Check whether two sets are disjoint.
print(set_a.isdisjoint(set_b))

# 18. Update one set with another set.
set_a.update(set_b)
print(set_a)

# 19. Remove a random element from a set.
my_set = {1, 2, 3, 4, 5}
random_element = my_set.pop()
print(random_element)
print(my_set)

# 20. Find common elements between three sets.
set_c = {4, 5, 6}
common_elements = set_a.intersection(set_b, set_c)
print(common_elements)

# 21. Given a sentence, find all unique characters using a set.
sentence = "hello world"
unique_chars = set(sentence)
print(unique_chars)

# 22. Count the number of unique words in a paragraph using a set.
paragraph = "This is a sample paragraph. This paragraph contains sample text."
unique_words = set(paragraph.split())
print(len(unique_words))
# 23. Given two lists, return a list of common unique elements using sets.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_unique_elements = list(set(list1).intersection(set(list2)))
print(common_unique_elements)
# 24. Find elements that appear in either of the two sets but not in both.
symmetric_difference = set(list1).symmetric_difference(set(list2))
print(symmetric_difference)
# 25. Given a list of numbers, find all duplicate elements using sets.
numbers = [1, 2, 2, 3, 4, 4, 5]
duplicates = set([x for x in numbers if numbers.count(x) > 1])
print(duplicates)
# 26. Write a program to check if two strings are anagrams using sets.
str1 = "listen"
str2 = "silent"
is_anagram = set(str1) == set(str2)
print(is_anagram)
# 27. Given a set of numbers, remove all even numbers.
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
num_set = {x for x in num_set if x % 2 != 0}
print(num_set)
# 28. Create a set comprehension to generate squares of numbers from 1 to 10.
squares = {x**2 for x in range(1, 11)}
print(squares)
# 29. From a given set, create a new set containing only numbers greater than 10.
num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
greater_than_10 = {x for x in num_set if x > 10}
print(greater_than_10)
# 30. Given multiple sets in a list, find the intersection of all sets.
sets_list = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
intersection = set.intersection(*sets_list)
print(intersection)
