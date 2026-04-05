# 1. Find Frequency of Each Element
# Problem Statement: Given a list of integers, count the frequency of each element and display the
nums = [1, 2, 2, 3, 1, 4, 2]
frequency = {}
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num, count in frequency.items():
    print(f"{num} -> {count}")
# 2. Rotate a List Left by One Position
# Problem Statement: Rotate the list one position to the left. The first element moves to the end.
nums = [10, 20, 30, 40, 50]
rotated = nums[1:] + nums[:1]
print(rotated)
# 3. Find Index of All Occurrences of a Given Element
# Problem Statement: Print all index positions where the target element occurs.
nums = [5, 2, 7, 2, 9, 2]
target = 2
indices = []
for i in range(len(nums)):
    if nums[i] == target:
        indices.append(i)
print(indices)
# 4. Remove All Negative Numbers from a List
# Problem Statement: Remove all negative numbers and return the updated list.
nums = [3, -1, 5, -7, 8, -2]
positive_nums = [num for num in nums if num >= 0]
print(positive_nums)
# 5. Check Whether a List is Palindrome
# Problem Statement: Check whether the list reads the same forward and backward.
nums = [1, 2, 3, 2, 1]
if nums == nums[::-1]:
    print("Palindrome")
else:    
    print("Not Palindrome")
# 6. Merge Two Lists and Remove Duplicates
# Problem Statement: Merge two lists into one and remove duplicate elements.
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged = list(set(list1 + list2))
print(merged)

# 7. Find Pairs Whose Sum Equals Target Value
# Problem Statement: Find all pairs of elements whose sum equals the target value.
nums = [2, 4, 3, 5, 7]
target = 7
pairs = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))
print(pairs)
# 8. Find Missing Number from 1 to n
# Problem Statement: A list contains numbers from 1 to n with one number missing. Find the missing
# number.
nums = [1, 2, 4, 5, 6]
n = len(nums) + 1
total_sum = n * (n + 1) // 2
missing_number = total_sum - sum(nums)
print(missing_number)
# 9. Remove Elements That Appear More Than Once
# Problem Statement: Remove elements that occur more than once and keep only unique elements.
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in nums:
    if nums.count(num) == 1:
        unique.append(num)
print(unique)