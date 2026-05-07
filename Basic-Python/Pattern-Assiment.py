print("Simple Pyramid")
n=5
for i in range(1,n+1):
    for j in range(i):
        print('*',end='')
    print()

print("Rotated Simple Pyramid")
n=5
for i in range(n,0,-1):
    for j in range(i-1):
        print(" ",end='')
    for j in range((n+1)-i):
        print("*",end='')
    print()
print("Inverted Pyramid")
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end='')
    print()
print("Rotated Inverted Pyramid")
n=5
for i in range(n,0,-1):
    for j in range((n+1)-i):
        print(" ",end='')
    for j in range(i):
        print("*",end='')
    print()
print("Triangle")
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i):
        print("* ",end='')
    print()
print("Inverted Triangle")
n=5
for i in range(1,n+1):
    for j in range(i+1):
        print(" ",end='')
    for j in range((n+1)-i):
        print("* ",end='')
    print()
print("Numeric Pyramid")
n=5
for i in range(1,n):
    for j in range(i):
        print(i,end='')
    print()
print("Continuous Numeric Pyramid")
n=5
k=1
for i in range(1,n):
    for j in range(i):
        print(k," ",end='')
        k+=1
    print()
print("Rotated Number Pyramid")
n=5
k=1
n=0
for i in range(1,n):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i):
        print(k," ",end='')
        k+=1
    print()
print("palindrome Triangle")
n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i,0,-1):
        print(j,end='')
    for j in range(2,i+1):
        print(j,end='')
    print()
print("Alphabet Pyramid")
n=4
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end=' ')
    print()
print("Continuous Alphabet Pyramid")
n=4
k=1
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+k),end=' ')
        k+=1
    print()



