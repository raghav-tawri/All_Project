# 1 Given a list of integers, find all pairs of elements whose sum is equal to a given
# number.
ls=[1,2,3,4,5,6,7,8,9]
target=16
pairs=set()
for n in ls:
    sums=target-n
    if sums in ls:
        pairs.add(tuple(sorted((sums,n))))
print(pairs)

# 2 Take a list of numbers and find the element which appears the maximum number of
# times.
lsn=[1,2,3,4,3,1,1,2,4,5]
print(lsn[0])
dict1=dict()
for i in lsn:
    dict1[i]=lsn.count(i)
print(dict1)
# 3 Given a list, remove consecutive duplicate elements. Example: [1,1,2,2,2,3,1,1] →
# [1,2,3,1]
ls2=[1,1,2,2,2,3,1,1]
res=[ls2[0]]
for i in range(1,len(ls2)):
    if ls2[i]!=ls2[i-1]:
        res.append(ls2[i])
print(res)
# 4 Take a list of integers and create a new list that contains only those elements which
# are greater than all elements before them.


# ls3=[9,8,7,6,5,4,3]
# res2=list()
# res2=sorted(ls3)
# print("Question 4 :- ",res2)

# 5 Given a list, shift all negative numbers to the beginning and positive numbers to the
# end without changing their relative order.
ls4=[-1,2,-3,4,-5,6]
neg=list()
pos=list()
for i in ls4:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print(neg+pos)
# 6 Take a list and find all the elements that are common between two given lists.
ls5=[1,2,3,4,5]
ls6=[4,5,6,7,8]
print(set(ls5).intersection(set(ls6)))
# 7 Given a list of numbers, replace every element with the greatest element on its right
# side.
ls7=[1,2,3,4,5]
for i in range(len(ls7)-1):
    ls7[i]=max(ls7[i+1:])
ls7[-1]=-1
print(ls7)
# 8 Take a list and find the longest increasing contiguous sublist.
ls8=[1,2,3,2,5,6,7]
max_len=1
current_len=1
for i in range(1,len(ls8)):
    if ls8[i]>ls8[i-1]:
        current_len+=1
    else:
        max_len=max(max_len,current_len)
        current_len=1
max_len=max(max_len,current_len)
print(max_len)
# 9 Given a list, find the first repeating element.
ls9=[1,2,3,4,2,5,6]
seen=set()
first_repeating=None
for num in ls9:
    if num in seen:
        first_repeating=num
        break
    seen.add(num)
print(first_repeating)
# 10 Take a list and rearrange it in such a way that first element is maximum, second is
# minimum, third is second maximum, fourth is second minimum, and so on.
ls10=[1,2,3,4,5,6]
ls10.sort()
result=[]
left=0
right=len(ls10)-1
while left<=right:
    if left==right:
        result.append(ls10[left])
    else:
        result.append(ls10[right])
        result.append(ls10[left])
    left+=1
    right-=1
print(result)
# 11 Given a list of integers, find all the triplets whose sum is zero.
ls11=[-1,0,1,2,-1,-4]
triplets=set()
for i in range(len(ls11)):
    for j in range(i+1,len(ls11)):
        for k in range(j+1,len(ls11)):
            if ls11[i]+ls11[j]+ls11[k]==0:
                triplets.add(tuple(sorted((ls11[i],ls11[j],ls11[k]))))
print(triplets)
# 12 Take a list and rotate it to the left by k positions.
ls12=[1,2,3,4,5]
k=2
k=k%len(ls12)
rotated=ls12[k:]+ls12[:k]
print(rotated)
# 13 Given a list, create a new list where each element is the product of all other elements
# except itself.
ls13=[1,2,3,4]
product_list=[]
for i in range(len(ls13)):
    product=1
    for j in range(len(ls13)):
        if i!=j:
            product*=ls13[j]
    product_list.append(product)
print(product_list)
# 14 Take a list and find the missing number from a list containing numbers from 1 to n.
ls14=[1,2,4,5]
n=5
missing_number=n*(n+1)//2-sum(ls14)
print(missing_number)
# 15 Given a list, remove all elements which are smaller than the element just before them.
ls15=[1,3,2,5,4]
result2=[ls15[0]]
for i in range(1,len(ls15)):
    if ls15[i]>=ls15[i-1]:
        result2.append(ls15[i])
print(result2)
# 16 Take a list and divide it into sublists of size k.
ls16=[1,2,3,4,5,6,7]
k=3
sublists=[ls16[i:i+k] for i in range(0,len(ls16),k)]
print(sublists)
# 17 Given a list, find the maximum difference between two elements such that the larger
# element comes after the smaller one.
ls17=[7,1,5,3,6,4]
min_element=ls17[0]
max_diff=0
for i in range(1,len(ls17)):
    if ls17[i]<min_element:
        min_element=ls17[i]
    else:
        max_diff=max(max_diff,ls17[i]-min_element)
print(max_diff)
# 18 Take a list and find all leaders in the list (an element is leader if it is greater than all
# elements to its right).
ls18=[16,17,4,3,5,2]
leaders=[]
max_from_right=ls18[-1]
leaders.append(max_from_right)
for i in range(len(ls18)-2,-1,-1):
    if ls18[i]>max_from_right:
        leaders.append(ls18[i])
        max_from_right=ls18[i]
leaders.reverse()
print(leaders)
# 19 Given a list, move all duplicate elements to the end of the list.
ls19=[1,2,3,2,4,5,1]
seen=set()
unique_elements=[]
duplicates=[]
for num in ls19:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)
        unique_elements.append(num)
result3=unique_elements+duplicates
print(result3)
# 20 Take a list and check if it can be sorted by only one swap of two elements.
ls20=[1,5,3,4,2]
sorted_ls20=sorted(ls20)
diff_indices=[i for i in range(len(ls20)) if ls20[i]!=sorted_ls20[i]]
if len(diff_indices)==2:
    i,j=diff_indices
    ls20[i],ls20[j]=ls20[j],ls20[i]
    if ls20==sorted_ls20:
        print("Yes, it can be sorted by one swap.")
    else:
        print("No, it cannot be sorted by one swap.")
else:
    print("No, it cannot be sorted by one swap.")