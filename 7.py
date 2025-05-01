#Loops 7
"""
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
z = 1

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print("Factorial of Numnerator = ",fact(n))



def ncr(n,r):
    if r > n:
        return 0 # ncr is 0 when r > n
    else:
        return fact(n)// (fact(r) * fact(n-r))


print("nCr = ",ncr(n,r))

"""


#For calculating nPr

n = int(input("Enter the Value of n: "))
r = int(input("Enter the value of r: "))

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print("Factorial of n: ",fact(n))

def npr(n,r):
    if r > n:
        return 0
    else:
        return fact(n)//fact(n-r)

print("nPr = ",npr(n,r))



















