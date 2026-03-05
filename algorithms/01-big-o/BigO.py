#Big O Notation -> O()
#Time Complexity - Space Complexity
# O(1)        → Constant
# O(log n)    → Logarithmic
# O(n)        → Linear
# O(n log n)  → Linearithmic
# O(n²)       → Quadratic
# O(n³)       → Cubic
# O(n!)       → Factorial

import math

def bigon(n):
    for i in range(0,n):
        print(i)

bigon(10)


def bigon2(n):
    for i in range(0,n):
        for j in range(0,n):
            print(i,j)

bigon2(5)


def bigon3(n):
    for i in range(0,n):
        for j in range(0,n):
            for k in range(0,n):
                print(i,j,k)

bigon3(5)


def logn(n):
    while(n>1):
        n = math.floor(n/2)
        print(n)

logn(100)


def nlogn(n):
    lim = n
    while n>1:
        n=math.floor(n/2)
        for i in range(1,lim):
            print(i)

nlogn(16)

##algoritma nfactorial kadar çağırılıyor
def  nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n-1)

nfactorial(3)