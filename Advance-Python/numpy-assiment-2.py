# 🟢Section A — Array Creation & Basics
import numpy as np
# Q1. Create a One-Dimensional Array
# Create a NumPy array containing values from 1 to 10.
# Then:
# 1. Print the shape
# 2. Print the size
# 3. Print the number of dimensions
arr=np.arange(1,11)
print(arr.shape)
print(arr.size)
print(arr.ndim)

# Q2. Create Arrays Using NumPy Functions
# Create:
# 1. A 3×3 matrix of zeros
# 2. A 2×4 matrix of ones
# 3. A 4×4 identity matrix
zeros_matrix=np.zeros((3,3))
ones_matrix=np.ones((2,4))
identity_matrix=np.eye(4)
print(zeros_matrix)
print(ones_matrix)
print(identity_matrix)

# Q3. arange() vs linspace()

# 1. Create an array from 0 to 20 with step size 2 using arange()
# 2. Create 5 equally spaced values between 0 and 20 using linspace()
# 3. Explain the difference between both outputs
arr_arange=np.arange(0,21,2)
arr_linspace=np.linspace(0,20,5)
print(arr_arange)
print(arr_linspace)
# arange creates values based on a specified step size 
# linspace creates a specific number of equally spaced values between a start and end.

# Q4. Data Types
# Create:
# [1,2,3,4]
arr2=np.array([1,2,3,4])
# 1. Check datatype
print(arr2.dtype)
# 2. Convert datatype to float
arr2_float=arr2.astype(float)
print(arr2_float)

# 🟡Section B — Indexing & Slicing
# Q5. Basic Indexing
# Given:
arr2 = np.array([10,20,30,40,50])
# Perform:
# 1. Print first element
print(arr2[0])
# 2. Print last element
print(arr2[-1])
# 3. Print middle element
print(arr2[len(arr2)//2])
# 4. Reverse the array
print(arr2[::-1])


# Q6. Basic Slicing
# Using the same array:
# 1. Extract first 3 elements
print(arr2[:3])
# 2. Extract last 2 elements
print(arr2[-2:])
# 3. Extract elements from index 1 to 4
print(arr2[1:5])
# 4. Extract every second element
print(arr2[::2])

# Q7. Matrix Indexing
# Given:

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Perform:
# 1. Print element 5
print(arr3[1,1])
# 2. Print second row
print(arr3[1,:])
# 3. Print third column
print(arr3[:,2])
# 4. Print last row using negative indexing
print(arr3[-1,:])

# Q8. Matrix Slicing
# Using the same matrix:
# 1. Extract:
# [[1,2],
# [4,5]]
print(arr3[0:2,0:2])
# 2. Extract:
# [[5,6],
# [8,9]]
print(arr3[1:3,1:3])

# 3. Extract corner elements [1,3,7,9]
print(arr3[[0,0,2,2],[0,2,0,2]])
# Q9. Reverse Rows & Columns

# Using:

arr5=np.array([[1,2,3],[4,5,6],[7,8,9]])

# 1. Reverse rows
print(arr5[::-1,:])
# 2. Reverse columns
print(arr5[:,::-1])
# 3. Reverse both rows and columns
print(arr5[::-1,::-1])

# 🔵Section C — Boolean Indexing

# Q10. Filtering Values

arr4 = np.array([5,10,15,20,25,30])

# 1. Extract values greater than 15
print(arr4[arr4>15])
# 2. Extract even numbers
print(arr4[arr4%2==0])
# 3. Replace values greater than 20 with 0
arr4[arr4>20]=0
print(arr4)

# Q11. Boolean Indexing in Matrix
# Given:
arr6 = np.array([[10,20,30],[40,50,60]])

# 1. Extract values greater than 25
print(arr6[arr6>25])
# 2. Replace values greater than 25 with -1
arr6[arr6>25]=-1
print(arr6)

# 🟣Section D — Broadcasting

# Q12. Scalar Broadcasting
# Add 10 to:

arr7=np.array([1,2,3,4])
arr7=arr7+10
print(arr7)

# Q13. Row-wise Broadcasting
# Add [1,2,3] to:
arr8=np.array([[10,20,30],[40,50,60]])
newarr=np.array([1,2,3])
arr8=arr8+newarr
print(arr8)

# Given:

A = np.array([[10,20,30],[40,50,60]])
B = np.array([1,2,3])

# Add B to A .
A = A + B
print(A)

# Q14. Column-wise Broadcasting
# Given:

A = np.array([[10,20,30],[40,50,60]])
B = np.array([[1],[2]])
# Add B to A .
A=A+B
print(A)

# Q15. Broadcasting Validity
# Check whether these operations are valid:
# 1. (2,3) + (3,)
# invalid because shapes 2*3 is not compatible with 3

# 2. (3,2) + (2,)
# valid because shapes 3*2 is compatible with 2

# 3. (2,3) + (2,)
# valid because shapes 2*3 is compatible with 2

# Explain why.
# If the dimensions are equal or one of them is 1, then the arrays are compatible for broadcasting. 

# 🟠Section E — Aggregation & Axis

# Q16. Sum Operations
# Given:

arr9 = np.array([[1,2,3],[4,5,6]])

# Find:
# 1. Total sum
print(np.sum(arr9))
# 2. Row-wise sum
print(np.sum(arr9, axis=1))
# 3. Column-wise sum
print(np.sum(arr9, axis=0))

# Q17. Statistical Operations

# Using the same matrix:
# 1. Mean of each row
print(np.mean(arr9, axis=1))
# 2. Mean of each column
print(np.mean(arr9, axis=0))
# 3. Maximum value in each row
print(np.max(arr9, axis=1))
# 4. Minimum value in each column
print(np.min(arr9, axis=0))

# Q18. Standard Deviation
arr9=np.array([[1,2,3],[4,5,6]])
print(np.std(arr9))

# Find standard deviation of: [10,20,30,40,50]
arr10=np.array([10,20,30,40,50])
print(np.std(arr10))

# 🔴Section F — Reshape & Flatten

# Q19. Reshaping
# Create:

arr11=np.array([1,2,3,4,5,6])

# Then:
# 1. Convert into 2×3 matrix
arr11 = arr11.reshape(2, 3)
# 2. Convert into 3×2 matrix
arr11 = arr11.reshape(3, 2)
# 3. Convert into column vector
arr11 = arr11.reshape(-1, 1)

# Q20. Flattening
# Given:

arr12=np.array([[1,2,3],[4,5,6],[4,5,6]])

# 1. Flatten using flatten()
print(arr12.flatten())
# 2. Flatten using ravel()
print(arr12.ravel())
# 3. Explain difference
# flatten() returns a copy of the array, while ravel() returns a view. 
# Modifying the result of ravel() will affect the original array, while modifying the result of flatten() will not.

# ⚫Section G — Copy vs View

# Q21. Observe Memory Sharing
# Run:
a = np.array([1,2,3])
b = a
b[0] = 100

# 1. Print a
print(a)
# 2. Explain why it changed
# b is not a copy of a,it is a reference to a (same array in memory).
# Q22. Create Independent Copy
# Modify previous code so changing b does not affect a .
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)
print(b)

# 🟤Section H — Normalization

# Q23. Min-Max Normalization

# Normalize:
# [10,20,30,40,50]
# between 0 and 1.
arr13=np.array([10,20,30,40,50])
normalized=(arr13-arr13.min())/(arr13.max()-arr13.min())
print(normalized)

# Q24. Matrix Normalization
# Normalize:
# [[1,2],
# [3,4]]
arr14=np.array([[1,2],[3,4]])
normalized_matrix=(arr14-arr14.min())/(arr14.max()-arr14.min())
print(normalized_matrix)

# Q25. Column-wise Normalization
# Normalize each column independently:
# [
# [10,100],
# [20,200],
# [30,300]
# ]
arr15=np.array([[10,100],[20,200],[30,300]])
minarr=arr15.min(axis=0)
maxarr=arr15.max(axis=0)
result=(arr15-minarr)/(maxarr-minarr)
print(result)

# 🟠Section I — Random Module (NEW)

# Q26. Generate Random Float Values
# Generate:
# 1. A single random float between 0 and 1
var=np.random.rand()
print(var)
# 2. An array of 5 random float values
arr_r=np.random.rand(5)
print(arr_r)

# Q27. Random Integer Array
# Generate:
# 1. 5 random integers between 1 and 10
rand_int=np.random.randint(1,11,5)
print(rand_int)
# 2. A 3×3 matrix of random integers between 50 and 100
rand_mat=np.random.randint(50,101,(3,3))
print(rand_mat)

# Q28. Random Choice
# Given:
# arr = [10,20,30,40,50]
# Randomly select:
# 1. One value
arr = np.array([10,20,30,40,50])
rand_var2=np.random.choice(arr)
print(rand_var2)
# 2. Three values
rand_var3=np.random.choice(arr, size=3)
print(rand_var3)

# Q29. Random Normal Distribution
# Generate:
# 1. 5 random values from normal distribution
rand_var4=np.random.randn(5)
print(rand_var4)
# 2. A 2×3 matrix using randn()
random_normal_matrix=np.random.randn(2,3)
print(random_normal_matrix)

# Q30. Set Random Seed
# 1. Generate random integers between 1 and 100 using:
# np.random.seed()
# Run the code multiple times and observe the output.
np.random.seed(42)
random_integers_seed=np.random.randint(1,101,5)
print(random_integers_seed)
# 2. Explain why the same values are generated.
# This ensures that sequence of random numbers generated is the same every time. 
# It is useful for you to get the same results across different iterations.


# Q32. Permutation
# Using:
# arr = np.array([1,2,3,4,5])
# 1. Generate a permutation of the array
arr16 = np.array([1,2,3,4,5])
var_permut=np.random.permutation(arr16)
print(var_permut)
# 2. Compare permutation with shuffle
# permutation returns a new array with the elements permuted, while shuffle modifies the original array in place.
arr17 = np.array([1,2,3,4,5])
np.random.shuffle(arr17)
print(arr17)

# Q33. Random Matrix Statistics
# Generate a 4×4 matrix of random integers between 1 and 50.
rand_mat2=np.random.randint(1,51,(4,4))
print(rand_mat2)
# Then:
# 1. Find maximum value
print(np.max(rand_mat2))
# 2. Find minimum value
print(np.min(rand_mat2))
# 3. Find row-wise sum
print(np.sum(rand_mat2, axis=1))
# 4. Find column-wise mean
print(np.mean(rand_mat2, axis=0))

# Q34. Random Filtering
# Generate 10 random integers between 1 and 100.
rnad_var5=np.random.randint(1,101,10)
print(rnad_var5)
# 1. Extract even numbers
print(rnad_var5[rnad_var5%2==0])
# 2. Extract values greater than 50
print(rnad_var5[rnad_var5>50])
# 3. Replace values less than 30 with 0
rnad_var5[rnad_var5<30]=0
print(rnad_var5)

# Q35. Random Normalization Challenge
# Generate a random array of size 8.
rand_arr=np.random.rand(8)
print(rand_arr)
# Normalize all values between 0 and 1.
result=(rand_arr-rand_arr.min())/(rand_arr.max()-rand_arr.min())
print(result)

# 🚀Bonus Challenges

# Q36.
# Create a 5×5 matrix with values from 1 to 25.
arr16=np.arange(1,26).reshape(5,5)
print(arr16)
# Then:
# 1. Print diagonal elements
print(arr16.diagonal())
# 2. Replace diagonal elements with 0
arr16[np.arange(5), np.arange(5)] = 0
print(arr16)

# Q35.

# Create:
# [[1,1,1],
# [2,2,2],
# [3,3,3]]
# without manually typing rows.
arr17=np.arange(1,4).reshape(3,1)
arr17=arr17+np.zeros((1,3))
print(arr17)

# Q36.

# Generate a random matrix and:
# 1. Reverse rows
rand_mat3=arr17[::-1]
print(rand_mat3)

# 2. Reverse columns
rand_mat4=arr17 [:, ::-1]
print(rand_mat4)

# 3. Flatten the matrix
rand_mat5=arr17.flatten()
print(rand_mat5)

# Q37.

# Generate a random 3×3 matrix and extract:
# 1. First row
rand_mat6=np.random.rand(3,3)
print(rand_mat6)
print(rand_mat6[0])
# 2. Last column
print(rand_mat6[:, -1])
# 3. Center element
print(rand_mat6[1, 1])
# 4. Corner elements
print(rand_mat6[0, 0])
print(rand_mat6[0, -1])
print(rand_mat6[-1, 0])
print(rand_mat6[-1, -1])


