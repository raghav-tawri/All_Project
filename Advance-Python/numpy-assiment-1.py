import numpy as np

# Q1. One-Dimensional Array
arr=np.array([10,20,30,40,50])
# 1. Print first element
print(arr[0])
# 2. Print last element
print(arr[0])
# 3. Print elements from index 1 to 3
print(arr[0:4])
# 4. Reverse the array
print(arr[::-1])

# Q2. Matrix Basics

# Create a 2×3 matrix using np.arange(1,7)
arr2=np.arange(1,7)
matrix1=arr2.reshape(2,3)
print(matrix1)
# 1. Print shape
print(matrix1.shape)
# 2. Print second row
print(matrix1[1])
# 3. Print first column
print(matrix1[:,0])

# 🟡Section B: Slicing (VERY IMPORTANT)

# Q3. Basic 1D Slicing

arr2 = np.array([1,2,3,4,5,6])

# 1. Extract elements from index 1 to 4
print(arr2[1:5])
# 2. Extract first 3 elements
print(arr2[:3])
# 3. Extract last 3 elements
print(arr2[-3:])
# 4. Reverse the array using slicing
print(arr2[::-1])

# Q4. Step Slicing
print()
# Using the same array:
# 1. Extract every 2nd element
print(arr2[::2])
# 2. Extract elements in reverse order with step
# 3. Extract elements starting from index 1 with step 2
print(arr2[1::2])

# Q5. 2D Slicing (Sub-matrix)
arr3 = np.array([
[10,20,30],
[40,50,60],
[70,80,90]
])

# Extract:
# 1. First two rows and first two columns
print(arr3[0:2])
print(arr3[:,:2])
# 2. Last two rows and last two columns
print(arr3[-2:, -2:])
# 3. Entire second row
print(arr3[1])
# 4. Entire third column
print(arr3[2])

# Q6. Advanced 2D Slicing
# 1. Extract:
# [[20,30],
# [50,60]]
print(arr3[:2,1:])

# 2. Extract:
# [[10,30],
# [70,90]]
print(arr3[0::2,0::2])

# 3. Reverse: rows and columns
print(arr3[::-1,::-1])

# Q7. Negative Indexing + Slicing
arr4 = np.array([10,20,30,40,50])
# Perform:
# 1. Extract last 2 elements
print(arr4[-2])
# 2. Extract all elements except last one
print(arr4[:-1])
# 3. Reverse using negative slicing
print(arr4[::-1])

# 🔵Section C: Boolean Indexing

# Q8
arr5 = np.array([10,20,30,40,50])

# 1. Extract values greater than 25
print(arr5[arr5>25])
# 2. Replace values greater than 25 with 0
arr5[arr5>25]=0
print(arr5)

# 🟣Section D: Broadcasting

# Q9
# Add [1,2,3] to:
# [[10,20,30],
# [40,50,60]]
arr6=np.array([[10,20,30],[40,50,60]])
newarr=np.array([1,2,3])
arr7=np.append(arr6,newarr)
print(arr7)
print()

# Q10
# Add column vector:
# [[1],
# [2]]  to:
# [[10,20,30],
# [40,50,60]]
col = np.array([[1],[2]])
arr8 = np.array([[10, 20, 30],[40, 50, 60]])
result = arr8 + col
print(result)
print()

# 🟠Section E: Axis & Aggregation

# Q11
arr9=np.array([[1,2,3],[4,5,6]])
# 1. Find total sum
print(np.sum(arr9))
# 2. Find column-wise sum
print(np.sum(arr9,axis=0))
# 3. Find row-wise sum
print(np.sum(arr9,axis=1))
print()

# Q12
# 1. Mean of each row
print(np.mean(arr9,axis=0))
# 2. Maximum of each column
print(np.max(arr9, axis=0))
print()
# 🔴Section F: Reshape & Flatten

# Q13
arr10=np.array([1,2,3,4,5,6])
# into:
# 1. 2×3 matrix
print(arr10.reshape(2, 3))
# 2. 3×2 matrix
print(arr10.reshape(3, 2))

# Q14
# Flatten:
# [[1,2,3],
# [4,5,6]]
print(arr10.flatten())
print()

# ⚫Section G: Copy vs View
# Q15 run
a = np.array([1,2,3])
b = a
b[0] = 100
print(a)
print(b)
print()

# 1. What is value of a ?
# b a=[100,2,3]
# 2. Why?
#  b does not create new array because of it it point to the same memory location

# Q16
# Fix above using .copy()
afix = np.array([1, 2, 3])
bfix = afix.copy()   # b gets its OWN separate memory
bfix[0] = 100
print(afix)
print(bfix)
print()

# 🧩Section H: Mixed Slicing + Logic

# Q17
arr12=np.array([[1,2,3],[4,5,6],[7,8,9]])
# Extract:
# 1. Middle row
print(arr12[1, :]) 
# 2. Middle column
print(arr12[:, 1]) 
# 3. Corners → [1,3,7,9]
arr13 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
corners = arr13[[0, 0, 2, 2], [0, 2, 0, 2]]
print(corners)

print()

# Q18
matrix = [[i, i, i] for i in range(1, 4)]
print(matrix)

print()
